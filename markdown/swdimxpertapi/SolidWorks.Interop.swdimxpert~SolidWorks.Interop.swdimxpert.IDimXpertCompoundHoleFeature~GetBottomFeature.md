---
title: "GetBottomFeature Method (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "GetBottomFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetBottomFeature.html"
---

# GetBottomFeature Method (IDimXpertCompoundHoleFeature)

Gets the bottom DimXpert feature for this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
Dim value As DimXpertFeature

value = instance.GetBottomFeature()
```

### C#

```csharp
DimXpertFeature GetBottomFeature()
```

### C++/CLI

```cpp
DimXpertFeature^ GetBottomFeature();
```

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertCompoundHoleFeature::GetBottomFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundHoleFeature~GetBottomFeature.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## Remarks

Only blind holes have bottom features. The bottom feature of a blind hole is a [DimXpert plane feature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html) in which the plane is perpendicular to the hole axis.

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
