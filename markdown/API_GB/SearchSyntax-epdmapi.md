---
title: "Search Syntax"
project: "SOLIDWORKS PDM Professional API Help"
interface: ""
member: ""
kind: "topic"
source: "API_GB/SearchSyntax-epdmapi.html"
---

# Search Syntax

Before now you searched for documents in the vault using text, comparison operators, and wildcards. As of SOLIDWORKS PDM Professional 2020, you can search using a richer syntax set. To do this, create a new search object using [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html). The new search object gives all IEdmSearch* properties and method parameters the enhanced search syntax capability outlined below.

##### Summary of Syntax Kernel Logic

##### Basic Syntax - Details

- [Syntax expressions](#Syntax)
- [Patterns (Variable, Search, and Complex)](#Patterns)
- [Encapsulated expressions and complex patterns](#Encapsulated)
- [Patterns and comparisons](#Comparisons)
- [Explicit/implicit data types](#DataTypes)
- [Colon-attached specifiers](#Colon)

##### Advanced Syntax - Details

- [Advanced specifiers](#Advanced)
- [Multi-value specifiers](#multi-value)
- [Variable (@) and configuration (@@) bindings](#Bindings)
- [Colon-attached bindings](#Colon2)

##### Examples

- [Using Basic Search Syntax (VB.NET)](Using_Basic_Search_Syntax_Example_VBNET.htm)
- [Using Basic Search Syntax (C#)](Using_Basic_Search_Syntax_Example_CSharp.htm)

###### Summary of Syntax Kernel Logic

##### A. The basic rules - preparing variable names and search values

- Comparison operators: =, <, >, <>, <=, >=.
- Contains patterns (P) and comparisons (<= Q) can be combined using logical operators AND (&), OR (|) and NOT (!) and parentheses ().
- Negated comparisons are similar to negated simple patterns. For example, !=P is the same as !{=P}. <>P is the same as {!=P} and (< P | > P).
- Spaces may be used to divide operands and operators for readability.
- AND is implicit in patterns. For example, (P Q R) means P & Q & R.
- The order of logical operator processing is NOT, AND, OR.
- To search for spaces and special characters, quote them with " or escape them with \.
- A quotation mark inside a pattern is not interpreted. To recognize ", escape it with \.
- A backslash inside a pattern must also be escaped with \.
- \ escapes both inside and outside of quotations.
- * and ? are wildcards both inside and outside of quotations, but only in the context of Contains or !Contains.
- \ is not required before * and ? in variable/configuration names or with comparison operators.
- Numeric constants are compared as numbers only if the variable has a numeric data type.
- Correctly represented dates (as quoted or unquoted strings) are compared as dates only if the variable has the DATE data type.

[- Back to top -](#top)

##### B. Patterns and comparisons (explicit and implicit data types)

- Single-value search logic is the default search logic. All conditions are implicitly contained in {} (see [Encapsulated expressions and complex patterns](#Encapsulated)). You can use braces, but they do not change the underlying logic. In single-value search logic, condtions target single variables/condigurations. For example,

**A & B** and **{A B}** both find documents containing variable values that contain both A and B

- **: !P** finds documents even if they have no variable values.
- **{!P}** only finds documents with existing variable values.
- **: !P or !{...}** finds all those documents that aren't found by P (or {...})
- Patterns can be negated indirectly. For example,

**!(!P | Q) is the same as P & !Q**

- Comparisons (including =, < , ...), even combined with AND/OR, always work over a single value, whether negated or not (directly or indirectly).
- Data type specifiers (TEXT, INT, ...) explicitly set how patterns should be compared.
- TEXT and the other data types have the same priority as NOT. For example, in condition INT A B, INT operates only on A. To extend the scope of INT, INT(A & B) should be used.
- The common data type of a multi-variable field is detected implicitly:

If texts are mixed with non-texts, then the data type is TEXT.

If dates are mixed with non-dates, then it is TEXT.

If integers are mixed with floats, then it is FLOAT.

[- Back to top -](#top)

##### C. Variables (@) and configurations (@@)

- @ introduces a variable, e.g., @Comment, @"Document number". Quotation/escaping is needed in case of spaces or special characters. Case is not detected.
- @ can also be used with a numeric constant representing a variable ID.
- @ can also be a binder that binds a certain variable to a syntax expression that follows. For example,

**@Author!=Pete**

- A binding can be multi-variable (like @(...)) with several variables inside that are delimited by OR (|). For example,

**@(Author | Creator) != Pete**

- "" or 0 represents a multiple "variable" that includes all common variables in the database. It corresponds to <Any Variable> in tab Variables.
- _Name is a special "variable" which corresponds to the file/folder name criterion.
- A binding has the same priority as NOT, !, TEXT, DATE, etc. For example,

In **@Version P Q**, Version must contain P, and Q must be found in another variable specified in the attached variable list.

In **@Variable1 (@Variable2 P & Q),** P must be found in Variable2 and Q must be found in Variable1.

- **@Var1 @Var2 P** results in a syntax error. To set multiple variables, use **@(Var1|Var2) P**.
- Parentheses can change the binding's operation, e.g., **@Version(P Q)** means Version must contain both P and Q.

- Bindings are directly applied to positive patterns in a distributive fashion (either simple (P), or complex { ... }). For example,

**@Number(!P &{ Q | R })** is the same as **!@Number(P) & @Number{Q | R}**

- @ is not allowed inside encapsulation braces { ... }.

- In addition to | , variables can be combined with AND (&), NOT (!), and parentheses. For example,

**@("" & !Comment) P** means at least one of the database variables, but not Comment, contains P.

- @@ introduces configurations in the same way that @ introduces variables. For example,

**@@"@" P** means search only the default configuration ("@") to find P.

- "" or 0 represents a multiple "configuration" which includes all configurations from the database.
- Default configuration is "@".
- Configuration 1 has a predefined name " " (a single space), no matter what its name is in the database.
- @() and @@() represent the initial setting of variables / configurations.
- @() means no variables (as initially in tab Variables).
- @@() means the same as @@"" or @@0. By default all configurations are searched.

[- Back to top -](#top)

##### D. Colon-attached (:) specifiers and variables

- Some keywords and operators at the beginning of (sub)-formula can have a colon attached, e.g., AND:, OR:, NOT:, &:, |:, !:, TEXT:, INT:, FLOAT:, DATE:. Such specifiers have the lowest priority and are processed after (), {}, NOT, AND, OR. For example,

**TEXT: a | b** is the same as **TEXT(a | b)**

**(TEXT: a) & (INT: 1)** is the same as **TEXT a INT 1**

**NOT: a b** is the same as **NOT(a b)**

- OR: implicitly sets spaces as ORs inside a given (sub-)formula.
- AND: implicitly sets spaces as ANDs inside a given (sub-)formula.
- You can use a colon in place of @ for variable binding. Instead of **@(Author|Comment|_Name|52) (john|smith)** you can use **Author:Comment:_Name:52: john|smith**.
- You can use two colons in place of @@ for configuration binding. For example, **"@":: 1:: 3:: john|smith.**

##### E. The advanced and multi-value specifiers (@: and :)

- The basic search syntax can be restrictive (i.e., no variable/configuration binding, no syntax error reporting, no explicit variable/config names/ids in conditions).
- @: placed at the beginning of a condition permits:

  - Variable/configuration binding, including the colon-attached format. For example, **@:Comment:city** finds documents where Comment contains city.
  - Multi-value search logic in which conditions target multiple variables/configurations. Braces are needed to specify single-value complex patterns.
  - Syntax error reporting.
  - Using _Name to represent a file/folder name.
  - Using virtual variables, including "" and 0 which represent all variables or configurations.
- : (colon) placed at the beginning of a condition permits:

  - Multi-value search logic in which conditions target multiple variables/configurations. Braces are needed to specify local single-value complex patterns within the multi-value condition.

[- Back to top -](#top)

###### Basic Syntax - Details

##### Syntax expressions

Syntax expressions and patterns are the new search values. The former search value **Metal** is exactly the same as the new corresponding pattern **Metal**. Syntax expressions include conditions with logical operators AND/OR/NOT or their shortcuts & | !. For example, **Ferrous & Metal** means a document should contain both substrings, **Metal** and **Ferrous**.

Single-value search logic is the default search logic. In single-value search logic conditions target single variables/configurations. Documents that contain a variable/configuration which satisfies the single-value complex pattern are found. Any condition that is passed as a second argument to [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html) or [IEdmSearch9::AddMultiVariableCondition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~AddMultiVariableCondition.html) is also implicitly enclosed in {} and is processed as a single-value complex pattern. (For multi-value search logic, see the **Advanced Syntax - Details** section.)

The logical AND can be applied implicitly by omitting AND (&). For example, **Ferrous Metal**. However, the old search value, **Ferrous Metal**, meant an exact phrase to be searched inside a variable value. According to the new rules, you should apply quotation marks to set the exact phrase, **"Ferrous Metal"**. The quotation marks are auxiliary here - they don't belong to the searched text itself. This is similar to Google Search where **Metal** and **Ferrous** can be found in different places of the document, in any order, in any number of instances, and so on. If we want to search for the phrase **Ferrous Metal** in Google Search**,** then we must quote it. The same is now true with SOLIDWORKS PDM Pro 2020.

If a quotation mark itself belongs to the searched text, then it has to be preceded by an auxiliary backslash. For example, **\"**. Each searched backslash has to be also preceded by another backslash - the first is an auxiliary one, the second is an actual character. In fact, any character can be escaped in that way. Special characters like &, | and others cannot be searched directly: A&B means "A" AND "B" but not "A&B". So they should be either quoted or escaped, or both, if searched, e.g. **"A&B"** or **A\&B** or **"A\&B"**.

You can avoid using quotes in favor of escaping. For example, **Ferrous\ Metal** (the space is escaped). On the contrary, you can always use auxiliary quotes, even if they are not really needed. For example, **"Metal".**

When quoting, the searched text should be between the beginning and the ending quote, so "" means an empty string. Quoted and unquoted pieces cannot be attached to each other. For example, **"("abc")"** is incorrect.

[- Back to top -](#top)

##### Patterns (Variable, Search, and Complex types)

A pattern is any quoted or unquoted searched (as a whole unit) text. For example, **Ferrous Metal** contains two patterns, and **"Ferrous Metal"** is a single one.

A pattern is a syntax expression that represents a searched value or a variable/configuration name or ID. Though we sometimes say "Document number" is a variable name, that is not correct. The variable name is actually **Document number**. It is quoted, "Document number", to represent the variable name. We can represent the variable name in different ways, e.g. Document\ number.

Simple names (or searched values) can be identical to their representations: **Author**, **Comment**, etc. However, even simple names can be represented by different patterns: **Author**, **"Author"**, **\Author**, **Au\thor**, **"\Author"** represent the same name, **Author**. **Document number** cannot be identical to its representation because of the space inside its name.

When talking about variables and configurations, numeric constants are database IDs. If a variable name in the database is identical to a numeric constant (i.e., constituted of digits), then you should use quotation marks or backslashes in its representation to differentiate it from numeric constants, i.e., **"51"**, **\82**. If a name in the database begins with _, it must also to be represented using " or \ because initial-underscored names are reserved for syntax usage.

Patterns may require another set of quotes as are required in C# or VB applications to escape their own reserved characters.

Spaces can be used or not between patterns and comparison/logical signs and parentheses to improve readability.

Without a comparison sign, any pattern is interpreted in the context of "Contains". In such cases, * and ? (if not escaped) work as wildcards "any number of characters" and "a single arbitrary character", e.g. "(*)" means a variable value should begin with "(" and end with ")". If no explicit non-escaped wildcards, they are meant implicitly. For example, **Metal** is equivalent to ***Metal*** (if no comparison sign, of course). Due to the explicit wildcard, "(*)" represents the whole variable value, not a substring inside it.

When talking about searched values (i.e. not about variable/configuration names), patterns can include wildcards, but only in the context of Contains, i.e. without =, <, >, etc. A pattern with wildcards represents a multitude of values. Again different patterns with wildcards can be equivalent to one other, even without " and \. For example, **a*z** represents the same set of values as **a**z**. Of course, \ and " give other equivalent representations: **"a**z"**, **\a*z**, **"a*\z",** etc. Note, you cannot use \ before wildcards if they are expected to work as wildcards. For example, **a\*z** represents exactly one word of three characters: a, *, and z. A backslash (\) before * and ? makes them common characters, no matter in what context. \ is not required before * and ? in variable/configuration names or with =, <, >, etc.

A complex pattern is any expression of the kind of {...}. Variables and configurations cannot be represented by complex patterns, and comparison operators cannot stand before them. Complex patterns are always considered in the context of Contains. For example,

**{a* & *z}** is interpreted as **"Contains a value that satisfies the condition inside {...}"**

It's clear that a complex pattern **{a* & *z}** and a simple one **a*z** can both represent the same set of searched values.

It's easy to find examples where a pattern is equivalent to a non-pattern: **Ferrous** is equivalent to **(Ferrous)** and to **{Ferrous}**, and to **(Ferrous & Ferrous)**, and to **!!Ferrous**.

Positive patterns only work over existing document values. If a document contains a value that satisfies the given pattern, then the document is found. Any encapsulated complex sub-condition {...} is also a positive pattern. **{!P}**, being a positive complex pattern, only works on existing values. If one value/configuration of the document contains P but another one does not, the document is found. If a pattern is in the scope of a single variable and a single configuration, then **{!P} AND P** cannot be satisfied. If several variable/configurations are inolved, **:{!P} & P** may find some documents.

Negative patterns are patterns that are under negation. For example, **!Metal**. Negation can be indirect. For example, **!(A !B)** means that A is negated and B is not negated. Negative patterns find all those documents that are not found by corresponding positive patterns.

For example,

: **!P** yields every document that doesn't contain P in any of its variables/configurations. It may find documents that don't have any values at all, because emptiness also does not contain P.

**{!P}**, being a positive complex pattern, only works on existing values.

**!{!P}** returns all documents where each existing value contains P, including those documents without values.

**P & !P** returns no documents.

: **P | !P** returns all documents.

[- Back to top -](#top)

##### Encapsulated expressions and complex patterns

A complex pattern is any expression of the kind of {...}. Variables and configurations cannot be represented by complex patterns, and comparison operators cannot appear before them. Complex patterns are always considered in the context of Contains. For example,

**{a* & *z}** is interpreted as **"Contains a value that satisfies the condition inside {...}"**

It's clear that a complex pattern **{a* & *z}** and a simple pattern **(a*z)** can both represent the same set of searched values.

Braces ({}) show that the whole sub-formula inside them should be searched for within a single variable value (for a given combination of variable and configuration). **{Metal Ferrous}** means that both substrings **Metal** and Ferrous **should** belong to the same variable value in the same configuration (in any order, in any places, and in any number of instances). Without braces, **Ferrous** can be found in one variable (or configuration) and **Metal** in a different variable (of the same document, of course).

Encapsulated expressions {...} can be considered complex patterns. You can write **a*b** or **{a* & *b}.** Both mean the same and both are checked inside the same single value.

**{!=100}** only finds a document that has a certain value not equal to 100, though some other value can be equal to 100. **<>100** works the same as **{!=100}**. **!{=100}** or just **!=100** only finds those documents that don't have any values equal to 100 (multi-value context).

Basic search syntax employs single-value search logic that implicitly encapsulates conditions in braces. You can use braces, but they do not change the underlying logic.

Advanced search syntax employs multi-value search logic that does not implicitly encapsulate conditions in braces. You must use braces to specify complex patterns. (See the **Advanced Syntax- Details** section.)

[- Back to top -](#top)

##### Patterns and comparisons

A comparison is a combination of a sign like =, <, >= etc. and a pattern like **=Ferrous**.

Patterns and comparisons are simple operands (i.e. terms) that can be combined with AND, OR, NOT. To set the logical order, use parentheses: (sldptr | txt) & attachment. Without parentheses, NOT has the highest priority and OR has the lowest.

Spaces can be used or not between patterns and comparison/logical signs and parentheses to improve readability.

Without a comparison sign, any pattern is interpreted in the context of "Contains". In that case, * and ? (if not escaped) work as wildcards (* = "any number of characters" and ? = "a single arbitrary character"). For example, "(*)" means a variable value should begin with "(" and end with ")". If no explicit non-escaped wildcards, they are meant implicitly. For example, **Metal** is equivalent to ***Metal*** (if no comparison sign, of course). Due to the explicit wildcard, **"(*)"** represents the whole variable value, not a substring inside it.

[- Back to top -](#top)

##### Explicit/implicit data types

Expressions are processed under a certain data type that has been inherited from the field variable. You can explicitly set a different data type. For example, in **DATE >="Jan 15, 2005"** , "Jan 15, 2005" will be considered a date type, not a string type. In the DATE context, patterns will be compared as texts if they don't represent correct dates. A correct date representation can be quoted or have escaped characters.

Each of data type specifiers (TEXT, INT, FLOAT, DATE) has the same priority as NOT.

In the TEXT context, all patterns are considered as string values.

In the INT or FLOAT context, each pattern which represents a correct numeric constant is compared as a number, otherwise as text. E.g. **"123"** and **\123** aren't correct constants, so they will be compared as string values.

In the case of multi-variable search syntax, the common implicit field data type is automatically detected from variables. For example, if dates are mixed with non-dates (or texts mixed with non-texts), then the date type will be TEXT; when INT is mixed with FLOAT, then the date type will be FLOAT. Booleans are considered as INTs (0 or 1). Automatic types are only used if there are no explicit type specifiers.

Colons can be used to change the priority of NOT and specifiers, e.g. **INT: >=1 <=10** sets the integer type for the whole expression. Without the colon, INT would have operated only on **>=1**.

Such "colon-attached" specifiers as AND: and OR: (&: |:) set spaces as the implicit AND or the implicit OR. For example,

**OR: a b c (&: d e f)** is equivalent to **a | B | c | d & e & f**.

By default AND is the implicit operator.

The full list of "colon-attached" specifiers (no space before the colon):

**TEXT: INT: FLOAT: DATE: AND: OR: NOT: &: |: !:**

Data type specifiers and bindings are applied directly to positive patterns inside the linked expression. A data type specifier or binding just sets the scope. Units which a type/binding act on are only positive patterns. For example,

**TEXT ( !1 & (200 | 300) ) is actually processed as ! TEXT 1 & (TEXT 200 | TEXT 300)**

It would be similar if there had been a single-variable or multi-variable binding in place of TEXT.

Data types operate the same between () and {}, so you can write {INT 1 & TEXT a}. However, for bindings each {...} is considered a large atomic positive pattern.

[- Back to top -](#top)

##### Colon-attached specifiers and variables

Consider **INT( >=1 <=10 )**. The parentheses are required because INT has the same priority as NOT. Without them, INT would only affect **>=1**, the whole expression being equivalent to **INT( >=1 ) <=10**.

INT: has the lowest priority. It is processed after NOT, AND and OR. Thus, **INT: >=1 <=10** is the same as **INT: (>=1 <=10)**. Owing to the colon, you can omit parentheses, making the expression simpler.

All the colon-attached specifiers have the same lowest priority. They are especially convenient when you apply them to the whole condition. However, when applying to simple operands (e.g. to terms containing patterns and comparisons), colon-attached specifiers may be unnecessary. For example,

**(INT: 100) | (TEXT: abc)** is equivalent to a much simpler **INT 100 | TEXT abc**

Because of their lowest priority and for the sake of avoiding ambiguities, all the colon-attached specifiers have to be used one by one on the left of the subsequent expression. They are placed at the very beginning of the whole condition or between "(" and the expression. The scope of such specifiers extend to the end of the condition or up to the corresponding ")". For example,

**Comment: 1:: "Document number": 2:: 123 & abc**

has four specifiers followed by the syntax expression, **123 & abc**. In the case of several colon-attached variables before the same syntax expression, all variables are implicitly grouped in a single binding with | between variable names. All the colon-attached configurations are similarly grouped in their own binding. The order of names/IDs/variables/configurations is not important.

[- Back to top -](#top)

###### Advanced Syntax - Details

##### Advanced specifiers (@:)

Single-value search logic is the default search logic (see the **Basic Syntax - Details** section.) In some cases, multi-value search logic is needed. In multi-value search logic, conditions target multiple variables/configurations. To turn on multi-value search logic, you must use either the multi-value specifier, **:**, or the advanced specifier, **@:**. Advanced specifiers allow you to use variable/configuration names/identifiers inside conditions. They also turn on syntax checking and reporting. To turn on multi-value search logic and syntax checking, a condition must begin with @:. Because @ has a special meaning, it should be quoted or escaped if it is being searched for in patterns. The advanced specifier forces you to write safer and less ambiguous expressions. It forbids risky syntax elements such as inch (") constants. For example, it requires you to use **4\"** instead of **4"**. With the advanced specifier, you must use {} to specify local single-value complex patterns within multi-value conditions (see [Encapsulated expressions and complex patterns](#Encapsulated)).

##### Multi-value specifiers (:)

The multi-value specifier (:) is a light version of the advanced specifier (@:). Like @:, the multi-value specifier (:) placed before a condition turns on multi-value search logic and indicates that you must use {} to specify local single-value complex patterns within multi-value condition. Unlike @:, the multi-value specifier (:) does not allow explicit variables/configurations and does not support syntax error messaging. For example,

**A B** is equivalent to **:{A B}**

**: {=5 =10}** returns no documents

If you want a document with 5 in one variable/configuration and 10 in another variable/configuration, use:

**: =5 =10**

To check whether a value is in a range, curly braces should be applied:

**:{>=1 <=10}**

Braces are not necessary for ranges if there is no multi-value specifier:

**>=1 <=10**

##### Variable and configuration bindings

@ is called "variable binder", because it binds a variable to a pattern or representation. It indicates that the subsequent pattern represents a variable name or identifier (if a numeric constant). For example, **@Comment**, **@"Document number"**. A combination of a variable binder and a pattern is a binding. The binding has the same priority as DATE or NOT. The binding acts on the subsequent operand, i.e., it indicates that it needs to be compared with the given variable, e.g. **@Number=100**, **@Author Johns.**

A binding can contain multiple variables. For example, **@(Comment | "Document number") 123** which is equivalent to **@Comment 123 | @"Document number" 123**. We can also use the other logical operators inside a binding. For example, **@(V & !U) P** is the same as **@V(P) & !@U(P)**. Multi-variable bindings provide better performance when compared to equivalent expressions where all bindings are single-variable ones.

If a variable name begins with an underscore, then it should be quoted/escaped, e.g. **@"_SpecialVar"**. Initial-underscore names are reserved for future syntax extensions. Currently only _Name has a special meaning in the syntax. _Name is a virtual variable indicating the file/folder name of a searched document/project. _Name can be used in any place where common variable names are used. _Name and _name are equivalent.

An empty string "" or numeric constant 0 represents one or more "virtual" variables. It can be used to specify the whole set of the database variables. **@""** is like **@(var1 | var2 | ... | varN)** which enumerates all of the common variable names. **@("" | _Name)** includes file/folder names in that enumeration.

A configuration binder @@ is similar to @ but deals with names and IDs of configurations. Again, **@@0** or **@""** searches over all configurations (and is assumed implicitly). Configuration 1 is present in projects and non-SOLIDWORKS documents and has a predefined name " ", i.e. a single space. Configuration 2 (commonly named "@") represents the default configuration.

@() and @@() set the initial (default) binding state: @() indicates that no variables are defined, so they should be explicitly present in the subsequent sub-formula. @@() is the same as @@0 and indicates that all configurations are searched.

You can think of data type specifiers and bindings as applied directly to positive patterns inside linked expressions. A data type specifier or binding just sets the scope. Units that a type/binding acts on are positive patterns.

**@(var1|var2) (>=100 !150 <=200)** is equivalent to **@(var1|var2) {>=100 <=200} & !@(var1|var2) 150**.

##### Colon-attached bindings

Bindings can be set in the "colon-attached" format. For example,

**Comment: 1:: "Document number": 2:: 123 & abc** is the same as **@(Comment | "Document number") @@(1|2) (123 & abc)**

Configuration bindings use colons to differentiate them from variable bindings.

@ and @@ are not applied at all if colons are used.

[- Back to top -](#top)
