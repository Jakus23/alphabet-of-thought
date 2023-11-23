# alphabet of thought (.aot)

> A programming language with minimal syntax for capturing thoughts digitally

## thoughts are distinct and unambiguous context and content (i.e. ideas) and the relationships between those ideas

### ideas are captured with tokens

*context*

* concept (a series of capitalised words like “Internet”, “Network” or “”)
* attribute (a series of lowercase words)
* alias (capitalised or lowercase words between parenthesis),
* map (ellipsis)

*content*

* default (the value after a semicolon and space for attributes or a dash and a space for concepts)
* terminal (the value after a dash)
* truth value (“Yes”, “No” or “None”)

## relationships are captured with predicates

* is-a (indentation on the next line between one concept and another)
* has-a (indentation from a concept or example concept to an attribute or indentation from a concept or example concept and the header of a markdown table)
* example-of (semicolon and space after attribute or indentation and dash on the next line for an attribute or values in a markdown table)
* another-name-for (parenthesis after concept or attribute)

## the alphabet of thought language in action

The concepts are `Person`, `Address`, `Physcial Address` and `Contact`.
Example attributes are `full name`

```
Person
    ... the example values are for the first inventor of calculus, computers and the alphabet of human thought
    - Gottfried Wilhelm von Leibniz
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
        child count: 0
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
        Meta
            username
            profile pic (url)
            name
            email address
            phone number
            date of birth
            gender
            password
            current city
            current home town
            ...
        X (Twitter)
            ...
        ...
    ...
    is active: No
    termination date: None
Contact
| address              | person |
| -------------------- | ------ |
| Last Leibniz Address |        |
|                      |        |

```
You are obviously surpised by my concepts. Well, hopefully it's because there are many more ideas and relationships I packed in. That is the point of the language;

- it is very readable
- source control
- you can add and change knowledge
- share the knowledge

Now that we have a shared understanding of the concept of `Person`, `Address` and `Contact`,
there may be real-life phenomenon you want to capture.

```
- Gottfried Wilhelm Leibniz (Person)
    
    
- House Of Leibniz (Physcial Address)
    
- Where To Visit Leibniz To Understand His Life (Contact)
    person: Gottfried Wilhelm Leibniz
    address: Last Physcial Address Of Leibniz
```