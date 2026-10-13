---
title: "Radius Property (IDimXpertFilletFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFilletFeature"
member: "Radius"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature~Radius.html"
---

# Radius Property (IDimXpertFilletFeature)

Gets the radius of this DimXpert fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Radius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFilletFeature
Dim value As System.Double

value = instance.Radius
```

### C#

```csharp
System.double Radius {get;}
```

### C++/CLI

```cpp
property System.double Radius {
   System.double get();
}
```

### Property Value

Radius of the fillet

## VBA Syntax

See [DimXpertFilletFeature::Radius](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFilletFeature~Radius.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertFilletFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature.html)
[IDimXpertFilletFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
