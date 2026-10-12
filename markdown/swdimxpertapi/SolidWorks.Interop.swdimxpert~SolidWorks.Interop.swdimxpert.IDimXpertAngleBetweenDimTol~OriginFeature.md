---
title: "OriginFeature Property (IDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenDimTol"
member: "OriginFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol~OriginFeature.html"
---

# OriginFeature Property (IDimXpertAngleBetweenDimTol)

Gets the DimXpert origin feature for this DimXpert angle-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OriginFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenDimTol
Dim value As DimXpertFeature

value = instance.OriginFeature
```

### C#

```csharp
DimXpertFeature OriginFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ OriginFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertAngleBetweenDimTol::OriginFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenDimTol~OriginFeature.html).

## Examples

[Get and Set Location Dimension Example (C#)](Get_and_Set_Location_Dimension_Example_CSharp.htm)
[Get and Set Location Dimension Example (VB.NET)](Get_and_Set_Location_Dimension_Example_VBNET.htm)
[Get and Set Location Dimension Example (VBA)](Get_and_Set_Location_Dimension_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VBA)](Get_DimXpert_Tolerance4_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VB.NET)](Get_DimXpert_Tolerance4_Example_VBNET.htm)

## See Also

[IDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol.html)
[IDimXpertAngleBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
