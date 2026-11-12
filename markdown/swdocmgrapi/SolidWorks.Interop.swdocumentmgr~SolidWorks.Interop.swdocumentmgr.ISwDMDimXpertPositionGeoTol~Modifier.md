---
title: "Modifier Property (ISwDMDimXpertPositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPositionGeoTol"
member: "Modifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~Modifier.html"
---

# Modifier Property (ISwDMDimXpertPositionGeoTol)

Gets the material condition modifier for this DimXpert position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPositionGeoTol
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

See [SwDMDimXpertPositionGeoTol::Modifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPositionGeoTol~Modifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.html)
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
