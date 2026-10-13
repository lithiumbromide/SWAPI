---
title: "GetIntersectFeature Method (IDimXpertIntersectCircleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectCircleFeature"
member: "GetIntersectFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature~GetIntersectFeature.html"
---

# GetIntersectFeature Method (IDimXpertIntersectCircleFeature)

Gets the DimXpert feature that intersects this DimXpert intersect circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectFeature( _
   ByRef Feature As DimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertIntersectCircleFeature
Dim Feature As DimXpertFeature
Dim value As System.Boolean

value = instance.GetIntersectFeature(Feature)
```

### C#

```csharp
System.bool GetIntersectFeature(
   out DimXpertFeature Feature
)
```

### C++/CLI

```cpp
System.bool GetIntersectFeature(
   [Out] DimXpertFeature^ Feature
)
```

### Parameters

- `Feature`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

### Return Value

True if the method call is successful; false otherwise

## See Also

[IDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature.html)
[IDimXpertIntersectCircleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
