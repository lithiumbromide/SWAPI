---
title: "Search Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Search"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Search.html"
---

# Search Method (IPDMWConnection)

Searches the vault using the specified search options.

## Syntax

### Visual Basic (Declaration)

```vb
Function Search( _
   ByVal pSearchOptions As PDMWSearchOptions _
) As PDMWSearchResults
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim pSearchOptions As PDMWSearchOptions
Dim value As PDMWSearchResults

value = instance.Search(pSearchOptions)
```

### C#

```csharp
PDMWSearchResults Search(
   PDMWSearchOptions pSearchOptions
)
```

### C++/CLI

```cpp
PDMWSearchResults^ Search(
   PDMWSearchOptions^ pSearchOptions
)
```

### Parameters

- `pSearchOptions`: [IPDMWSearchOptions](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html) object

### Return Value

[IPDMWSearchResults](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResults.html) object

## VBA Syntax

See [PDMWConnection::Search](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Search.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
