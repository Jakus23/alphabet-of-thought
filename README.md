# alpha (.aot)

> connect your ideas in code

- For you, your organization your computers
- take structured notes that are easy to read, write, and maintain
- minimal syntax and cognitive load
- ideal for working productively

Alpha (.aot) is a lightweight, human-friendly markup for representing structured knowledge and relationships directly in text.

Your brain can focus on synthesis, abstraction and other emerging types of reasoning — making it ideal for those who want to capturing complex ideas, load working-memory with only important ideas quickly, automating work with AI, and make your ideas distinct and unambiguous.

A set of idea types and connection types provide a clear structure for representing knowledge, making it easier to express relationships, attributes, and examples in a consistent and understandable way.

## ideas (the “tokens”)

*context*

1. concept (first word is capitalised) like `Person`
2. attribute (a series of lowercase words) like `full name`
3. alias (between parenthesis after a concept or attribute) like `(string)`
4. map (ellipsis followed by an optional incompleteness explanation) like `... irrelevant data not included`

*content*

5. default (the value after a semicolon and space for attributes or indentation on the next line a dash for the most likely value for an attribute) like `: 2.1 billion`
6. terminal (the value after a dash for an example of a concept) like `- John`
7. code like `for person in persons: print(person)`

## connections (the implied “token predicates”)

1. is-a (indentation on the next line between one concept and another concept)

```
    Organization
        Business
            ... “an business is-a organization”
```

2. has-a (indentation from a concept or terminal to an attribute or indentation from a concept or terminal and the header of a markdown table)

```
    Person
        first name
          ... “a person has-a first name”
```
3. value-is (semicolon and space after attribute or values in a markdown table)

```
    first name: Gottfried
        ... “first name value-is Gottfried
    surname
        - von Leibniz
        - Zuckerberg
            ... “surname value-is von Leibniz or Zuckerberg”
```
4. has-another-name (parenthesis after a concept or attribute)

```
    Person (Natural Person)
      ... “person has-another-name natural person”
      full name (name)
          ... “full name has-another-name name”
```
5. has-example (from a concept or terminal, and  another terminal)

```
    Person
        - Mark Zuckerberg
            ... “person has-example Mark Zuckerberg”
```
6. value-for

```
    Person
        - Gottfried Wilhelm von Leibniz
        full name: Gottfried Wilhelm von Leibniz
            ... Gottfried Wilhelm von Leibniz value-for
```
7. attribute-is-a-concept

```
    Number
        Integer
        Float
    number: 5
        ... “number attribute-is-a-concept number”
    age (integer): 5
        ... “age attribute-is-a-concept integer”
```

## alpha in action
```
Data Types
    Number
        Integer
            is whole: yes
        ... more number types available
        precision
        memory usage
        availability operations
        is arithmetic supported: yes
    Date
    Boolean
        - True
        - False
        is binary: yes
        - {"key":"value"}
    Sequence
        String
        ... more sequences like lists are possible
```

