---
title: "ConfigurationName Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "ConfigurationName"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~ConfigurationName.html"
---

# ConfigurationName Property (IPDMWSearchResult)

Gets the name of the configuration in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
}
```

### Property Value

Name of configuration

## VBA Syntax

See [PDMWSearchResult::ConfigurationName](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~ConfigurationName.html).

## Remarks

[IPDMWSearchOptions::SearchConfigSpecificProperties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~SearchConfigSpecificProperties.html) must be true to use this property.

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)
[IPDMWSearchOptions::SearchConfigSpecificProperties Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~SearchConfigSpecificProperties.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
