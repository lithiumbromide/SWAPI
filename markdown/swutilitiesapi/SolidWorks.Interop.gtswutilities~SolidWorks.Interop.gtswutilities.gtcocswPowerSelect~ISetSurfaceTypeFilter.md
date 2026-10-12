---
title: "ISetSurfaceTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "ISetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~ISetSurfaceTypeFilter.html"
---

# ISetSurfaceTypeFilter Method (gtcocswPowerSelect)

Sets the surface types, such as planes, cylinders, cones, etc., to select in the surface type filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetSurfaceTypeFilter( _
   ByVal lSurfTypeCount As System.Integer, _
   ByRef pSurfTypeArr As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lSurfTypeCount As System.Integer
Dim pSurfTypeArr As System.Integer
Dim value As System.Integer

value = instance.ISetSurfaceTypeFilter(lSurfTypeCount, pSurfTypeArr)
```

### C#

```csharp
System.int ISetSurfaceTypeFilter(
   System.int lSurfTypeCount,
   ref System.int pSurfTypeArr
)
```

### C++/CLI

```cpp
System.int ISetSurfaceTypeFilter(
   System.int lSurfTypeCount,
   System.int% pSurfTypeArr
)
```

### Parameters

- `lSurfTypeCount`: Number of surface types to select
- `pSurfTypeArr`: Array of the surface types to select

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::ISetSurfaceTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~ISetSurfaceTypeFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
