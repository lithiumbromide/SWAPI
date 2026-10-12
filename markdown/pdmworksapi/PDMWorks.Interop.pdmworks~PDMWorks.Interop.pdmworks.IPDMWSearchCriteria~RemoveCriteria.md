---
title: "RemoveCriteria Method (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "RemoveCriteria"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~RemoveCriteria.html"
---

# RemoveCriteria Method (IPDMWSearchCriteria)

Removes a search criteria.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveCriteria( _
   ByVal Index As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim Index As System.Integer

instance.RemoveCriteria(Index)
```

### C#

```csharp
void RemoveCriteria(
   System.int Index
)
```

### C++/CLI

```cpp
void RemoveCriteria(
   System.int Index
)
```

### Parameters

- `Index`: Index number of the search criteria to remove

## VBA Syntax

See [PDMWSearchCriteria::RemoveCriteria](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~RemoveCriteria.html).

## Remarks

To determine the index number of the search criteria to remove, use [IPDMWSearchCriteria::CriteriaCount](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~CriteriaCount.html) before using this method.

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::AddCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~AddCriteria.html)
[IPDMWSearchCriteria::GetCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~GetCriteria.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
