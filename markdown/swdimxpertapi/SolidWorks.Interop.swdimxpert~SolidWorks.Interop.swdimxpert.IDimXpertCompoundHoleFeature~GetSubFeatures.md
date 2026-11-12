---
title: "GetSubFeatures Method (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "GetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetSubFeatures.html"
---

# GetSubFeatures Method (IDimXpertCompoundHoleFeature)

Gets all of the sub-features of this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
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

See [DimXpertCompoundHoleFeature::GetSubFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundHoleFeature~GetSubFeatures.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## Remarks

This method returns all sub-features of the hole feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.

For example, the sub-features of a simple hole are related to functional geometry and are not listed in the DimXpertManager tree. However, the sub-features of a hole pattern are manufacturing features (e.g., simple holes) that are significant for downstream processes. These manufacturing features are listed in the DimXpertManager tree.

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
