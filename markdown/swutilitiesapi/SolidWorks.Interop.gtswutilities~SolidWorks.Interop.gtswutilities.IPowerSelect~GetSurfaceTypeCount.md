---
title: "GetSurfaceTypeCount Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetSurfaceTypeCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeCount.html"
---

# GetSurfaceTypeCount Method (IPowerSelect)

Gets the number of surface types, such as planes, cylinders, cones, etc., selected in the surface type filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSurfaceTypeCount( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetSurfaceTypeCount(lErrorcode)
```

### C#

```csharp
System.int GetSurfaceTypeCount(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetSurfaceTypeCount(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of surface types selected in surface type filter

## VBA Syntax

See [IPowerSelect::GetSurfaceTypeCount](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetSurfaceTypeCount.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeFilter.html)
[IPowerSelect::IGetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetSurfaceTypeFilter.html)
[IPowerSelect::ISetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetSurfaceTypeFilter.html)
[IPowerSelect::SetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetSurfaceTypeFilter.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
