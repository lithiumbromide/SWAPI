---
title: "DimensionType Property (ISwDMDimXpertDimensionTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDimensionTolerance"
member: "DimensionType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~DimensionType.html"
---

# DimensionType Property (ISwDMDimXpertDimensionTolerance)

Gets the type of this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimensionType As swDmDimXpertDimensionToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDimensionTolerance
Dim value As swDmDimXpertDimensionToleranceType_e

value = instance.DimensionType
```

### C#

```csharp
swDmDimXpertDimensionToleranceType_e DimensionType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertDimensionToleranceType_e DimensionType {
   swDmDimXpertDimensionToleranceType_e get();
}
```

### Property Value

Type of dimension tolerance as defined in [SwDmDimXpertDimensionToleranceType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertDimensionToleranceType_e.html)

## VBA Syntax

See [SwDMDimXpertDimensionTolerance::DimensionType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDimensionTolerance~DimensionType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html)
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
