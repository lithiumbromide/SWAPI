---
title: "IDimXpertAnnotation Interface"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: ""
kind: "interface"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html"
---

# IDimXpertAnnotation Interface

Allows you to access DimXpert annotations on the DimXpertManager tab of the Management Panel.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
```

### C#

```csharp
public interface IDimXpertAnnotation
```

### C++/CLI

```cpp
public interface class IDimXpertAnnotation
```

## VBA Syntax

See [DimXpertAnnotation](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)
[Get DimXpert Features and Annotations Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## Remarks

This interface is the base class for three types of annotation interface: [IDimXpertTolerance](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance.html), [IDimXpertDimensionTolerance](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionTolerance.html), and [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html). Use the [IDimXpertAnnotation::Type](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~Type.html) property to find out which specific interface is needed to acquire more information for a given DimXpert annotation type.

## Accessors

[IDimXpertAnnotation::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetAppliedAnnotations.html) and [IDimXpertAnnotation::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~IGetAppliedAnnotations.html)

[IDimXpertFeature::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedAnnotations.html) and [IDimXpertFeature::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~IGetAppliedAnnotations.html)

[IDimXpertGtol::Annotation](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertGtol~Annotation.html)

[IDimXpertPart::GetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotations.html) and [IDimXpertPart::IGetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~IGetAnnotations.html)

[IDimXpertPart::GetAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotation.html)

[IDimXpertPart::InsertGtol](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertGtol.html)

[IFeature::GetSpecificFeature2](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## See Also

[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
