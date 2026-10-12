---
title: "BlockToleranceDecimalPlaces Property (ISwDMDimXpertDimensionTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDimensionTolerance"
member: "BlockToleranceDecimalPlaces"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~BlockToleranceDecimalPlaces.html"
---

# BlockToleranceDecimalPlaces Property (ISwDMDimXpertDimensionTolerance)

Gets the precision of the block tolerance of this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlockToleranceDecimalPlaces As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDimensionTolerance
Dim value As System.Integer

value = instance.BlockToleranceDecimalPlaces
```

### C#

```csharp
System.int BlockToleranceDecimalPlaces {get;}
```

### C++/CLI

```cpp
property System.int BlockToleranceDecimalPlaces {
   System.int get();
}
```

### Property Value

Number of decimal places for block tolerance

## VBA Syntax

See [SwDMDimXpertDimensionTolerance::BlockToleranceDecimalPlaces](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDimensionTolerance~BlockToleranceDecimalPlaces.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html)
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
