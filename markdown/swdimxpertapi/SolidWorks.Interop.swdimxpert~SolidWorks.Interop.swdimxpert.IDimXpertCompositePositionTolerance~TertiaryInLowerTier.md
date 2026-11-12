---
title: "TertiaryInLowerTier Property (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "TertiaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~TertiaryInLowerTier.html"
---

# TertiaryInLowerTier Property (IDimXpertCompositePositionTolerance)

Gets whether the tertiary datum is repeated in the lower tier of this DimXpert composite position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TertiaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositePositionTolerance
Dim value As System.Boolean

value = instance.TertiaryInLowerTier
```

### C#

```csharp
System.bool TertiaryInLowerTier {get;}
```

### C++/CLI

```cpp
property System.bool TertiaryInLowerTier {
   System.bool get();
}
```

### Property Value

True if the tertiary datum is repeated in the lower tier; false otherwise

## VBA Syntax

See [DimXpertCompositePositionTolerance::TertiaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~TertiaryInLowerTier.html).

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
