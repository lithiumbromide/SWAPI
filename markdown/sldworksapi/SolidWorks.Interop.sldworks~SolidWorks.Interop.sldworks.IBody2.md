---
title: "IBody2 Interface"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html"
---

# IBody2 Interface

Allows access to the faces on a body and the ability to create surfaces for sewing into a body object.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBody2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
```

### C#

```csharp
public interface IBody2
```

### C++/CLI

```cpp
public interface class IBody2
```

## VBA Syntax

See [Body2](ms-its:sldworksapivb6.chm::/sldworks~Body2.html).

## Examples

[Get Bodies (C++)](Get_Bodies_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Original Body from Pattern Body (VBA)](Get_Original_Body_from_Pattern_Body_Example_VB.htm)
[Get Original Body from Pattern Body (VB.NET)](Get_Original_Body_from_Pattern_Body_Example_VBNET.htm)
[Get Original Body from Pattern Body (C#)](Get_Original_Body_from_Pattern_Body_Example_CSharp.htm)
[Display Temporary Body (C#)](Display_Temporary_Body_Example_CSharp.htm)
[Display Temporary Body (VB.NET)](Display_Temporary_Body_Example_VBNET.htm)
[Display Temporary Body (VBA)](Display_Temporary_Body_Example_VB.htm)

## Accessors

[IAttribute::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetBody.html)

[IBody2::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Copy.html)

[IBody2::CreateBodyFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromFaces.html) and [IBody2::ICreateBodyFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBodyFromFaces.html)

[IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html) and [IBody2::ICreateTempBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateTempBodyFromSurfaces.html) designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2|c3820'

[IBody2::DeleteFacesMakeSheetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html) and [IBody2::IDeleteFacesMakeSheetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html) designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2|c3823'

[IBody2::ExtendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ExtendSurface.html) and [IBody2::IExtendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IExtendSurface.html)

[IBody2::GetExcessBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetExcessBodyArray.html)

[IBody2::GetMiddleSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetMiddleSurface.html) and [IBody2::IGetMiddleSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetMiddleSurface.html)

[IBody2::GetOriginalPatternedBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetOriginalPatternedBody.html)

[IBody2::GetProcessedBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetProcessedBody2.html) and [IBody2::IGetProcessedBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetProcessedBody.html)

[IBody2::GetProcessedBodyWithSelFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html) and [IBody2::IGetProcessedBodyWithSelFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)

SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html

[IBody2::GetSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetSheetBody.html) and [IBody2::IGetSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetSheetBody.html)

[IBody2::MakeOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MakeOffset.html)

[IBody2::OffsetPlanarWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~OffsetPlanarWireBody.html)

[IBody2::Operations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Operations2.html) and [IBody2::IOperations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html)

[IBoundaryBossFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodies.html)

[ICircularPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScopeBodies.html)

[ICircularPatternFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~IGetPatternBodyArray.html)

[ICircularPatternFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~PatternBodyArray.html)

[ICombineBodiesFeatureData::IGetBodiesToCombine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.html)

[ICombineBodiesFeatureData::BodiesToCombine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.html)

[ICombineBodiesFeatureData::MainBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~MainBody.html)

[IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html) and [IComponent2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetBody.html)

[IComponent2::GetBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBodies3.html)

[IConfiguration::GetDisplayStateBodyProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.html)

[ICoreFeatureData::TargetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoreFeatureData~TargetBody.html)

[ICornerReliefFeatureData::GetBodyScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetBodyScope.html)

[ICurve::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateWireBody.html)

[ICurveDrivenPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~FeatureScopeBodies.html)

[ICurveDrivenPatternFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.html)

[ICurveDrivenPatternFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.html)

[IDeleteBodyFeatureData::Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html)

[IDeleteBodyFeatureData::IGetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.html)

[IEdge::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~CreateWireBody.html)

[IEdge::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetBody.html)

[IEnumBodies2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Next.html)

[IExtrudeFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.html)

[IExtrudeFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.html)

[IFace2::CreateSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~CreateSheetBody.html) and [IFace2::ICreateSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ICreateSheetBody.html)

[IFace2::CreateSheetBodyByFaceExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html) and [IFace2::ICreateSheetBodyByFaceExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)

[IFace2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetBody.html) and [IFace2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetBody.html)

[IFacet::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet~GetBody.html)

[IFeatureManager::PreIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreIntersect.html)

[IFillPatternFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeatureScopeBodies.html)

[IGraphicsBody::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody~GetBody.html)

[IIndentFeatureData::TargetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html)

[IIntersectFeatureData::GetIntersections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData~GetIntersections.html)

[IIntersectFeatureData::GetIntersectionsTools](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.html)

[ILinearPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~FeatureScopeBodies.html)

[ILinearPatternFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILinearPatternFeatureData~IGetPatternBodyArray.html)

[ILinearPatternFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.html)

[ILoftFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~FeatureScopeBodies.html)

[ILoftFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~IGetFeatureScopeBodies.html)

[ILoop2::RevolvePlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~RevolvePlanarLoop.html) and [ILoop2::IRevolvePlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IRevolvePlanarLoop.html)

[ILoop2::SweepPlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~SweepPlanarLoop.html) and [ILoop2::ISweepPlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~ISweepPlanarLoop.html)

[IMacroFeatureData::EditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~EditBodies.html)

[IMacroFeatureData::IGetEditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetEditBodies.html)

[IMassProperty2::SelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.html)

[IMeshBody::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody~GetBody.html)

[IMidSurface2::GetNextNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.html) and [IMidSurface2::IGetFirstNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.html)

[IMirrorPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.html)

[IMirrorPatternFeatureData::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies.html)

[IMirrorSolidFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~IGetPatternBodyArray.html)

[IMirrorSolidFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~PatternBodyArray.html)

[IModeler::CheckInterferenceBetweenTwoBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.html)

[IModeler::CreateBodiesFromSheets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html) and [IModeler::ICreateBodiesFromSheets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)

[IModeler::CreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBrepBody3.html) and [IModeler::ICreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBrepBody3.html)

[IModeler::CreateExtrudedBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateExtrudedBody.html)

[IModeler::CreateSheetFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSheetFromFaces.html) and [IModeler::ICreateSheetFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)

[IModeler::CreateSweptBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSweptBody.html)

[IModeler::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateWireBody.html) and [IModeler::ICreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateWireBody.html)

[IModeler::CheckInterference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CheckInterference.html) and [IModeler::ICheckInterference2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterference2.html)

[IModeler::CreateBodyFromBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromBox.html) and [IModeler::ICreateBodyFromBox2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)

[IModeler::CreateBodyFromCone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromCone.html) and [IModeler::ICreateBodyFromCone2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)

[IModeler::CreateBodyFromCyl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromCyl.html) and [IModeler::ICreateBodyFromCyl2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)

[IModeler::CreateBodyFromFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromFaces2.html) and [IModeler::ICreateBodyFromFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)

[IModeler::CreateSheetFromSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSheetFromSurface.html) and [IModeler::ICreateSheetFromSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)

[IModeler::Restore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~Restore.html) and [IModeler::IRestore2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IRestore2.html)

[IMoveCopyBodyFeatureData::Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies.html)

[IMoveCopyBodyFeatureData::IGetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.html)

[IMoveFaceFeatureData::GetEndConditionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)

[IPartDoc::CreateNewBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateNewBody.html) and [IPartDoc::ICreateNewBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateNewBody2.html)

[IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html)

[IPartDoc::GetRelatedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetRelatedBodies.html)

[IPartDoc::GetRelatedSectionedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html)

[IPartExplodeStep::GetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetBodies.html)

[IRevolveFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~FeatureScopeBodies.html)

[IRevolveFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~IGetFeatureScopeBodies.html)

[ISaveBodyFeatureData::GetSaveBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.html)

[IScaleFeatureData::Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~Bodies.html)

[IScaleFeatureData::IGetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~IGetBodies.html)

[ISectionViewData::SelectiveSectioningList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.html)

[ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html)

[ISimpleHoleFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.html)

[ISimpleHoleFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.html)

[ISketchPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScopeBodies.html)

[ISketchPatternFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~IGetPatternBodyArray.html)

[ISketchPatternFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~PatternBodyArray.html)

[ISketchSegment::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~CreateWireBody.html)

[ISplitBodyFeatureData::GetSplitBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html) and [ISplitBodyFeatureData::IGetSplitBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html)

[ISpring::BaseProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~BaseProfile.html)

[ISpring::GetSpringBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~GetSpringBody.html)

[ISpring::SectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~SectionProfile.html)

[IStructureSystemMemberFeatureData::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetBody.html)

[IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html)

[ISurface::CreateTrimmedSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet.html)

[ISurfaceCutFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.html)

[ISurfaceCutFeatureData::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html)

[ISurfaceTrimFeatureData::IGetPiecesToKeep](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.html)

[ISurfaceTrimFeatureData::PiecesToKeep](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.html)

[ISweepFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~FeatureScopeBodies.html)

[ISweepFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~IGetFeatureScopeBodies.html)

[ISweepFeatureData::Profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html)

[ITablePatternFeatureData::IGetPatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~IGetPatternBodyArray.html)

[ITablePatternFeatureData::PatternBodyArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.html)

[IThickenFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~FeatureScopeBodies.html)

[IThickenFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~IGetFeatureScopeBodies.html)

[IToolingSplitFeatureData::IGetCavitySurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetCavitySurfaces.html)

[IToolingSplitFeatureData::CavitySurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~CavitySurfaces.html)

[IToolingSplitFeatureData::CoreSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~CoreSurfaces.html) and [IToolingSplitFeatureData::IGetCoreSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetCoreSurfaces.html)

[IToolingSplitFeatureData::IGetPartingSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.html)

[IToolingSplitFeatureData::PartingSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.html)

[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html)

[IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.html)

[IWizardHoleFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FeatureScopeBodies.html)

[IWizardHoleFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IGetFeatureScopeBodies.html)

## Access Diagram

[Body2](SWObjectModel.pdf#Body2)

## See Also

[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)
