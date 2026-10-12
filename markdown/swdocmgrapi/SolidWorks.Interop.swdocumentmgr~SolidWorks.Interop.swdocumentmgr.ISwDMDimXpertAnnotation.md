---
title: "ISwDMDimXpertAnnotation Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAnnotation"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html"
---

# ISwDMDimXpertAnnotation Interface

Allows you to access general information about DimXpert geometric tolerance, dimension tolerance, and datum annotations.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMDimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAnnotation
```

### C#

```csharp
public interface ISwDMDimXpertAnnotation
```

### C++/CLI

```cpp
public interface class ISwDMDimXpertAnnotation
```

## VBA Syntax

See [SwDMDimXpertAnnotation](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAnnotation.html).

## Examples

[Get DimXpert Sphere and Datum (VB.NET)](Get_DimXpert_Sphere_and_Datum_Example_VBNET.htm)
[Get DimXpert Sphere and Datum (C#)](Get_DimXpert_Sphere_and_Datum_Example_CSharp.htm)

## Remarks

This interface is the base class for three types of annotation interface: [ISwDMDimXpertGeometricTolerance](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html), [ISwDMDimXpertDimensionTolerance](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html), and [ISwDMDimXpertDatum](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDatum.html). Use the [ISwDMDimXpertAnnotation::type](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.html) property to find out which specific interface is needed to acquire more information for a given DimXpert annotation type.

## Accessors

[ISwDMDimXpertPart::GetAnnotations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.html) and [ISwDMDimXpertPart::IGetAnnotations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.html)

## See Also

[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
