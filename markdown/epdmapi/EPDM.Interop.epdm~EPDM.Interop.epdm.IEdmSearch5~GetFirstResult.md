---
title: "GetFirstResult Method (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "GetFirstResult"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html"
---

# GetFirstResult Method (IEdmSearch5)

Gets the first file or folder that matches the search criteria.

## Syntax

### Visual Basic

```vb
Function GetFirstResult() As IEdmSearchResult5
```

### C#

```csharp
IEdmSearchResult5 GetFirstResult()
```

### C++/CLI

```cpp
IEdmSearchResult5^ GetFirstResult();
```

### Return Value

[IEdmSearchResult5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html); Nothing or null if no files or folders match the search criteria or there are syntax errors in search conditions (see Remarks)

## Examples

See the [IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html) and [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Remarks

If the search object was obtained using [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html) (IEdmSearch9) then this method's return of Nothing or null can mean either:

- the search found no documents,

- or -

- there are one or more search condition syntax errrors. Call [IEdmSearch9::GetSyntaxErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~GetSyntaxErrors.html) to determine whether there are syntax errors. If IEdmSearch9::GetSyntaxErrors returns Nothing or null, then you can assume that this method returned Nothing or null because the search found no documents. See [Search Syntax](SearchSyntax-epdmapi.html).

After calling this method, call [IEdmSearch5::GetNextResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetNextResult.html) to retrieve the rest of the files and folders that match the search criteria.

C++ users must release the returned interface, IEdmSearchResult5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The method successfully executed, but no files or folders match the search criteria.

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
