---
title: "GetSearchOptionsObject Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "GetSearchOptionsObject"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~GetSearchOptionsObject.html"
---

# GetSearchOptionsObject Method (IPDMWConnection)

Gets the search options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchOptionsObject() As PDMWSearchOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As PDMWSearchOptions

value = instance.GetSearchOptionsObject()
```

### C#

```csharp
PDMWSearchOptions GetSearchOptionsObject()
```

### C++/CLI

```cpp
PDMWSearchOptions^ GetSearchOptionsObject();
```

### Return Value

[IPDMWSearchOptions](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html) object

## VBA Syntax

See [PDMWConnection::GetSearchOptionsObject](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~GetSearchOptionsObject.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
