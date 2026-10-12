---
title: "ToleranceLowerTier Property (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "ToleranceLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~ToleranceLowerTier.html"
---

# ToleranceLowerTier Property (IDimXpertCompositePositionTolerance)

Gets the tolerance value in the lower tier for this DimXpert composite position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ToleranceLowerTier As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositePositionTolerance
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

See [DimXpertCompositePositionTolerance::ToleranceLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~ToleranceLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertCompositePositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
