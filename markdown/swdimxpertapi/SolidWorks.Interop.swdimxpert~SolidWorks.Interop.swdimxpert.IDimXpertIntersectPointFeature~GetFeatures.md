---
title: "GetFeatures Method (IDimXpertIntersectPointFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectPointFeature"
member: "GetFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature~GetFeatures.html"
---

# GetFeatures Method (IDimXpertIntersectPointFeature)

Gets the DimXpert features of this DimXpert intersect point.

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
Dim instance As IDimXpertIntersectPointFeature
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

See [DimXpertIntersectPointFeature::GetFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectPointFeature~GetFeatures.html).

## See Also

[IDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature.html)
[IDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
