---
title: "ISetSurfaceTypeFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "ISetSurfaceTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetSurfaceTypeFilter.html"
---

# ISetSurfaceTypeFilter Method (IPowerSelect)

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
Dim instance As IPowerSelect
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

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::SetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetSurfaceTypeFilter.html)
[IPowerSelect::IGetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetSurfaceTypeFilter.html)
[IPowerSelect::GetSurfaceTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeFilter.html)
[IPowerSelect::GetSurfaceTypeCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSurfaceTypeCount.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
