---
title: "SetSurfaceTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetSurfaceTypeFilter.html"
---

# SetSurfaceTypeFilter Method (gtcocswPowerSelect)

Sets the surface types, such as planes, cylinders, cones, etc., to select in the surface type filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSurfaceTypeFilter( _
   ByVal varSurfTypeArr As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim varSurfTypeArr As System.Object
Dim value As System.Integer

value = instance.SetSurfaceTypeFilter(varSurfTypeArr)
```

### C#

```csharp
System.int SetSurfaceTypeFilter(
   System.object varSurfTypeArr
)
```

### C++/CLI

```cpp
System.int SetSurfaceTypeFilter(
   System.Object^ varSurfTypeArr
)
```

### Parameters

- `varSurfTypeArr`: Array of the surface types to select in the surface type filter

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetSurfaceTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetSurfaceTypeFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
