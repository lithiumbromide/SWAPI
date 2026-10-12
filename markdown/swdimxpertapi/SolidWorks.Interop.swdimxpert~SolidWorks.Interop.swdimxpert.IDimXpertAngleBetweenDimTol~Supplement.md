---
title: "Supplement Property (IDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenDimTol"
member: "Supplement"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol~Supplement.html"
---

# Supplement Property (IDimXpertAngleBetweenDimTol)

Gets whether to evaluate the supplement angle for this DimXpert angle-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Supplement As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenDimTol
Dim value As System.Boolean

value = instance.Supplement
```

### C#

```csharp
System.bool Supplement {get;}
```

### C++/CLI

```cpp
property System.bool Supplement {
   System.bool get();
}
```

### Property Value

True to evaluate the supplement angle (default); false otherwise

## VBA Syntax

See [DimXpertAngleBetweenDimTol::Supplement](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenDimTol~Supplement.html).

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
