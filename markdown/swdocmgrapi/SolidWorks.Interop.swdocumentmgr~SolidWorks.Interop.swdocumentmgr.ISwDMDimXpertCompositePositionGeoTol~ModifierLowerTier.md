---
title: "ModifierLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "ModifierLowerTier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~ModifierLowerTier.html"
---

# ModifierLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)

Gets the material condition modifer for the tolerance in the lower tier for this DimXpert composite position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ModifierLowerTier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositePositionGeoTol
Dim value As swDmDimXpertMaterialConditionModifier_e

value = instance.ModifierLowerTier
```

### C#

```csharp
swDmDimXpertMaterialConditionModifier_e ModifierLowerTier {get;}
```

### C++/CLI

```cpp
property swDmDimXpertMaterialConditionModifier_e ModifierLowerTier {
   swDmDimXpertMaterialConditionModifier_e get();
}
```

### Property Value

Material condition modifier in the lower tier as defined in [swDmDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [SwDMDimXpertCompositePositionGeoTol::ModifierLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~ModifierLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
