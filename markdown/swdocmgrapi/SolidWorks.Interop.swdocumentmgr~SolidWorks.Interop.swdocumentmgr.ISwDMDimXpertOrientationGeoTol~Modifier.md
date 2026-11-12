---
title: "Modifier Property (ISwDMDimXpertOrientationGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertOrientationGeoTol"
member: "Modifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~Modifier.html"
---

# Modifier Property (ISwDMDimXpertOrientationGeoTol)

Gets the material condition modifier for this DimXpert orientation geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertOrientationGeoTol
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

See [SwDMDimXpertOrientationGeoTol::Modifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertOrientationGeoTol~Modifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.html)
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
