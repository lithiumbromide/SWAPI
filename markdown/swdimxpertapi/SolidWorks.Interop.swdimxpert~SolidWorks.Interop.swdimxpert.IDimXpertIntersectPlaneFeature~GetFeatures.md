---
title: "GetFeatures Method (IDimXpertIntersectPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectPlaneFeature"
member: "GetFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature~GetFeatures.html"
---

# GetFeatures Method (IDimXpertIntersectPlaneFeature)

Gets the DimXpert features that intersect on this DimXpert intersect plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatures( _
   ByRef Feature1 As DimXpertFeature, _
   ByRef Feature2 As DimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertIntersectPlaneFeature
Dim Feature1 As DimXpertFeature
Dim Feature2 As DimXpertFeature
Dim value As System.Boolean

value = instance.GetFeatures(Feature1, Feature2)
```

### C#

```csharp
System.bool GetFeatures(
   out DimXpertFeature Feature1,
   out DimXpertFeature Feature2
)
```

### C++/CLI

```cpp
System.bool GetFeatures(
   [Out] DimXpertFeature^ Feature1,
   [Out] DimXpertFeature^ Feature2
)
```

### Parameters

- `Feature1`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)
- `Feature2`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectPlaneFeature::GetFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectPlaneFeature~GetFeatures.html).

## Examples

[Get DimXpert Intersect Features Example (VBA)](Get_DimXpert_Intersect_Features_Example_VB.htm)
[Get DimXpert Intersect Features Example (VB.NET)](Get_DimXpert_Intersect_Features_Example_VBNET.htm)

## See Also

[IDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature.html)
[IDimXpertIntersectPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
