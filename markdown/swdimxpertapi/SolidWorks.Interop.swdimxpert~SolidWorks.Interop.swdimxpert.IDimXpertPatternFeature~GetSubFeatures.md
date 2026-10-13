---
title: "GetSubFeatures Method (IDimXpertPatternFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPatternFeature"
member: "GetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature~GetSubFeatures.html"
---

# GetSubFeatures Method (IDimXpertPatternFeature)

Gets all of the sub-features of this DimXpert pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPatternFeature
Dim value As System.Object

value = instance.GetSubFeatures()
```

### C#

```csharp
System.object GetSubFeatures()
```

### C++/CLI

```cpp
System.Object^ GetSubFeatures();
```

### Return Value

Array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

## VBA Syntax

See [DimXpertPatternFeature::GetSubFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPatternFeature~GetSubFeatures.html).

## Examples

[Get and Set Pattern Example (C#)](Get_and_Set_Pattern_Example_CSharp.htm)
[Get and Set Pattern Example (VB.NET)](Get_and_Set_Pattern_Example_VBNET.htm)
[Get and Set Pattern Example (VBA)](Get_and_Set_Pattern_Example_VB.htm)
[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## Remarks

This method returns all sub-features of the pattern feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection of the pattern do appear in the DimXpertManager tree.

For example, the sub-features of a simple hole are related to functional geometry and are not listed in the DimXpertManager tree. However, the sub-features of a hole pattern are manufacturing features (e.g., simple holes) that are significant for downstream processes. These manufacturing features are listed in the DimXpertManager tree.

## See Also

[IDimXpertPatternFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature.html)
[IDimXpertPatternFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
