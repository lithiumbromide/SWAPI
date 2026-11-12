---
title: "SecondaryInLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "SecondaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~SecondaryInLowerTier.html"
---

# SecondaryInLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)

Gets whether the secondary datum is repeated in the lower tier of this DimXpert composite position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SecondaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositePositionGeoTol
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

See [SwDMDimXpertCompositePositionGeoTol::SecondaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~SecondaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
