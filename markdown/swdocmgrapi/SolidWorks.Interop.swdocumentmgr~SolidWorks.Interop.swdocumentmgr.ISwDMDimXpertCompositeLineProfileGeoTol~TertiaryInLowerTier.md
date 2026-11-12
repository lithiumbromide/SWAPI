---
title: "TertiaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeLineProfileGeoTol"
member: "TertiaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol~TertiaryInLowerTier.html"
---

# TertiaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)

Gets whether the tertiary datum is repeated in the lower tier of this DimXpert composite line profile geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TertiaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeLineProfileGeoTol
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

See [SwDMDimXpertCompositeLineProfileGeoTol::TertiaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeLineProfileGeoTol~TertiaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeLineProfileGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol.html)
[ISwDMDimXpertCompositeLineProfileGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
