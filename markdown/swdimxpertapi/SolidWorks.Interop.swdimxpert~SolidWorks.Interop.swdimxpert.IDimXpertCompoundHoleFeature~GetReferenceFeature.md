---
title: "GetReferenceFeature Method (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "GetReferenceFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetReferenceFeature.html"
---

# GetReferenceFeature Method (IDimXpertCompoundHoleFeature)

Gets the reference DimXpert feature for this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
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

See [DimXpertCompoundHoleFeature::GetReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundHoleFeature~GetReferenceFeature.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## Remarks

The reference feature is used to dimension the depth of a blind hole. This method currently returns a plane feature but could return another feature type. Cast the object returned by this method to [IDimXpertPlaneFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html).

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
