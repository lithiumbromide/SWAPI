---
title: "GetReferenceFeature Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "GetReferenceFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~GetReferenceFeature.html"
---

# GetReferenceFeature Method (IDimXpertExtrudeFeature)

Gets the reference DimXpert feature for this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
Dim value As DimXpertFeature

value = instance.GetReferenceFeature()
```

### C#

```csharp
DimXpertFeature GetReferenceFeature()
```

### C++/CLI

```cpp
DimXpertFeature^ GetReferenceFeature();
```

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertExtrudeFeature::GetReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~GetReferenceFeature.html).

## Examples

[Get DimXpert Extrude Feature Example (VBA)](Get_DimXpert_Extrude_Feature_Example_VB.htm)
[Get DimXpert Extrude Feature Example (VB.NET)](Get_DimXpert_Extrude_Feature_Example_VBNET.htm)

## Remarks

The reference feature is used to dimension the depth of a blind extrude. This method currently returns a plane feature but could return another feature type. Cast the object returned by this method to [IDimXpertPlaneFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html).

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
