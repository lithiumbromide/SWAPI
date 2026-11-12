---
title: "CreateSearch2 Method (IEdmVault21)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault21"
member: "CreateSearch2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html"
---

# CreateSearch2 Method (IEdmVault21)

Creates an interface to a search object.

## Syntax

### Visual Basic

```vb
Function CreateSearch2() As IEdmSearch5
```

### C#

```csharp
IEdmSearch5 CreateSearch2()
```

### C++/CLI

```cpp
IEdmSearch5^ CreateSearch2();
```

### Return Value

[IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)

## Examples

See the [IEdmVault21](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21.html) examples.

## Remarks

This method creates a search object that allows you to search files and folders using multi-variable conditions, logical operators, and special search syntax. Once this search object is instantiated, special search syntax is allowed in all IEdmSearch* properties and method parameters. (See [Search Syntax](SearchSyntax-epdmapi.html).)

To perform a search:

1. Cast the returned IEdmSearch5 to [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html).
2. Add a single variable search condition using [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html). The new search allows you to specify the poValue parameter using special search syntax and eliminates the need to specify the lEdmVarOp parameter.
3. Add a multi-variable search condition using [IEdmSearch9::AddMultiVariableCondition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~AddMultiVariableCondition.html). Special search syntax applies.
4. Use the special search syntax in [IEdmSearch5::FileName](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~FileName.html), [IEdmSearch5::VersionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~VersionComment.html), [IEdmSearch5::State](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~State.html), and [IEdmSearch6::SetToken](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.html).
5. Call [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html). If no results are returned, either nothing was found or there were search syntax errors.
6. If step 5 returns no results, then see if there are search syntax errors by calling [IEdmSearch9::GetSyntaxErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~GetSyntaxErrors.html). (Note: no syntax errors are reported unless advanced specifiers were placed before each search syntax.)
7. If step 5 returns results, call [IEdmSearch5::GetNextResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetNextResult.html) repeatedly to get further results.

C++ users must release the returned pointer, IEdmSearch5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault21 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21.html)
[IEdmVault21 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21_members.html)

## Availability

SOLIDWORKS PDM Professional 2020
