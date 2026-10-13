---
title: "IEdmSearch9 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch9"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html"
---

# IEdmSearch9 Interface

Allows you to quickly find files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmSearch9
   Inherits IEdmSearch5, IEdmSearch6, IEdmSearch7, IEdmSearch8
```

### C#

```csharp
public interface IEdmSearch9 : IEdmSearch5, IEdmSearch6, IEdmSearch7, IEdmSearch8
```

### C++/CLI

```cpp
public interface class IEdmSearch9 : public IEdmSearch5, IEdmSearch6, IEdmSearch7, IEdmSearch8
```

## Examples

[Using Basic Search Syntax (VB.NET)](Using_Basic_Search_Syntax_Example_VBNET.htm)
[Using Basic Search Syntax (C#)](Using_Basic_Search_Syntax_Example_CSharp.htm)

## Remarks

This interface:

- Extends [IEdmSearch8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html) by providing the ability to peform a search for files and folders using logical operators, multi-variable conditions, and new search syntax. See [Search Syntax](SearchSyntax-epdmapi.html).

- Is extended by [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html).

In extended searches:

- All IEdmSearch* properties and method parameters support the new search syntax.
- [IEdmSearch9::AddMultiVariableCondition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~AddMultiVariableCondition.html) can be used to specify new search syntax for two or more file or folder data card variables.
- If [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) returns Nothing or null, it means that either:

  - no documents were found

- or -

- there was a syntax error in one of the search syntax expressions.

After calling IEdmSearch5::GetFirstResult, you must call [IEdmSearch9::GetSyntaxErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~GetSyntaxErrors.html) to see if there are any syntax errors. If not, then you can deduce that no documents were found.

## Accessors

[IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html)

## See Also

[IEdmSearch9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
