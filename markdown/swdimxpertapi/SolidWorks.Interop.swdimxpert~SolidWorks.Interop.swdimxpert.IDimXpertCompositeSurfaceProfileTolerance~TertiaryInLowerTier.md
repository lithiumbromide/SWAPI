---
title: "TertiaryInLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeSurfaceProfileTolerance"
member: "TertiaryInLowerTier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance~TertiaryInLowerTier.html"
---

# TertiaryInLowerTier Property (IDimXpertCompositeSurfaceProfileTolerance)

Gets whether the tertiary datum is repeated in the lower tier for this DimXpert composite surface profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TertiaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeSurfaceProfileTolerance
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

See [DimXpertCompositeSurfaceProfileTolerance::TertiaryInLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeSurfaceProfileTolerance~TertiaryInLowerTier.html).

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
