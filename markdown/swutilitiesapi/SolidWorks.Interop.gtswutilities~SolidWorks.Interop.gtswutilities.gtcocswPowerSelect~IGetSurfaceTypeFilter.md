---
title: "IGetSurfaceTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "IGetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~IGetSurfaceTypeFilter.html"
---

# IGetSurfaceTypeFilter Method (gtcocswPowerSelect)

Gets a list of the selected surface types, such as planes, cylinders, cones, etc., in the surface type filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSurfaceTypeFilter( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.IGetSurfaceTypeFilter(lErrorcode)
```

### C#

```csharp
System.int IGetSurfaceTypeFilter(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int IGetSurfaceTypeFilter(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the selected surface types in surface type filter

## VBA Syntax

See [IPowerSelect::IGetSurfaceTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~IGetSurfaceTypeFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
