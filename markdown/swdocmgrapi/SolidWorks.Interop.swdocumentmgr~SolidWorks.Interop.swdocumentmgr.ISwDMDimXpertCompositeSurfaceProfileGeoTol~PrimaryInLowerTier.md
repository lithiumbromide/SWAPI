---
title: "PrimaryInLowerTier Property (ISwDMDimXpertCompositeSurfaceProfileGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeSurfaceProfileGeoTol"
member: "PrimaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol~PrimaryInLowerTier.html"
---

# PrimaryInLowerTier Property (ISwDMDimXpertCompositeSurfaceProfileGeoTol)

Gets whether the primary datum is repeated in the lower tier of this DimXpert composite surface profile geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeSurfaceProfileGeoTol
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

True, if the primary datum is repeated in the lower tier; false, otherwise

## VBA Syntax

See [SwDMDimXpertCompositeSurfaceProfileGeoTol::PrimaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeSurfaceProfileGeoTol~PrimaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeSurfaceProfileGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol.html)
[ISwDMDimXpertCompositeSurfaceProfileGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeSurfaceProfileGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
