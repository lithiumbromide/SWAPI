---
title: "DimensionTypeIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "DimensionTypeIntraFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.html"
---

# DimensionTypeIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the type of dimension tolerance used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimensionTypeIntraFeature As swDmDimXpertDimensionToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol
Dim value As swDmDimXpertDimensionToleranceType_e

value = instance.DimensionTypeIntraFeature
```

### C#

```csharp
swDmDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {get;}
```

### C++/CLI

```cpp
property swDmDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {
   swDmDimXpertDimensionToleranceType_e get();
}
```

### Property Value

Type of dimension tolerance as defined in [swDmDimXpertDimensionToleranceType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertDimensionToleranceType_e.html)

## VBA Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::DimensionTypeIntraFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
