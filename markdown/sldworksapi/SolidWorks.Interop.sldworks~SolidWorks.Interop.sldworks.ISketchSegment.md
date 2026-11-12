---
title: "ISketchSegment Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html"
---

# ISketchSegment Interface

Provides access to functions that are common among sketch entities.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
```

### C#

```csharp
public interface ISketchSegment
```

### C++/CLI

```cpp
public interface class ISketchSegment
```

## VBA Syntax

See [SketchSegment](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment.html).

## Examples

[Get Sketch Segment Length (C++)](Get_Sketch_Segment_Length_Example_CPlusPlus_COM.htm)
[Get Sketch Segment Length (VBA)](Get_Sketch_Segment_Length_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)
[Select Chain of Entities Attached to a Sketch Segment (C#)](Select_Chain_of_Entities_Example_CSharp.htm)
[Select Chain of Entities Attached to a Sketch Segment (VB.NET)](Select_Chain_of_Entities_Example_VBNET.htm)
[Select Chain of Entities Attached to a Sketch Segment (VBA)](Select_Chain_of_Entities_Example_VB.htm)

## Remarks

A SketchSegment can represent a sketch arc, line, ellipse, parabola or spline.

ISketchSegment provides functions that are generic to every type of sketch segment. For example, every sketch segment has an ID and can be programmatically selected. Therefore, the ISketchSegment interface provides functions to obtain the ID and to select the item. (For access to sketched points, see the [ISketchPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) object)

## Accessors

[IBrokenOutSectionFeatureData::SketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.html) and [IBrokenOutSectionFeatureData::IGetSketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment.html)

[IDetailCircle::GetProfileItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~GetProfileItems.html) and [IDetailCircle::IGetProfileItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~IGetProfileItems.html)

[IEnumSketchSegments::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchSegments~Next.html)

[ILayer::GetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems.html)

[IMirrorComponentFeatureData::AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.html)

[IModelDoc2::CreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateArc2.html) and [IModelDoc2::ICreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateArc2.html)

[IModelDoc2::CreateCircle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircle2.html) and [IModelDoc2::ICreateCircle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateCircle2.html)

[IModelDoc2::CreateCircleByRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircleByRadius2.html) and [IModelDoc2::ICreateCircleByRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateCircleByRadius2.html)

[IModelDoc2::CreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse2.html) and [IModelDoc2::ICreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateEllipse2.html)

[IModelDoc2::CreateEllipticalArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.html) and [IModelDoc2::ICreateEllipticalArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.html)

[IModelDoc2::CreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLine2.html) and [IModelDoc2::ICreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateLine2.html)

[IModelDoc2::CreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateSpline.html) and [IModelDoc2::ICreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSpline.html)

[IModelDoc2::CreateSplneByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.html) and [IModelDoc2::ICreateSplineByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.html)

[IOneBendFeatureData::FlatPatternSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.html) and [IOneBendFeatureData::IFlatPatternSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments.html)

[IPrimaryMemberPathSegmentFeatureData::GetPathSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~GetPathSegments.html)

[IPrimaryMemberPointLengthFeatureData::DirectionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~DirectionReference.html)

[IRevolveFeatureData2::Axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~Axis.html)

[ISketch::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSegments.html)

[ISketch::GetSketchTextSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchTextSegments.html)

[ISketchContour::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~GetSketchSegments.html) and [ISketchContour::IGetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~IGetSketchSegments.html)

[ISketchManager::CreateFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateFillet.html)

[ISketchManager::CreateSpline3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.html)

[ISketchManager::CreateSplinesByEqnParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.html)

[ISketchPath::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~GetSketchSegments.html) and [ISketchPath::IGetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~IGetSketchSegments.html)

[ISMGussetFeatureData::ReferenceLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.html)

[IStructuralMemberFeatureData::GetPathSegmentAt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.html)

[IStructuralMemberFeatureData::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetSketchSegments.html)

[IStructuralMemberFeatureData::IGetPathSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.html)

[IStructuralMemberFeatureData::PathSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.html)

[IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html)

[IView::GetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLines.html) and [IView::IGetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBendLines.html)

[IWrapSketchFeatureData::PullDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWrapSketchFeatureData~PullDirection.html)

## Access Diagram

[SketchSegment](SWObjectModel.pdf#SketchSegment)

## See Also

[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
