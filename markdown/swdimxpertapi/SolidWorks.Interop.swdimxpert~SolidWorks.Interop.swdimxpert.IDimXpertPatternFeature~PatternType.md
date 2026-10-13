---
title: "PatternType Property (IDimXpertPatternFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPatternFeature"
member: "PatternType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature~PatternType.html"
---

# PatternType Property (IDimXpertPatternFeature)

Gets the type of this DimXpert pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternType As swDimXpertFeatureType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPatternFeature
Dim value As swDimXpertFeatureType_e

value = instance.PatternType
```

### C#

```csharp
swDimXpertFeatureType_e PatternType {get;}
```

### C++/CLI

```cpp
property swDimXpertFeatureType_e PatternType {
   swDimXpertFeatureType_e get();
}
```

### Property Value

Type of this DimXpert pattern feature as defined in [swDimXpertFeatureType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertFeatureType_e.html)

## VBA Syntax

See [DimXpertPatternFeature::PatternType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPatternFeature~PatternType.html).

## Examples

[Get and Set Pattern Example (C#)](Get_and_Set_Pattern_Example_CSharp.htm)
[Get and Set Pattern Example (VB.NET)](Get_and_Set_Pattern_Example_VBNET.htm)
[Get and Set Pattern Example (VBA)](Get_and_Set_Pattern_Example_VB.htm)
[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertPatternFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature.html)
[IDimXpertPatternFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
