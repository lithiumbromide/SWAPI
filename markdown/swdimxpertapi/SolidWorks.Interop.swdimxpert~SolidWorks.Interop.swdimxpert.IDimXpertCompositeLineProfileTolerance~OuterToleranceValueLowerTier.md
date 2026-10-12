---
title: "OuterToleranceValueLowerTier Property (IDimXpertCompositeLineProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeLineProfileTolerance"
member: "OuterToleranceValueLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance~OuterToleranceValueLowerTier.html"
---

# OuterToleranceValueLowerTier Property (IDimXpertCompositeLineProfileTolerance)

Gets the outer tolerance value in the lower tier for this DimXpert composite line profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OuterToleranceValueLowerTier As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeLineProfileTolerance
Dim value As System.Double

value = instance.OuterToleranceValueLowerTier
```

### C#

```csharp
System.double OuterToleranceValueLowerTier {get;}
```

### C++/CLI

```cpp
property System.double OuterToleranceValueLowerTier {
   System.double get();
}
```

### Property Value

Outer tolerance value in the lower tier

## VBA Syntax

See [DimXpertCompositeLineProfileTolerance::OuterToleranceValueLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeLineProfileTolerance~OuterToleranceValueLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositeLineProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
