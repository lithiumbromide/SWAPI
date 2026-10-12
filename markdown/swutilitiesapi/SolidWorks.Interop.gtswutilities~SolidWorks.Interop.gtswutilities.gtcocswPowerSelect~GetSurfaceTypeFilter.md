---
title: "GetSurfaceTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetSurfaceTypeFilter.html"
---

# GetSurfaceTypeFilter Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)
