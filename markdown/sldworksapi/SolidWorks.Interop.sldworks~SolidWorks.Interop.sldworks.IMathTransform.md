---
title: "IMathTransform Interface"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html"
---

# IMathTransform Interface

Provides a simplified interface for manipulating transformation matrix data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
```

### C#

```csharp
public interface IMathTransform
```

### C++/CLI

```cpp
public interface class IMathTransform
```

## VBA Syntax

See [MathTransform](ms-its:sldworksapivb6.chm::/sldworks~MathTransform.html).

## Examples

[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)
[Calculate Transformations in Part (C#)](Calculate_Transformations_in_Part_Example_CSharp.htm)
[Calculate Transformations in Part (VB.NET)](Calculate_Transformations_in_Part_Example_VBNET.htm)
[Calculate Transformations in Part (VBA)](Calculate_Transformations_in_Part_Example_VB.htm)
[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

Transformation matrix data:

|a b c . n |

|d e f . o |

|g h i . p |

|j k l . m |

The SOLIDWORKS transformation matrix is stored as a homogeneous matrix of 16 elements, ordered as shown. The first 9 elements (a to i) are elements of a 3x3 rotational sub-matrix, the next 3 elements (j,k,l) define a translation vector, and the next 1 element (m) is a scaling factor. The last 3 elements (n,o,p) are unused in this context.

The 3x3 rotational sub-matrix represents 3 axis sets:

- row 1 for x-axis components of rotation
- row 2 for y-axis components of rotation
- row 3 for z-axis components of rotation

The 3 axes are constrained to be orthogonal and unified so that they produce a pure rotational transformation. Reflections can also be added to these axes by setting the components to negative. The rotation sub-matrix coupled with the lower-left translation vector and the lower-right corner scaling factor creates an affine transformation, which is a transformation that preserves lines and parallelism; i.e., maps parallel lines to parallel lines.

If the 3 axis sets of the 3x3 rotational sub-matrix are not orthogonal or unified, then they are automatically corrected according to the following rules:

- If any axis is 0, or any two axes are parallel, or all axes are coplanar, then an identity matrix replaces the rotational sub-matrix.
- All axes are corrected to be of unit length.
- The axes are built to be orthogonal to each other in the prioritized order of Z, X, Y (X is orthogonal to Z, Y is orthogonal to Z and X).

## Accessors

[IAnnotation::GetFipPlaneTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetFlipPlaneTransform.html)

[IBody2::GetCoincidenceTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetCoincidenceTransform.html)

[IBody2::GetOriginalPatternedBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetOriginalPatternedBody.html)

[ICircularPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~GetTransform.html)

[ICollision::GetTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~GetTransforms.html)

[ICollisionDetectionGroup::GetTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~GetTransforms.html)

[IComponent2::GetSpecificTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)

[IComponent2::GetTotalTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetTotalTransform.html)

[IComponent2::PresentationTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~PresentationTransform.html)

[IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html)

[ICosmeticThreadFeatureData::IGetPatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.html)

[ICosmeticThreadFeatureData::PatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms.html)

[ICThread::IGetPatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~IGetPatternedTransforms.html)

[ICThread::PatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~PatternedTransforms.html)

[ICurveDrivenPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~GetTransform.html)

[IDerivedPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~GetTransform.html)

[IDisplayDimension::GetDefinitionTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetDefinitionTransform.html)

[IInterferenceDetectionMgr::GetComponentsAndTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.html)

[ILinearPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILinearPatternFeatureData~GetTransform.html)

[ILocalCircularPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCircularPatternFeatureData~GetTransform.html)

[ILocalCurvePatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~GetTransform.html)

[ILocalLinearPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~GetTransform.html)

[ILocalSketchPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalSketchPatternFeatureData~GetTransform.html)

[IMacroFeatureData::FeatureTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~FeatureTransform.html)

[IMacroFeatureData::GetEditTargetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform.html)

[IMacroFeatureData::GetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetSelections3.html) and [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html)

[IMacroFeatureData::PatternTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~PatternTransform.html)

[IMathTransform::Inverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~Inverse.html) and [IMathTransform::IInverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~IInverse.html)

[IMathTransform::Multiply](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~Multiply.html) and [IMathTransform::IMultiply](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~IMultiply.html)

[IMathUtility::ComposeTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility~ComposeTransform.html)

[IMathUtility::CreateTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility~CreateTransform.html) and [IMathUtility::ICreateTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility~ICreateTransform.html)

[IMathUtility::CreateTransformRotateAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.html) and [IMathUtility::ICreateTransformRotateAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.html)

[IMirrorPartFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData~GetTransform.html)

[IMirrorSolidFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~GetTransform.html)

[IModelDocExtension::GetCoordinateSystemTransformByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html)

[IModelView::Orientation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Orientation3.html)

[IModelView::Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Transform.html)

[IRefPlane::Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane~Transform.html)

[ISectionViewData::GetDynamicCenterTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetDynamicCenterTransform.html)

[ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html)

[ISketchBlockInstance::BlockToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~BlockToSketchTransform.html)

[ISketchPatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~GetTransform.html)

[ITablePatternFeatureData::GetTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~GetTransform.html)

[IView::ModelToViewTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ModelToViewTransform.html)

[IView3D::Rotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D~Rotation.html)

## Access Diagram

[MathTransform](SWObjectModel.pdf#MathTransform)

## See Also

[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
