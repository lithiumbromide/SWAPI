---
title: "ToleranceLowerTier Property (IDimXpertCompositeLineProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeLineProfileTolerance"
member: "ToleranceLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance~ToleranceLowerTier.html"
---

# ToleranceLowerTier Property (IDimXpertCompositeLineProfileTolerance)

Gets the tolerance value in the lower tier for this DimXpert composite line profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ToleranceLowerTier As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeLineProfileTolerance
Dim value As System.Double

value = instance.ToleranceLowerTier
```

### C#

```csharp
System.double ToleranceLowerTier {get;}
```

### C++/CLI

```cpp
property System.double ToleranceLowerTier {
   System.double get();
}
```

### Property Value

Tolerance value in the lower tier

## VBA Syntax

See [DimXpertCompositeLineProfileTolerance::ToleranceLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeLineProfileTolerance~ToleranceLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositeLineProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
