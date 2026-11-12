---
title: "PrimaryInLowerTier Property (IDimXpertCompositeLineProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeLineProfileTolerance"
member: "PrimaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance~PrimaryInLowerTier.html"
---

# PrimaryInLowerTier Property (IDimXpertCompositeLineProfileTolerance)

Gets whether the primary datum is repeated in the lower tier of this DimXpert composite line profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeLineProfileTolerance
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

See [DimXpertCompositeLineProfileTolerance::PrimaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeLineProfileTolerance~PrimaryInLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositeLineProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
