---
title: "BlockToleranceDecimalPlacesIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "BlockToleranceDecimalPlacesIntraFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~BlockToleranceDecimalPlacesIntraFeature.html"
---

# BlockToleranceDecimalPlacesIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the precision of the block tolerances used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlockToleranceDecimalPlacesIntraFeature As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol
Dim value As System.Integer

value = instance.BlockToleranceDecimalPlacesIntraFeature
```

### C#

```csharp
System.int BlockToleranceDecimalPlacesIntraFeature {get;}
```

### C++/CLI

```cpp
property System.int BlockToleranceDecimalPlacesIntraFeature {
   System.int get();
}
```

### Property Value

Number of decimal places for block tolerances

## VBA Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::BlockToleranceDecimalPlacesIntraFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~BlockToleranceDecimalPlacesIntraFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
