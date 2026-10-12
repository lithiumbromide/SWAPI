---
title: "PrimaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeLineProfileGeoTol"
member: "PrimaryInLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol~PrimaryInLowerTier.html"
---

# PrimaryInLowerTier Property (ISwDMDimXpertCompositeLineProfileGeoTol)

Gets whether the primary datum is repeated in the lower tier of this DimXpert composite line profile geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryInLowerTier As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeLineProfileGeoTol
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

See [SwDMDimXpertCompositeLineProfileGeoTol::PrimaryInLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeLineProfileGeoTol~PrimaryInLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeLineProfileGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol.html)
[ISwDMDimXpertCompositeLineProfileGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeLineProfileGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
