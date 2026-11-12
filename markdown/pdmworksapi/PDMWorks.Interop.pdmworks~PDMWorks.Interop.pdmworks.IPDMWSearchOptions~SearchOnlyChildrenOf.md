---
title: "SearchOnlyChildrenOf Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "SearchOnlyChildrenOf"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~SearchOnlyChildrenOf.html"
---

# SearchOnlyChildrenOf Property (IPDMWSearchOptions)

Gets or sets whether to limit the scope of the search by specifying a project or parent document.

## Syntax

### Visual Basic (Declaration)

```vb
Property SearchOnlyChildrenOf As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As System.String

instance.SearchOnlyChildrenOf = value

value = instance.SearchOnlyChildrenOf
```

### C#

```csharp
System.string SearchOnlyChildrenOf {get; set;}
```

### C++/CLI

```cpp
property System.String^ SearchOnlyChildrenOf {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path and filename of the project or parent document whose children to search or an empty string to search the entire va

## VBA Syntax

See [PDMWSearchOptions::SearchOnlyChildrenOf](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~SearchOnlyChildrenOf.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
