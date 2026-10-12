---
title: "SecondaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeLineProfileGeoTol"
member: "SecondaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol~SecondaryInLowerTier.html"
---

# SecondaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)

Gets whether the secondary datum is repeated in the lower tier of this DimXpert composite line profile geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SecondaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeLineProfileGeoTol
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

See [SwDMDimXpertCompositeLineProfileGeoTol::SecondaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeLineProfileGeoTol~SecondaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeLineProfileGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol.html)
[ISwDMDimXpertCompositeLineProfileGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
