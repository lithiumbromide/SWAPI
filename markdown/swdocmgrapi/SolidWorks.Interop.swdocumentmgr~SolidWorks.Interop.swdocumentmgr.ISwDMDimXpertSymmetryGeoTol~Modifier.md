---
title: "Modifier Property (ISwDMDimXpertSymmetryGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertSymmetryGeoTol"
member: "Modifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~Modifier.html"
---

# Modifier Property (ISwDMDimXpertSymmetryGeoTol)

Gets the material condition modifier for this DimXpert symmetry geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertSymmetryGeoTol
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

See [SwDMDimXpertSymmetryGeoTol::Modifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertSymmetryGeoTol~Modifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.html)
[ISwDMDimXpertSymmetryGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
