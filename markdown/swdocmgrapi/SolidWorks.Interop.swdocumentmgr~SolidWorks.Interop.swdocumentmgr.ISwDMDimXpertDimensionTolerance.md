---
title: "ISwDMDimXpertDimensionTolerance Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDimensionTolerance"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html"
---

# ISwDMDimXpertDimensionTolerance Interface

Allows you to access general information about DimXpert dimension tolerances.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMDimXpertDimensionTolerance
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDimensionTolerance
```

### C#

```csharp
public interface ISwDMDimXpertDimensionTolerance
```

### C++/CLI

```cpp
public interface class ISwDMDimXpertDimensionTolerance
```

## VBA Syntax

See [SwDMDimXpertDimensionTolerance](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDimensionTolerance.html).

## Examples

[Get DimXpert Tolerance (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)
[Get DimXpert Tolerance (C#)](Get_DimXpert_Tolerance_Example_CSharp.htm)

## Remarks

This interface is the base class for several more specific interfaces. (See the **See Also** section.) You can access more general information from [ISwDMDimXpertAnnotation](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html). Use the [ISwDMDimXpertAnnotation::type](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.html) property to find out which specific interface is needed to acquire more information for a given DimXpert tolerance type.

## Accessors

[ISwDMDimXpertPart::GetAnnotations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.html) and [ISwDMDimXpertPart::IGetAnnotations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.html)

## See Also

[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol.html)
[ISwDMDimXpertChamferDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertConeAngleDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeAngleDimTol.html)
[ISwDMDimXpertCounterBoreDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol.html)
[ISwDMDimXpertCounterSinkAngleDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol.html)
[ISwDMDimXpertCounterSinkDiameterDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkDiameterDimTol.html)
[ISwDMDimXpertDepthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol.html)
[ISwDMDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDiameterDimTol.html)
[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.html)
[ISwDMDimXpertLengthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertLengthDimTol.html)
[ISwDMDimXpertRadiusDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertRadiusDimTol.html)
[ISwDMDimXpertWidthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertWidthDimTol.html)
[ISwDMDimXpertPatternAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternAngleBetweenDimTol.html)
