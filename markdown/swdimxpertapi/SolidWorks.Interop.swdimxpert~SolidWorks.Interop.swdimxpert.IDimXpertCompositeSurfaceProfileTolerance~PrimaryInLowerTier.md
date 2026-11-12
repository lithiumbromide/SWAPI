---
title: "PrimaryInLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeSurfaceProfileTolerance"
member: "PrimaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance~PrimaryInLowerTier.html"
---

# PrimaryInLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)

Gets whether the primary datum is repeated in the lower tier for this DimXpert composite surface profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeSurfaceProfileTolerance
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

See [DimXpertCompositeSurfaceProfileTolerance::PrimaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeSurfaceProfileTolerance~PrimaryInLowerTier.html).

## Examples

[Get DimXpert Tolerance6 Example (VBA)](Get_DimXpert_Tolerance6_Example_VB.htm)
[Get DimXpert Tolerance6 Example (VB.NET)](Get_DimXpert_Tolerance6_Example_VBNET.htm)

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositeSurfaceProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance.html)
[IDimXpertCompositeSurfaceProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
