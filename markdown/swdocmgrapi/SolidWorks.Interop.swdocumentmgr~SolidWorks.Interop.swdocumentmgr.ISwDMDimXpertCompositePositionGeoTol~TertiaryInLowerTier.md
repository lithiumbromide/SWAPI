---
title: "TertiaryInLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "TertiaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~TertiaryInLowerTier.html"
---

# TertiaryInLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)

Gets whether the tertiary datum is repeated in the lower tier of this DimXpert composite position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TertiaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositePositionGeoTol
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

True, if the tertiary datum is repeated in the lower tier; false, otherwise

## VBA Syntax

See [SwDMDimXpertCompositePositionGeoTol::TertiaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~TertiaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
