import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    const collection = vscode.languages.createDiagnosticCollection('aot');
    context.subscriptions.push(collection);

    vscode.workspace.onDidSaveTextDocument(document => {
        if (document.languageId === 'aot') {
            lintDocument(document, collection);
        }
    });

    vscode.workspace.onDidOpenTextDocument(document => {
        if (document.languageId === 'aot') {
            lintDocument(document, collection);
        }
    });

    vscode.workspace.onDidChangeTextDocument(event => {
        if (event.document.languageId === 'aot') {
            lintDocument(event.document, collection);
        }
    });
}

function lintDocument(document: vscode.TextDocument, collection: vscode.DiagnosticCollection) {
    const filePath = document.fileName;
    const workspaceFolder = vscode.workspace.workspaceFolders?.[0].uri.fsPath || '';
    const pythonScript = path.join(workspaceFolder, 'main.py');

    // Run the Python parser as a subprocess
    exec(`python "${pythonScript}" "${filePath}"`, (error, stdout, stderr) => {
        const diagnostics: vscode.Diagnostic[] = [];
        // Parse stderr or stdout for error messages
        const lines = (stderr + stdout).split('\n');
        for (const line of lines) {
            // Example error: Illegal character 'x' in line 12
            const match = line.match(/Illegal character '(.+)' in line (\d+)/);
            if (match) {
                const lineNum = parseInt(match[2], 10) - 1;
                diagnostics.push(new vscode.Diagnostic(
                    new vscode.Range(lineNum, 0, lineNum, document.lineAt(lineNum).text.length),
                    `Illegal character '${match[1]}'`,
                    vscode.DiagnosticSeverity.Error
                ));
            }
            // Example syntax error: Syntax error at '...'
            const syntaxMatch = line.match(/Syntax error at '(.+)'/);
            if (syntaxMatch) {
                diagnostics.push(new vscode.Diagnostic(
                    new vscode.Range(0, 0, 0, 1),
                    `Syntax error at '${syntaxMatch[1]}'`,
                    vscode.DiagnosticSeverity.Error
                ));
            }
        }
        collection.set(document.uri, diagnostics);
    });
}

export function deactivate() {}