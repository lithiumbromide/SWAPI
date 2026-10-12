---
title: "Blind Property (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "Blind"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~Blind.html"
---

# Blind Property (IDimXpertCompoundHoleFeature)

Gets whether the DimXpert compound hole is blind or through all.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Blind As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
Dim value As System.Boolean

value = instance.Blind
```

### C#

```csharp
System.bool Blind {get;}
```

### C++/CLI

```cpp
property System.bool Blind {
   System.bool get();
}
```

### Property Value

True if blind; false if through all

## VBA Syntax

See [DimXpertCompoundHoleFeature::Blind](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundHoleFeature~Blind.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
