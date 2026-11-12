---
title: "IDimXpertTolerance Interface"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: ""
kind: "interface"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html"
---

# IDimXpertTolerance Interface

Allows you to access DimXpert geometric tolerance information for annotations on the DimXpertManager tab of the Management Panel.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimXpertTolerance
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
```

### C#

```csharp
public interface IDimXpertTolerance
```

### C++/CLI

```cpp
public interface class IDimXpertTolerance
```

## VBA Syntax

See [DimXpertTolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance.html).

## Examples

[Get DimXpert Tolerance1 Example (VBA)](Get_DimXpert_Tolerance1_Example_VB.htm)
[Get DimXpert Tolerance1 Example (VB.NET)](Get_DimXpert_Tolerance1_Example_VBNET.htm)
[Get DimXpert Features and Annotations Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## Remarks

DimXpert geometric tolerance annotations are configured by clicking the Geometric Tolerance icon on the DimXpert tool bar and entering information in the Geometric Tolerance Properties dialog. This interface accesses the tolerances, datums, and datum modifiers that are set in this dialog.

Use this interface to obtain circularity, cylindricity, circular runout, and total runout tolerance data. This interface is also the base class for several more specific interfaces (see **See Also** section below). You can access more general annotation information using [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html). Use the [IDimXpertAnnotation::Type](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~Type.html) property to find out which specific interface is needed to acquire more information for a given tolerance type.

## Accessors

[IDimXpertAnnotation::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetAppliedAnnotations.html) and [IDimXpertAnnotation::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~IGetAppliedAnnotations.html)

[IDimXpertPart::GetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotations.html) and [IDimXpertPart::IGetAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~IGetAnnotations.html)

[IDimXpertPart::GetAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotation.html)

[IDimXpertFeature::GetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedAnnotations.html) and [IDimXpertFeature::IGetAppliedAnnotations](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~IGetAppliedAnnotations.html)

[IFeature::GetSpecificFeature2](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## See Also

[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
[IDimXpertPositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance.html)
[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertSymmetryTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance.html)
[IDimXpertConcentricityTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConcentricityTolerance.html)
[IDimXpertLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertLineProfileTolerance.html)
[IDimXpertSurfaceProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSurfaceProfileTolerance.html)
[IDimXpertCompositeSurfaceProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeSurfaceProfileTolerance.html)
[IDimXpertFlatnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFlatnessTolerance.html)
[IDimXpertOrientationTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance.html)
[IDimXpertStraightnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance.html)
[IDimXpertTangencyTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTangencyTolerance.html)
