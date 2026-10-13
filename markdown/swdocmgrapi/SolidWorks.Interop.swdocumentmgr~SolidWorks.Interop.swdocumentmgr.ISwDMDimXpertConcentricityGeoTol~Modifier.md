---
title: "Modifier Property (ISwDMDimXpertConcentricityGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertConcentricityGeoTol"
member: "Modifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConcentricityGeoTol~Modifier.html"
---

# Modifier Property (ISwDMDimXpertConcentricityGeoTol)

Gets the material condition modifier for this DimXpert concentricity geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertConcentricityGeoTol
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

Material condition modifier for the concentricity tolerance as defined in [swDmDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [SwDMDimXpertConcentricityGeoTol::Modifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertConcentricityGeoTol~Modifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertConcentricityGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConcentricityGeoTol.html)
[ISwDMDimXpertConcentricityGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConcentricityGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
