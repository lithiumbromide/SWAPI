---
title: "CompoundHoleType Property (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "CompoundHoleType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~CompoundHoleType.html"
---

# CompoundHoleType Property (IDimXpertCompoundHoleFeature)

Gets the type of this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompoundHoleType As swDimXpertCompoundHoleType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
Dim value As swDimXpertCompoundHoleType_e

value = instance.CompoundHoleType
```

### C#

```csharp
swDimXpertCompoundHoleType_e CompoundHoleType {get;}
```

### C++/CLI

```cpp
property swDimXpertCompoundHoleType_e CompoundHoleType {
   swDimXpertCompoundHoleType_e get();
}
```

### Property Value

Type of this DimXpert compound hole as defined in [swDimXpertCompoundHoleType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertCompoundHoleType_e.html)

## VBA Syntax

See [DimXpertCompoundHoleFeature::CompoundHoleType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundHoleFeature~CompoundHoleType.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
