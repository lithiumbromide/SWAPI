---
title: "RemoveFilters Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "RemoveFilters"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RemoveFilters.html"
---

# RemoveFilters Method (IPowerSelect)

Removes the specified filters, if they are set, in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFilters( _
   ByVal lFilterEnums As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lFilterEnums As System.Integer
Dim value As System.Integer

value = instance.RemoveFilters(lFilterEnums)
```

### C#

```csharp
System.int RemoveFilters(
   System.int lFilterEnums
)
```

### C++/CLI

```cpp
System.int RemoveFilters(
   System.int lFilterEnums
)
```

### Parameters

- `lFilterEnums`: Filters to remove as defined in [gtpslFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFilterType_e.html)

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::RemoveFilters](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~RemoveFilters.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFilters.html)
[IPowerSelect::GetAppliedFiltersCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFiltersCount.html)
[IPowerSelect::IGetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetAppliedFilters.html)
[IPowerSelect::SetEdgeAngleFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetEdgeAngleFilter.html)
[IPowerSelect::SetEdgeConvexityFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetEdgeConvexityFilter.html)
[IPowerSelect::SetFaceColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFaceColorFilter.html)
[IPowerSelect::SetFeatureColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureColorFilter.html)
[IPowerSelect::SetFeatureNameFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureNameFilter.html)
[IPowerSelect::SetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureTypeFilter.html)
[IPowerSelect::IPowerSelect::SetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetSurfaceTypeFilter.html)
[IPowerSelect::ISetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetFeatureTypeFilter.html)
[IPowerSelect::ISetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetSurfaceTypeFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
