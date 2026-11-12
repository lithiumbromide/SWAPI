---
title: "GetSurfaceTypeFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeFilter.html"
---

# GetSurfaceTypeFilter Method (IPowerSelect)

Gets a list of the selected surface types, such as planes, cylinders, cones, etc., in the surface type filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSurfaceTypeFilter( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetSurfaceTypeFilter(lErrorcode)
```

### C#

```csharp
System.object GetSurfaceTypeFilter(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetSurfaceTypeFilter(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the selected surface types in surface type filter

## VBA Syntax

See [IPowerSelect::GetSurfaceTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetSurfaceTypeFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetSurfaceTypeCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeCount.html)
[IPowerSelect::IGetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetSurfaceTypeFilter.html)
[IPowerSelect::ISetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetSurfaceTypeFilter.html)
[IPowerSelect::SetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetSurfaceTypeFilter.html)
