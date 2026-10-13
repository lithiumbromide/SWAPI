---
title: "GetPlaneFeatures Method (IDimXpertCompoundNotchFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundNotchFeature"
member: "GetPlaneFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetPlaneFeatures.html"
---

# GetPlaneFeatures Method (IDimXpertCompoundNotchFeature)

Gets the DimXpert plane features for both sides of this DimXpert compound notch.

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
Dim instance As IDimXpertCompoundNotchFeature
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

See [DimXpertCompoundNotchFeature::GetPlaneFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundNotchFeature~GetPlaneFeatures.html).

## See Also

[IDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature.html)
[IDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
