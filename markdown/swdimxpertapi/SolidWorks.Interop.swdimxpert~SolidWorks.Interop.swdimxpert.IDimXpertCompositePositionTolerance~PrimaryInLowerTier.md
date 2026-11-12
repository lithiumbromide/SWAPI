---
title: "PrimaryInLowerTier Property (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "PrimaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~PrimaryInLowerTier.html"
---

# PrimaryInLowerTier Property (IDimXpertCompositePositionTolerance)

Gets whether the primary datum is repeated in the lower tier of this DimXpert composite position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositePositionTolerance
Dim value As System.Boolean

value = instance.PrimaryInLowerTier
```

### C#

```csharp
System.bool PrimaryInLowerTier {get;}
```

### C++/CLI

```cpp
property System.bool PrimaryInLowerTier {
   System.bool get();
}
```

### Property Value

True if the primary datum is repeated in the lower tier; false otherwise

## VBA Syntax

See [DimXpertCompositePositionTolerance::PrimaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~PrimaryInLowerTier.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertCompositePositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
