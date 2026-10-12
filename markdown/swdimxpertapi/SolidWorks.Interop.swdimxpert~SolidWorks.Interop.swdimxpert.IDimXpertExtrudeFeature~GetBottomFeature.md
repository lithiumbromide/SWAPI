---
title: "GetBottomFeature Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "GetBottomFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~GetBottomFeature.html"
---

# GetBottomFeature Method (IDimXpertExtrudeFeature)

Gets the bottom DimXpert feature for this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
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

See [DimXpertExtrudeFeature::GetBottomFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~GetBottomFeature.html).

## Examples

[Get DimXpert Extrude Feature Example (VBA)](Get_DimXpert_Extrude_Feature_Example_VB.htm)
[Get DimXpert Extrude Feature Example (VB.NET)](Get_DimXpert_Extrude_Feature_Example_VBNET.htm)

## Remarks

Only blind extrudes have bottom features. The bottom feature of a blind extrude is usually a [DimXpert plane feature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html).

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
