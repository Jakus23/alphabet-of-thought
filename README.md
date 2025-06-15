# alpha (.aot)

Alpha is a lightweight, readable, text language. Designed for real-world cognitive and collaborative work, for teams who want to formulate, connect, communicate, and automate their knowledge. It’s not about organising information - Alpha helps you abstract meaning from existing knowledge and share understanding with others and yourself over time.

## What is Alpha?

Alpha is built on a few powerful principles:
- I think uniquely, but I always extend existing thought structures to think.
- Structured thoughts are ideas that connect to each other.
- Knowledge works best when organised as a *tree* - not linear text, visuals, or code.

### Elements

Alpha has *ideas* and *connections* between ideas to build structured thought. Here's how it works:

#### Idea Types (What you're describing)

*context*

1. Concepts – Capitalised terms (e.g. `Person`)
2. Attributes – Lowercase terms (e.g. `full name`)
3. Aliases – Alternatives in parentheses (e.g. `Person (Natural Person)`)
4. Maps – Indicate omitted or incomplete data (e.g. `... irrelevant data not included`)

*content (data)*

5. Attribute Defaults – Expected values (e.g. `age: 42`)
6. Examples (e.g. `- Mark Zuckerberg`)
7. Code – Inline snippets (e.g. `for person in persons:`)

#### Connection Types (How ideas relate)

1. is-a - Concepts organised hierarchically (indentation implies inheritance)

```
    Organisation
        Business
```
2. has-a – Concepts have attributes

```
    Person
        full name
```
3. value-is – Assign a value to an attribute

```
    full name: Gottfried Leibniz
```
4. has-another-name – Aliases using parentheses

```
    Person (Natural Person)
```
5. has-example – Instances of concepts, attributes or other examples
```
    Person
        - Mark Zuckerberg
```
6. attribute-is-a-concept – Attributes that are also concepts

```
    Years
    age years: 5
```
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
Report
    - http://www.w3.org/TR/rdf-syntax-grammar
        title dc: RDF/XML Syntax Specification (Revised)
        editor ex: Dave Beckett
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
```

This example shows how Alpha retains all structure and meaning — but in a clearer, more accessible format that is infinitely extendable.

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

## Inspiration
Alpha is influenced by:
- Charles Peirce’s How to Make Our Ideas Clear
- Leibniz’s Alphabet of Human Thought
- Practical modern software development

Ideal for knowledge workers
- Formulate and communicate complicated ideas effortlessly
- Reduce confusion and duplication
- Use as a problem solving tool or remembering problems already solved 
- Documenting business knowledge for automating work with AI


Perfect for:
- Knowledge workers & analysts
- Business documentation
- Systems thinkers


[1] Aspects
True thoughts are hard won. They emerge from incorporating many aspects while myopic thoughts dies from not adjusting from self-contridiction and counter-examples.

- States
- Metrics
- Time
- Stakeholders
- Functions
- Entity
- Data Types (trees, graphs, associatives, composites)
- Location
- Operational (cause and effect)
