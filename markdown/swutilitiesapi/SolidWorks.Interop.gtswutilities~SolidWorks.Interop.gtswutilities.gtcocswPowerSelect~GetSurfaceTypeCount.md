---
title: "GetSurfaceTypeCount Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetSurfaceTypeCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetSurfaceTypeCount.html"
---

# GetSurfaceTypeCount Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
