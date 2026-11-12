---
title: "Blind Property (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "Blind"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~Blind.html"
---

# Blind Property (IDimXpertExtrudeFeature)

Gets whether the DimXpert extrude is blind or through all.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Blind As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
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

See [DimXpertExtrudeFeature::Blind](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~Blind.html).

## Examples

[Get DimXpert Extrude Feature Example (VBA)](Get_DimXpert_Extrude_Feature_Example_VB.htm)
[Get DimXpert Extrude Feature Example (VB.NET)](Get_DimXpert_Extrude_Feature_Example_VBNET.htm)

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
