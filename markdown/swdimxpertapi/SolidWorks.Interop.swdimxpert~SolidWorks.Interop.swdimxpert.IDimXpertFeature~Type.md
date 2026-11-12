---
title: "Type Property (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "Type"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~Type.html"
---

# Type Property (IDimXpertFeature)

Gets the type of this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As swDimXpertFeatureType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As swDimXpertFeatureType_e

value = instance.Type
```

### C#

```csharp
swDimXpertFeatureType_e Type {get;}
```

### C++/CLI

```cpp
property swDimXpertFeatureType_e Type {
   swDimXpertFeatureType_e get();
}
```

### Property Value

Type of this DimXpert feature as defined in [swDimXpertFeatureType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertFeatureType_e.html)

## VBA Syntax

See [DimXpertFeature::Type](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~Type.html).

## Examples

[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
