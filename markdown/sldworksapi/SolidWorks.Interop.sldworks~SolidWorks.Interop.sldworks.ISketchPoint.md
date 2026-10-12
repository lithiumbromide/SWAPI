---
title: "ISketchPoint Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html"
---

# ISketchPoint Interface

Provides access to sketch point entities.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
```

### C#

```csharp
public interface ISketchPoint
```

### C++/CLI

```cpp
public interface class ISketchPoint
```

## VBA Syntax

See [SketchPoint](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint.html).

## Examples

[Get Sketch Points and Sketch Point IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)
[Get Sketch Points (VBA)](Get_Sketch_Points_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## Remarks

The ISketchPoint object provides access to sketch points while the [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) object provides access to sketch arcs, lines, ellipses, parabolas, and splines and their corresponding [ISketchArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html), [ISketchEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse.html), [ISketchLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine.html), [ISketchParabola](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola.html), [ISketchText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText.html), and [ISketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html) interfaces.

## Accessors

[IChainPatternFeatureData::Group1PathLink1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html)

[IChainPatternFeatureData::Group1PathLink2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)

[IChainPatternFeatureData::Group2PathLink1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)

[IChainPatternFeatureData::Group2PathLink2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html)

[IDomeFeatureData2::ConstraintPointOrSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~ConstraintPointOrSketch.html)

[IEnumSketchPoints::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchPoints~Next.html)

[IFillPatternFeatureData::SeedFeatureCenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter.html)

[IHingeMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate.html)

[IHoleSeriesFeatureData2::GetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPoints.html) and [IHoleSeriesFeatureData2::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetSketchPoints.html)

[ILayer::GetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems.html)

[ILocalSketchPatternFeatureData::SelectedPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.html)

[IModelDoc2::CreatePoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePoint2.html) and [IModelDoc2::ICreatePoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePoint2.html)

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html)

[IMoveCopyBodyFeatureData::TranslateToVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TranslateToVertex.html)

[IPartialEdgeFilletData::ReferenceOffsetEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEnd.html)

[IPartialEdgeFilletData::ReferenceOffsetStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.html)

[IPrimaryMemberPointLengthFeatureData::EndPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndPoint.html)

[IPrimaryMemberPointLengthFeatureData::GetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~GetPoints.html)

[ISecondaryMemberUpToMembersFeatureData::GetFromPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPoint.html)

[ISecondaryMemberUpToMembersFeatureData::GetPointMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetPointMemberPairs.html)

[ISketch::GetSketchPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchPoints2.html)

[ISketchArc::GetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~GetCenterPoint2.html) and [ISketchArc::IGetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~IGetCenterPoint2.html)

[ISketchArc::GetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~GetEndPoint2.html) and [ISketchArc::IGetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~IGetEndPoint2.html)

[ISketchArc::GetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~GetStartPoint2.html) and [ISketchArc::IGetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc~IGetStartPoint2.html)

[ISketchEllipse::GetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~GetCenterPoint2.html) and [ISketchEllipse::IGetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~IGetCenterPoint2.html)

[ISketchEllipse::GetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~GetEndPoint2.html) and [ISketchEllipse::IGetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~IGetEndPoint2.html)

[ISketchEllipse::GetMajorPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~GetMajorPoint2.html) and [ISketchEllipse::IGetMajorPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~IGetMajorPoint2.html)

[ISketchEllipse::GetMinorPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetMinorPoint2.html) and [ISketchEllipse::IGetMinorPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~IGetMinorPoint2.html)

[ISketchEllipse::GetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~GetStartPoint2.html) and [ISketchEllipse::IGetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse~IGetStartPoint2.html)

[ISketchLine::GetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine~GetEndPoint2.html) and [ISketchLine::IGetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine~IGetEndPoint2.html)

[ISketchLine::GetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine~GetStartPoint2.html) and [ISketchLine::IGetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine~IGetStartPoint2.html)

[ISketchParabola::GetApexPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~GetApexPoint2.html) and [ISketchParabola::IGetApexPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~IGetApexPoint2.html)

[ISketchParabola::GetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~GetEndPoint2.html) and [ISketchParabola::IGetEndPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~IGetEndPoint2.html)

[ISketchParabola::GetFocalPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~GetFocalPoint2.html) and [ISketchParabola::IGetFocalPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~IGetFocalPoint2.html)

[ISketchParabola::GetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~GetStartPoint2.html) and [ISketchParabola::IGetStartPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchParabola~IGetStartPoint2.html)

[ISketchPatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.html)

[ISketchSlot::GetCenterPointHandle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot~GetCenterPointHandle.html)

[ISketchSlot::GetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot~GetSlotPoints.html)

[ISMGussetFeatureData::ReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html)

[IStructuralMemberFeatureData::GetConnectionPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html) and [IStructuralMemberFeatureData::IGetConnectionPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html)

[IStructuralMemberFeatureData::LocateProfilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint.html)

[IStructuralMemberGroup::LocateProfilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup~LocateProfilePoint.html)

[IStructureSystemMemberProfile::PiercePointSelectionObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~PiercePointSelectionObject.html)

[ISurfaceFlattenFeatureData::FixPointVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~FixPointVertex.html)

[ISymmetricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.html)

[ITabAndSlotGroupData::SelectionEndReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint.html)

[ITabAndSlotGroupData::SelectionStartReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint.html)

[ITablePatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.html)

[IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.html)

[IWizardHoleFeatureData2::GetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.html) and [IWizardHoleFeatureData2::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.html)

[IWrapSketchFeatureData::PullDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWrapSketchFeatureData~PullDirection.html)

## Access Diagram

[SketchPoint](SWObjectModel.pdf#SketchPoint)

## See Also

[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.html)
[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.html)
[IRefPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)
