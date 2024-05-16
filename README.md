# alpha (.aot)

> Connect ideas. Readable by you, your organization and computer.

- trivial text notation instead of boxes and arrows
- no complexity cargo-cult
- world class practices inspired by Python, ymal, JSON, Clojure, SQL, org and Markup
- thought relevance algorithmically calculated from git repo
- ideal for working productively with computers

There are 7 idea types and 5 relationship types

### ideas (the “tokens”)

*context*

1. concept (first word is capitalised) like `Social Graph`
2. attribute (a series of lowercase words) like `active users`
3. alias (between parenthesis after a concept or attribute) like `(Network)`
4. map (ellipsis followed by an optional incompleteness explanation) like `... irrelevant data not included`

*content*

5. default (the value after a semicolon and space for attributes or indentation on the next line a dash for the most likely value for an attribute) like `2.1 billion`
6. terminal (the value after a dash for an example of a concept) like `- Facebook`
7. truth value like `Yes`,`No` or `None` 

## relationships (the implied “token predicates”)

1. is-a (indentation on the next line between one concept, another or a terminal, or between an attribute and a terminal)

```
    Organization
        Business
            ... Organization is-a Business
```

2. has-a (indentation from a concept or terminal to an attribute or indentation from a concept or terminal and the header of a markdown table)

```
    Person
        first name
            ... Person has-a first name
```
3. has-example (from a concept or terminal to another terminal)

```
    Person
        - Mark Zuckerberg
            ... Person has-example Mark Zuckerberg
```

4. value-is (semicolon and space after attribute or values in a markdown table)

```
    first name: John
        ... first name value-is John 
```

5. has-another-name (parenthesis after concept or attribute)

```
    Person (Natural Person)
      ... Person has-another-name Natural Person
    full name (name)
      ... full name has-another-name name
```

## alpha in action

```
Social Graph
    - Vertical
    - Human
    - Content
    - Inert
    name: Facebook
        - Twitter
        - Instagram
        - Facebook
        - ...
    started: 2007-10-10
    active users: 2.9 billion
    base: Web
        - Web
        - Metaverse
        - Physical
    is user content allowed: Yes
Node
    Organization
        Business
        Non Government Organisation
        Government Organisation
        ...
    Person
        full name: Gottfried Wilhelm von Leibniz
        home language: Latin
            - German
            - French
            - ...
        nationality: Germany
        birthdate: 1646-07-01
        gender: Male
          - Male
          - Female
        first name: Gottfried
        surname: Leibniz
        title: Dr
          - Mnr
          - Miss
          - Mrs
          - Ms
          - Dr
          - Prof
        initials: GW
        date of death: 	1716-11-14 
        marital status: Single
          - Married
          - Divorced
          - Single
          - Widow
          - Widower
        occupation status: Employed
          - Employed
            - Contributor
            - Manager
            - Executive
            - Non Executive
            - Independent
          - Self Employed
          - Unemployed
          - Retired
        residential status: Home Owner
          - Renting
          - Home Owner
        education standard classification: Post Doc
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
        child count: 0
    social graph
Edge
    requester (stakeholder)
    responder (stakeholder)
    shared interest
        - Friends
        - Influencer
        - Family Tie
        - Professional Connection
        - Spam
User
    node
    is active: Yes
Address
    Physcial Address
        - Last Leibniz Address
          street number (physical address line): Holzmarkt 4-6
          suburb (physical address line): Mitte
          city: Hanover
          country: Germany
          code: 301591
        ... Leibniz had other addresses too
    Email
        full address: leibniztheman@gmail.com
        user name: leibniztheman
        email service provider: gmail
        top level domain: com
        is primary: Yes
    Telephone
        number: +77 777 7777
        type: Cellphone
            - Landline
            - Cellphone
    Social Media
    ...
    is active: No
    termination date: None
Contact
  address
  node
Allowed Device
    social graph: Facebook
    device: Smartphone
        - Computer
        - Smartphone
        - ...
    operating System: Android
        - iOS
    application
        - Web Browser
            - Safari
            - ...
        - App
        - ...

```