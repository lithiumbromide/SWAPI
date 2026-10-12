---
title: "ToleranceLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeSurfaceProfileTolerance"
member: "ToleranceLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance~ToleranceLowerTier.html"
---

# ToleranceLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)

Gets the tolerance value in the lower tier for this DimXpert composite surface profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ToleranceLowerTier As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeSurfaceProfileTolerance
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

See [DimXpertCompositeSurfaceProfileTolerance::ToleranceLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeSurfaceProfileTolerance~ToleranceLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeSurfaceProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance.html)
[IDimXpertCompositeSurfaceProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
