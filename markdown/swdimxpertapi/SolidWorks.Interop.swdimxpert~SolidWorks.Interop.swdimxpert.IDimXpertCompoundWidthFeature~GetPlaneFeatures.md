---
title: "GetPlaneFeatures Method (IDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundWidthFeature"
member: "GetPlaneFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature~GetPlaneFeatures.html"
---

# GetPlaneFeatures Method (IDimXpertCompoundWidthFeature)

Gets the DimXpert plane features for both sides of this DimXpert compound width.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlaneFeatures( _
   ByRef Plane1 As DimXpertPlaneFeature, _
   ByRef Plane2 As DimXpertPlaneFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundWidthFeature
Dim Plane1 As DimXpertPlaneFeature
Dim Plane2 As DimXpertPlaneFeature
Dim value As System.Boolean

value = instance.GetPlaneFeatures(Plane1, Plane2)
```

### C#

```csharp
System.bool GetPlaneFeatures(
   out DimXpertPlaneFeature Plane1,
   out DimXpertPlaneFeature Plane2
)
```

### C++/CLI

```cpp
System.bool GetPlaneFeatures(
   [Out] DimXpertPlaneFeature^ Plane1,
   [Out] DimXpertPlaneFeature^ Plane2
)
```

### Parameters

- `Plane1`: [IDimXpertPlaneFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html)
- `Plane2`: [IDimXpertPlaneFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundWidthFeature::GetPlaneFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundWidthFeature~GetPlaneFeatures.html).

## See Also

[IDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature.html)
[IDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
