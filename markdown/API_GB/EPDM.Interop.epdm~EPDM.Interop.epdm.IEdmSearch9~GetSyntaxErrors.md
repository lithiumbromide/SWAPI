---
title: "GetSyntaxErrors Method (IEdmSearch9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch9"
member: "GetSyntaxErrors"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~GetSyntaxErrors.html"
---

# GetSyntaxErrors Method (IEdmSearch9)

Gets syntax errors resulting from this search.

## Syntax

### Visual Basic

```vb
Function GetSyntaxErrors() As System.String()
```

### C#

```csharp
System.string[] GetSyntaxErrors()
```

### C++/CLI

```cpp
System.array<String^>^ GetSyntaxErrors();
```

### Return Value

Array of localized syntax errors; Nothing or null if no errors

## Examples

See the [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Remarks

This method returns errors only if the advanced specifier (@:) is specified at the beginning of search syntax conditions.

If [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) returns Nothing or null it can mean either:

- the search found no documents

- or -

- there were one or more search syntax errrors.

Call this method after IEdmSearch5::GetFirstResult to determine whether there are syntax errors. If this method returns Nothing or null, then you can assume that IEdmSearch5::GetFirstResult found no documents.

See [Search Syntax](SearchSyntax-epdmapi.html).

## See Also

[IEdmSearch9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html)
[IEdmSearch9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9_members.html)

## Availability

SOLIDWORKS PDM Professional 2020
