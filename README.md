# alpha (.aot)

> Connect ideas. Readable by you, your organization and computers.

- trivial text notation instead of boxes and arrows
- recursive
- no patterns or symbols
- world class practices inspired by python, ymal, JSON, Clojure, SQL, org and Markup
- ideal for working productively with computers

There are 7 idea types and 6 relationship types

## ideas (the “tokens”)

*context*

1. concept (first word is capitalised) like `Person`
2. attribute (a series of lowercase words) like `full name`
3. alias (between parenthesis after a concept or attribute) like `(integer)`
4. map (ellipsis followed by an optional incompleteness explanation) like `... irrelevant data not included`

*content*

5. default (the value after a semicolon and space for attributes or indentation on the next line a dash for the most likely value for an attribute) like `: 2.1 billion`
6. terminal (the value after a dash for an example of a concept) like `- Germany`
7. code like `"for i in range(7): print(i)"`

## relationships (the implied “token predicates”)

1. is-a (indentation on the next line between one concept, another or a terminal, or between an attribute and a terminal)

```
    Organization
        Business
          ... “a business is-a organization”
```

2. has-a (indentation from a concept or terminal to an attribute or indentation from a concept or terminal and the header of a markdown table)

```
    Person
        first name
          ... “a person has-a first name”
```
3. has-example (from a concept or terminal to another terminal)

```
    Person
        - Mark Zuckerberg
          ... “a person has-example Mark Zuckerberg”
```

4. value-is (semicolon and space after attribute or values in a markdown table)

```
    first name: John
      ... “first name value-is John”
```

5. has-another-name (parenthesis after a concept or attribute)

```
    Person (Natural Person)
      ... “person has-another-name natural person”
    integer (int)
      ... “full name has-another-name int”
```
6. map-unspecified (ellipsis)

```
    Number
      - 1
      - 2.6
      - ... more numbers
      ... more number types like integer

```

## alpha in action

```
Data Types
    Number
        Imaginary
        Irrational
        Float
            Big float
            Small float
            description: Decimal point values
        Fraction
            Decimal
            Fraction
        Integer
            Small integer
            Large integer
            Postive small integers
            description: Whole numbers
    Date
    Boolen
        - True
        - False
    None
    Set
    Dictionary
        - {"key":"value"}
    Sequence
        String
        List
        Tuple
Object
    Country
        - Germany
        - United States of America
    Person
        full name (text): Gottfried Wilhelm von Leibniz
        home language (text): Latin
            - German
            - French
            - ...
        nationality (country): Germany
        birthdate (date): 1646-07-01
        gender (text): Male
          - Male
          - Female
        first name (text): Gottfried
        surname (text): Leibniz
        title (text): Dr
          - Mnr
          - Miss
          - Mrs
          - Ms
          - Dr
          - Prof
        initials (text): GW
        date of death (date): 	1716-11-14 
        marital status (text): Single
          - Married
          - Divorced
          - Single
          - Widow
          - Widower
        occupation status (text): Employed
          - Employed
            - Contributor
            - Manager
            - Executive
            - Non Executive
            - Independent
          - Self Employed
          - Unemployed
          - Retired
        residential status (text): Home Owner
          - Renting
          - Home Owner
        education standard classification (text): Post Doc
          - Childhood
          - Primary
          - Lower Secondary
          - Upper Secondary
          - Postsecondary Non Tertiary
          - Short Cycle Tertiary
          - Bachelors
          - Masters
          - Doctors
          - Post Doc
        child count (integer): 0

```