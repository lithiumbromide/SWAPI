---
title: "CriteriaCount Property (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "CriteriaCount"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~CriteriaCount.html"
---

# CriteriaCount Property (IPDMWSearchCriteria)

Gets the number of search criteria.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CriteriaCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim value As System.Integer

value = instance.CriteriaCount
```

### C#

```csharp
System.int CriteriaCount {get;}
```

### C++/CLI

```cpp
property System.int CriteriaCount {
   System.int get();
}
```

### Property Value

Number of search criteria

## VBA Syntax

See [PDMWSearchCriteria::CriteriaCount](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~CriteriaCount.html).

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::GetCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~GetCriteria.html)
[IPDMWSearchCriteria::RemoveCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~RemoveCriteria.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
