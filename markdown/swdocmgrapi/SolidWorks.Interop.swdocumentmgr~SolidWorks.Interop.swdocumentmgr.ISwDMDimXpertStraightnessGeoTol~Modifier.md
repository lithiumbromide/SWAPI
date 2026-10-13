---
title: "Modifier Property (ISwDMDimXpertStraightnessGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertStraightnessGeoTol"
member: "Modifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~Modifier.html"
---

# Modifier Property (ISwDMDimXpertStraightnessGeoTol)

Gets the material condition modifier for this DimXpert straightness geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertStraightnessGeoTol
Dim value As swDmDimXpertMaterialConditionModifier_e

value = instance.Modifier
```

### C#

```csharp
swDmDimXpertMaterialConditionModifier_e Modifier {get;}
```

### C++/CLI

```cpp
property swDmDimXpertMaterialConditionModifier_e Modifier {
   swDmDimXpertMaterialConditionModifier_e get();
}
```

### Property Value

Material condition modifier as defined in [swDmDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [SwDMDimXpertStraightnessGeoTol::Modifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertStraightnessGeoTol~Modifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.html)
[ISwDMDimXpertStraightnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
