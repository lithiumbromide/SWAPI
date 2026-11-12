---
title: "SecondaryInLowerTier Property (ISwDMDimXpertCompositeSurfaceProfileGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeSurfaceProfileGeoTol"
member: "SecondaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol~SecondaryInLowerTier.html"
---

# SecondaryInLowerTier Property (ISwDMDimXpertCompositeSurfaceProfileGeoTol)

Gets whether the secondary datum is repeated in the lower tier for this DimXpert composite surface profile geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SecondaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeSurfaceProfileGeoTol
Dim value As System.Boolean

value = instance.SecondaryInLowerTier
```

### C#

```csharp
System.bool SecondaryInLowerTier {get;}
```

### C++/CLI

```cpp
property System.bool SecondaryInLowerTier {
   System.bool get();
}
```

### Property Value

True, if the secondary datum is repeated in the lower tier; false, otherwise

## VBA Syntax

See [SwDMDimXpertCompositeSurfaceProfileGeoTol::SecondaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeSurfaceProfileGeoTol~SecondaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeSurfaceProfileGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol.html)
[ISwDMDimXpertCompositeSurfaceProfileGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
