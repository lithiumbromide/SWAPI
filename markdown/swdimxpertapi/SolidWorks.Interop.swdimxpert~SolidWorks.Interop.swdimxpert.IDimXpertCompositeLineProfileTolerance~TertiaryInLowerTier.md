---
title: "TertiaryInLowerTier Property (IDimXpertCompositeLineProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeLineProfileTolerance"
member: "TertiaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance~TertiaryInLowerTier.html"
---

# TertiaryInLowerTier Property (IDimXpertCompositeLineProfileTolerance)

Gets whether the tertiary datum is repeated in the lower tier of this DimXpert composite line profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TertiaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeLineProfileTolerance
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

See [DimXpertCompositeLineProfileTolerance::TertiaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeLineProfileTolerance~TertiaryInLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositeLineProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
