---
title: "SearchConfigSpecificProperties Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "SearchConfigSpecificProperties"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~SearchConfigSpecificProperties.html"
---

# SearchConfigSpecificProperties Property (IPDMWSearchOptions)

Gets or sets whether to search configuration-specific properties during a search.

## Syntax

### Visual Basic (Declaration)

```vb
Property SearchConfigSpecificProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As System.Boolean

instance.SearchConfigSpecificProperties = value

value = instance.SearchConfigSpecificProperties
```

### C#

```csharp
System.bool SearchConfigSpecificProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool SearchConfigSpecificProperties {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to search configuration-specific properties, false to not

## VBA Syntax

See [PDMWSearchOptions::SearchConfigSpecificProperties](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~SearchConfigSpecificProperties.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## Remarks

By default, configuration-specific properties are not searched.

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)
[PDMWSearchResult::ConfigurationName Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~ConfigurationName.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
