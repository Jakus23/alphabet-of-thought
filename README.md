# alpha (.aot)

*Connect your ideas in code.*
Alpha is a lightweight, readable language directly in plain text. Use `.aot` as the file extension for Alpha files.

## What is Alpha?

Alpha (.aot) is a *text* language for connecting ideas clearly, in a human-readable way. It’s especially useful to express complex concepts, communicate clearly, or automate understanding using AI.

Alpha is built on a few powerful principles:
- We all naturally have standard thought types.
- Knowledge works best when organised as a *tree of context* - not linear text, visuals, or code.
- It’s not just about storing information - Alpha helps you share understanding and abstract meaning.
- Text beats diagrams for sharing, editing, and maintaining knowledge over time.

# Core Concepts

Alpha uses *ideas* and *connections* to build structured thought. Here's how it works:

## Idea Types (What you're describing)

*context*

1. Concepts – Capitalized nouns (e.g. `Person`)
2. Attributes – Lowercase phrases (e.g. `full name`)
3. Aliases – Alternative names in parentheses (e.g. `Person (Natural Person)`)
4. Maps – Indicate omitted or incomplete data (e.g. `... irrelevant data not included`)

*content*

5. Attribute Defaults – Expected values (e.g. `age: 42`)
6. Concept Examples (e.g. `- Mark Zuckerberg`)
7. Code – Inline snippets (e.g. `for person in persons:`)

## Connection Types (How ideas relate)

1. is-a - Concepts organized hierarchically (indentation implies inheritance)

```
    Organization
        Business
            ... “an business is-a organization”
```

2. has-a – Concepts have attributes

```
    Person
        first name
```
3. value-is – Assign a value to an attribute

```
    full name: Gottfried Leibniz
```
4. has-another-name – Aliases using parentheses

```
    TODO: Not a good example, because multiple things are going on here
    Person (Natural Person)
      full name (name)
```
5. has-example – Examples as terminals

```
    Person
        - Mark Zuckerberg
```
6. attribute-is-a-concept – Attributes that are also concepts

```
    Years
    age years: 5
```
## Usage notes

Ideal for knowledge workers
- formulate and communicate complicated ideas,
- read key thoughts to get into flow,
- use as a problem solving tool, and 
- documenting business knowledge for automating work with AI

The language was inspired philosphically by Charles Pierce's "How to Make Our Ideas Clear" and the "Alphabet of Human Thought" proposal by Gottfried Leibniz, and modern programming practices and methodologies.

## Example: From RDF/Turtle to Alpha

Here’s the same information written in both  [Turtle (syntax)](https://en.wikipedia.org/wiki/Turtle_(syntax)) and Alpha.

### Turtle

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix ex: <http://example.org/stuff/1.0/> .

<http://www.w3.org/TR/rdf-syntax-grammar>
  dc:title "RDF/XML Syntax Specification (Revised)" ;
  ex:editor [
    ex:fullname "Dave Beckett";
    ex:homePage <http://purl.org/net/dajobe/>
  ]  .
```
### Alpha


```
Resource
    Report
        - The Subject Turtle Resource
            title dc: RDF/XML Syntax Specification (Revised)
            editor ex: Dave Beckett
            uri: http://www.w3.org/TR/rdf-syntax-grammar
    Editor
        - Dave Beckett
            full name ex: Dave Beckett
            home page ex uri: http://purl.org/net/dajobe/
    Prefix (Namespace)
        Dublin Core (DC)
            uri: http://purl.org/dc/elements/1.1/
        Example (Ex)
            uri: http://example.org/stuff/1.0/
        Resource Description Framework Syntax (RDF)
            uri: http://www.w3.org/1999/02/22-rdf-syntax-ns#
            is necessary for this example: no
    uri (uniform resource identifier)
```

This example shows how Alpha retains all structure and meaning—but in a clearer, more accessible format.

## Why Use Alpha?
Perfect for:
- Knowledge workers & analysts
- Business documentation
- Systems thinkers
- Teams who want to connect, communicate, and automate their knowledge
Benefits:
- Write and read complex structures effortlessly
- Reduce confusion and duplication
- Works great with AI and automation tools
- Designed for real-world cognitive and collaborative work

## Design Principles

### Readability
- Use full words, fix misspellings
- No synonyms for the same thing
- Use singular terms consistently

### Generality
- Avoid redundant concepts
- Use the most general valid term
- Add qualifiers where needed

### Granularity
- Concepts should reflect their parts
- Only go deeper if it’s worth the effort

### Dimensionality
Work with ideas in major structures:
### Strategy (target states, time, stakeholders, principles etc.)
### Function (actions and outcomes)
### Entity (inheritance, dependencies, etc.)
### Data Types (trees, graphs, associatives, composites)
### Operations (how things get done)

## Inspiration
Alpha is influenced by:
- Charles Peirce’s How to Make Our Ideas Clear
- Leibniz’s Alphabet of Human Thought
- Practical modern software development
    

