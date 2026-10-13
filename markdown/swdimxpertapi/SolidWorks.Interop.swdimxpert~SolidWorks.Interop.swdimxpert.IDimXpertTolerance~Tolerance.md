---
title: "Tolerance Property (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "Tolerance"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~Tolerance.html"
---

# Tolerance Property (IDimXpertTolerance)

Gets the value of this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Tolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Double

value = instance.Tolerance
```

### C#

```csharp
System.double Tolerance {get;}
```

### C++/CLI

```cpp
property System.double Tolerance {
   System.double get();
}
```

### Property Value

Value of geometric tolerance

## VBA Syntax

See [DimXpertTolerance::Tolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~Tolerance.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
