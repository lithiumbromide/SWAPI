---
title: "GetPlaneFeature Method (IDimXpertIntersectCircleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectCircleFeature"
member: "GetPlaneFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature~GetPlaneFeature.html"
---

# GetPlaneFeature Method (IDimXpertIntersectCircleFeature)

Gets the DimXpert plane feature used to dimension this DimXpert intersect circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlaneFeature( _
   ByRef Plane As DimXpertPlaneFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertIntersectCircleFeature
Dim Plane As DimXpertPlaneFeature
Dim value As System.Boolean

value = instance.GetPlaneFeature(Plane)
```

### C#

```csharp
System.bool GetPlaneFeature(
   out DimXpertPlaneFeature Plane
)
```

### C++/CLI

```cpp
System.bool GetPlaneFeature(
   [Out] DimXpertPlaneFeature^ Plane
)
```

### Parameters

- `Plane`: [IDimXpertPlaneFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectCircleFeature::GetPlaneFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectCircleFeature~GetPlaneFeature.html).

## See Also

[IDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature.html)
[IDimXpertIntersectCircleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
