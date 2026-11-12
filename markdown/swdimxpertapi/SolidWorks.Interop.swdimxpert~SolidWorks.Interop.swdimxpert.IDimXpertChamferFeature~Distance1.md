---
title: "Distance1 Property (IDimXpertChamferFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertChamferFeature"
member: "Distance1"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature~Distance1.html"
---

# Distance1 Property (IDimXpertChamferFeature)

Gets the length on bevel side 1 of the selected edge, face, or vertex.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Distance1 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertChamferFeature
Dim value As System.Double

value = instance.Distance1
```

### C#

```csharp
System.double Distance1 {get;}
```

### C++/CLI

```cpp
property System.double Distance1 {
   System.double get();
}
```

### Property Value

Length of bevel on one side of the selected entity

## VBA Syntax

See [DimXpertChamferFeature::Distance1](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertChamferFeature~Distance1.html).

## Examples

[Get DimXpert Chamfer Feature Example (VBA)](Get_DimXpert_Chamfer_Feature_Example_VB.htm)
[Get DimXpert Chamfer Feature Example (VB.NET)](Get_DimXpert_Chamfer_Feature_Example_VBNET.htm)

## See Also

[IDimXpertChamferFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature.html)
[IDimXpertChamferFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
