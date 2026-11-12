---
title: "GetAppliedFilters Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetAppliedFilters"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFilters.html"
---

# GetAppliedFilters Method (IPowerSelect)

Gets a list of the filters applied in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedFilters( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetAppliedFilters(lErrorcode)
```

### C#

```csharp
System.object GetAppliedFilters(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetAppliedFilters(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the applied filters as defined in [gtpslFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFilterType_e.html)

## VBA Syntax

See [IPowerSelect::GetAppliedFilters](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetAppliedFilters.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetAppliedFiltersCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFiltersCount.html)
[IPowerSelect::IGetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetAppliedFilters.html)
[IPowerSelect::RemoveFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RemoveFilters.html)
[IPowerSelect::GetEdgeAngleFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetEdgeAngleFilter.html)
[IPowerSelect::GetEdgeConvexityFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetEdgeConvexityFilter.html)
[IPowerSelect::GetFaceColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFaceColorFilter.html)
[IPowerSelect::GetFeatureColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureColorFilter.html)
[IPowerSelect::GetFeatureNameFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureNameFilter.html)
[IPowerSelect::GetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilter.html)
[IPowerSelect::GetFeatureTypeFilterCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilterCount.html)
[IPowerSelect::GetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeFilter.html)
[IPowerSelect::IGetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetFeatureTypeFilter.html)
[IPowerSelect::IGetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetSurfaceTypeFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
