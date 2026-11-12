---
title: "IDimXpertDimensionTolerance Interface"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionTolerance"
member: ""
kind: "interface"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance.html"
---

# IDimXpertDimensionTolerance Interface

Allows you to access DimXpert dimension tolerance information for annotations on the DimXpertManager tab of the Management Panel.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimXpertDimensionTolerance
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionTolerance
```

### C#

```csharp
public interface IDimXpertDimensionTolerance
```

### C++/CLI

```cpp
public interface class IDimXpertDimensionTolerance
```

## VBA Syntax

See [DimXpertDimensionTolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionTolerance.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)
[Get DimXpert Features and Annotations Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## Remarks

This interface is the base class for several more specific interfaces (see the **See Also** section below). You can access more general annotation information using [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html). Use the [IDimXpertAnnotation::Type](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~Type.html) property to find out which specific interface is needed to acquire more information for a given DimXpert tolerance type.

## Accessors

[IDimXpertAnnotation::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetAppliedAnnotations.html) and [IDimXpertAnnotation::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~IGetAppliedAnnotations.html)

[IDimXpertPart::GetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotations.html) and [IDimXpertPart::IGetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~IGetAnnotations.html)

[IDimXpertPart::GetAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotation.html)

[IDimXpertFeature::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedAnnotations.html) and [IDimXpertFeature::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~IGetAppliedAnnotations.html)

[IFeature::GetSpecificFeature2](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## See Also

[IDimXpertDimensionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance_members.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
[IDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol.html)
[IDimXpertChamferDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCounterBoreDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterBoreDimTol.html)
[IDimXpertCounterSinkAngleDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkAngleDimTol.html)
[IDimXpertCounterSinkDiameterDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkDiameterDimTol.html)
[IDimXpertDepthDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDepthDimTol.html)
[IDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol.html)
[IDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol.html)
[IDimXpertRadiusDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRadiusDimTol.html)
