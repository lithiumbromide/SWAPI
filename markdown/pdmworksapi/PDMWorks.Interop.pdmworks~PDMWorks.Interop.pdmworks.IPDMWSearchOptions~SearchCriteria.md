---
title: "SearchCriteria Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "SearchCriteria"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~SearchCriteria.html"
---

# SearchCriteria Property (IPDMWSearchOptions)

Gets the search criteria.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SearchCriteria As PDMWSearchCriteria
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As PDMWSearchCriteria

value = instance.SearchCriteria
```

### C#

```csharp
PDMWSearchCriteria SearchCriteria {get;}
```

### C++/CLI

```cpp
property PDMWSearchCriteria^ SearchCriteria {
   PDMWSearchCriteria^ get();
}
```

### Property Value

[IPDMWSearchCriteria](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)

## VBA Syntax

See [PDMWSearchOptions::SearchCriteria](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~SearchCriteria.html).

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
