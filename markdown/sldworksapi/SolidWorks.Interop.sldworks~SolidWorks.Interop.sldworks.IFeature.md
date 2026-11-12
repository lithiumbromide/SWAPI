---
title: "IFeature Interface"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html"
---

# IFeature Interface

Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
```

### C#

```csharp
public interface IFeature
```

### C++/CLI

```cpp
public interface class IFeature
```

## VBA Syntax

See [Feature](ms-its:sldworksapivb6.chm::/sldworks~Feature.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)
[Traverse Assembly At Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)
[Get Areas of MidSurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)
[Get Areas of MidSurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)
[Get Areas of MidSurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)

## Accessors

[IAssemblyDoc::GetActiveGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.html)

[IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html)

[IAssemblyDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~FeatureByName.html) and [IAssemblyDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IFeatureByName.html)

[IBody2::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFeatures.html) and [IBody2::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetFeatures.html)

[IBodyFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~GetFeature.html)

[IBodyFolder::GetTopLevelFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatures.html)

[IBomFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetFeature.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IComment::FeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment~FeatureOwner.html)

[ICommentFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~GetFeature.html)

[IComplexCornerTreatmentFeatureData::GetTrimToolMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.html)

[IComponent2::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FeatureByName.html)

[IComponent2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FirstFeature.html)

[IConfiguration::GetDisplayStateFeatureProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html)

[ICoreFeatureData::BoundingSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoreFeatureData~BoundingSketch.html)

[ICornerManagementFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetFeature.html)

[ICornerManagementFolder::GetStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetStructureSystemFolder.html)

[ICornerMember::GetUnderlyingMemberFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~GetUnderlyingMemberFeature.html)

[ICornerTreatmentFeatureData::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~GetFeature.html)

[ICornerTreatmentGroupFolder::GetCornerTreatments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html)

[ICornerTreatmentGroupFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetFeature.html)

[ICosmosMotionStudyResults::GetPlotFeatures](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotFeatures.html) and [ICosmosMotionStudyResults::IGetPlotFeatures](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~IGetPlotFeatures.html)

[ICosmosMotionStudyResults::InsertPlotFeature](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~InsertPlotFeature.html)

[ICurveDrivenPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.html)

[ICutListSortOptions::GetFacesOrFeaturesToExclude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude.html)

[IDerivedPatternFeatureData::IGetSeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~IGetSeedComponentArray.html)

[IDerivedPatternFeatureData::PatternFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PatternFeature.html)

[IDerivedPatternFeatureData::SeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~SeedComponentArray.html)

[IDimension::GetFeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetFeatureOwner.html)

[IDimXpertAnnotation::GetModelFeature](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetModelFeature.html)

[IDimXpertFeature::GetModelFeature](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetModelFeature.html)

[IDrawingDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~FeatureByName.html) and [IDrawingDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IFeatureByName.html)

[IFace2::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFeature.html) and [IFeature::IGetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFeature.html)

[IFace2::GetPatternSeedFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetPatternSeedFeature.html) and [IFace2::IGetPatternSeedFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetPatternSeedFeature.html)

[IFamilyTableFeature::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetFeature.html)

[IFeature::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetChildren.html) and [IFeature::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetChildren.html)

[IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html) and [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html)

[IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) and [IFeature::IGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html)

[IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html) and [IFeature::IGetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextSubFeature.html)

[IFeature::GetOwnerFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetOwnerFeature.html)

[IFeature::GetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetParents.html) and [IFeature::IGetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetParents.html)

[IFeatureFolder::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~GetFeatures.html) and [IFeatureFolder::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~IGetFeatures.html)

[IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.html)

[IFeatureManager::CreateFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFeature.html)

[IFeatureManager::CreateFormTool2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFormTool2.html)

[IFeatureManager::CreateCoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.html)

[IFeatureManager::CreateCoordinateSystemUsingNumericalValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystemUsingNumericalValues.html)

[IFeatureManager::CreateSaveBodyFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateSaveBodyFeature.html)

[IFeatureManager::DraftXpertChange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~DraftXpertChange.html)

[IFeatureManager::DraftXpertRemove](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~DraftXpertRemove.html)

[IFeatureManager::EndVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html)

[IFeatureManager::FeatureAdvancedTableDrivenPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.html)

[IFeatureManager::FeatureBossThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureBossThicken.html)

[IFeatureManager::FeatureChainPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureChainPattern.html)

[IFeatureManager::FeatureCircularPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.html)

[IFeatureManager::FeatureCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCut.html)

[IFeatureManager::FeatureCutThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThicken.html)

[IFeatureManager::FeatureCutThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThin.html)

[IFeatureManager::FeatureExtrusion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureExtrusion2.html)

[IFeatureManager::FeatureExtrusionThin2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.html)

[IFeatureManager::FeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet.html) and [IFeatureManager::IFeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IFeatureFillet.html)

[IFeatureManager::FeatureFillPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillPattern.html)

[IFeatureManager::FeatureFolderLocation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFolderLocation.html)

[IFeatureManager::FeatureLinearPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLinearPattern2.html)

[IFeatureManager::FeatureLocalCurveDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLocalCurveDrivenPattern.html)

[IFeatureManager::FeatureLocalSketchDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLocalSketchDrivenPattern.html)

[IFeatureManager::FeatureRevolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html)

[IFeatureManager::FeatureRevolveCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveCut.html)

[IFeatureManager::FeatureRevolveThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)

[IFeatureManager::FeatureRevolveThinCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)

[IFeatureManager::FeatureSketchDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureSketchDrivenPattern.html)

[IFeatureManager::FilletXpertChange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FilletXpertChange.html)

[IFeatureManager::FilletXpertRemove](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

[IFeatureManager::FinishCornerRelief](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FinishCornerRelief.html)

[IFeatureManager::FinishSMNormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishSMNormalCut.html)

[IFeatureManager::GetCornerManagementFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCornerManagementFolders.html)

[IFeatureManager::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFeatures.html) and [IFeatureManager::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IGetFeatures.html)

[IFeatureManager::GetStructureSystemFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetStructureSystemFolders.html)

[IFeatureManager::HoleWizard5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~HoleWizard5.html)

[IFeatureManager::InsertCenterofMass](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCenterOfMass.html)

[IFeatureManager::InsertCenterOfMassReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCenterOfMassReferencePoint.html)

[IFeatureManager::InsertCombineFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCombineFeature.html) and [IFeatureManager::IInsertCombineFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertCombineFeature.html)

[IFeatureManager::InsertCosmeticThread2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticThread2.html)

[IFeatureManager::InsertCosmeticWeldBead2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.html)

[IFeatureManager::InsertCrossBreak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCrossBreak.html)

[IFeatureManager::InsertCutBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutBlend.html)

[IFeatureManager::InsertCutSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSwept3.html)

[IFeatureManager::InsertCutSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSurface.html)

[IFeatureManager::InsertDeleteBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDeleteBody.html)

[IFeatureManager::InsertDeleteHoleForSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteHoleForSurface.html)

[IFeatureManager::InsertDerivedPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDerivedPattern.html)

[IFeatureManager::InsertDwgOrDxfFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile.html)

[IFeatureManager::InsertEdgeMerge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertEdgeMerge.html)

[IFeatureManager::InsertEndCapFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertEndCapFeature.html)

[IFeatureManager::InsertEndCapFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertEndCapFeature2.html)

[IFeatureManager::InsertFeatureChamfer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFeatureChamfer.html)

[IFeatureManager::InsertFeatureLock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureLock.html)

[IFeatureManager::InsertFeatureTreeFolder2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFeatureTreeFolder2.html)

[IFeatureManager::InsertFilletBeadFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature2.html)

[IFeatureManager::InsertFilletBeadFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature3.html)

[IFeatureManager::InsertFillSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFillSurface2.html)

[IFeatureManager::InsertFlattenSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface.html)

[IFeatureManager::InsertFlexFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFlexFeature.html)

[IFeatureManager::InsertFormToolFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFormToolFeature.html)

[IFeatureManager::InsertFreeform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFreeform.html)

[IFeatureManager::InsertGlobalBoundingBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGlobalBoundingBox.html)

[IFeatureManager::InsertGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.html)

[IFeatureManager::InsertGussetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertGussetFeature.html)

[IFeatureManager::InsertGussetFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertGussetFeature2.html)

[IFeatureManager::InsertIndent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertIndent.html)

[IFeatureManager::InsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html) and [IFeatureManager::IInsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html)

[IFeatureManager::InsertMateReference2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMateReference2.html)

[IFeatureManager::InsertMirrorFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html)

[IFeatureManager::InsertMoldCoreCavitySolids](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.html)

[IFeatureManager::InsertMoldPartingLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.html)

[IFeatureManager::InsertMoldPartingSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface.html)

[IFeatureManager::InsertMoldShutOffSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.html)

[IFeatureManager::InsertMoveCopyBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html)

[IFeatureManager::InsertMoveFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveFace.html)

[IFeatureManager::InsertMultifaceDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMultiFaceDraft.html)

[IFeatureManager::InsertNetBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertNetBlend.html)

[IFeatureManager::InsertProtrusionBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionBlend.html)

[IFeatureManager::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html)

[IFeatureManager::InsertReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertReferencePoint.html) and [IFeatureManager::IInsertReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertReferencePoint.html)

[IFeatureManager::InsertRevolvedRefSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface.html)

[IFeatureManager::InsertRuledSurfaceFromEdge2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.html)

[IFeatureManager::InsertScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertScale.html)

[IFeatureManager::InsertSheetMetal3dBend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetal3dBend.html)

[IFeatureManager::InsertSheetMetalBaseFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange2.html)

[IFeatureManager::InsertSheetMetalCornerTrim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalCornerTrim.html)

[IFeatureManager::InsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html) and [IFeatureManager::IInsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertSheetMetalEdgeFlange2.html)

[IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.html)

[IFeatureManager::InsertSheetMetalHem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.html)

[IFeatureManager::InsertSheetMetalLoftedBend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend.html)

[IFeatureManager::InsertSheetMetalMiterFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalMiterFlange.html)

[IFeatureManager::InsertSplitLineIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.html)

[IFeatureManager::InsertStructuralWeldment2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2.html)

[IFeatureManager::InsertStructuralWeldment3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html)

[IFeatureManager::InsertSubFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSubFolder.html)

[IFeatureManager::InsertSubWeldFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSubWeldFolder.html)

[IFeatureManager::InsertSubWeldFolder2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSubWeldFolder2.html)

[IFeatureManager::InsertSweepSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSweepSurface2.html)

[IFeatureManager::InsertTableDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern.html) and [IFeatureManager::IInsertTableDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertTableDrivenPattern.html)

[IFeatureManager::InsertUntrimSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertUntrimSurface.html)

[IFeatureManager::InsertWeldmentCutList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentCutList.html)

[IFeatureManager::InsertWeldmentCutList2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentCutList2.html)

[IFeatureManager::InsertWeldmentFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentFeature.html)

[IFeatureManager::InsertWeldmentTrimFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.html)

[IFeatureManager::InsertWeldmentTrimFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.html)

[IFeatureManager::InsertWrapFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWrapFeature.html)

[IFeatureManager::PostIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostIntersect.html)

[IFeatureManager::PostSplitBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostSplitBody.html)

[IFeatureManager::PostTrimSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostTrimSurface.html)

[IFeatureManager::SetNetBlendCurveData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.html)

[IFeatureManager::SetNetBlendDirectionData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.html)

[IFeatureManager::SimpleHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SimpleHole.html)

[IFeatureStatistics::Features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureStatistics~Features.html)

[IFillPatternFeatureData::PatternFeatureArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternFeatureArray.html)

[IFlatPatternFeatureData::GetAddCornerTrim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)

[IFlatPatternFeatureData::GetBreakCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.html)

[IFlatPatternFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFolder~GetFeature.html)

[IFlatPatternFolder::GetFlatPatterns](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFolder~GetFlatPatterns.html)

[IFoldsFeatureData::Bends](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~Bends.html)

[IFoldsFeatureData::IGetBends](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBends.html)

[IGeneralTableFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature~GetFeature.html)

[IGeneralToleranceTableFeature::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature~GetFeature.html)

[IHoleTable::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~GetFeature.html)

[ILinearPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFeatureArray.html)

[ILocalCircularPatternFeatureData::IGetSeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSeedComponentArray.html)

[ILocalCircularPatternFeatureData::SeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCircularPatternFeatureData~SeedComponentArray.html)

[ILocalLinearPatternFeatureData::IGetSeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~IGetSeedComponentArray.html)

[ILocalLinearPatternFeatureData::SeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~SeedComponentArray.html)

[ILoftFeatureData::GuideCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves.html)

[ILoftFeatureData::IGetGuideCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.html)

[IMacroFeatureData::IGetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetParents.html)

[IMacroFeatureData::Parents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~Parents.html)

[IModelDoc2::FeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.html)

[IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html)

[IModelDoc2::InsertProjectedSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertProjectedSketch2.html) and [IModelDoc2::IInsertProjectedSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertProjectedSketch2.html)

[IModelDoc2::InsertSketchForEdgeFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.html) and [IModelDoc2::IInsertSketchForEdgeFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertSketchForEdgeFlange.html)

[IVersionCompatibilityItem::IncompatibleObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem~IncompatibleObject.html)

[IModelDocExtension::CreateStructureSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStructureSystem.html)

[IModelDocExtension::GetLastFeatureAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetLastFeatureAdded.html)

[IModelDocExtension::GetTemplateSheetMetal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal.html)

[IMotionPlotFeatureData::GetXAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotFeatureData~GetXAxis.html)

[IMotionPlotFeatureData::GetYAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.html) and [IMotionPlotFeatureData::IGetYAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis.html)

[IPartDoc::CreateFeatureFromBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.html)

[IPartDoc::CreateSurfaceFeatureFromBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.html) and [IPartDoc::ICreateSurfaceFeatureFromBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.html)

[IPartDoc::FeatureById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FeatureById.html) and [IPartDoc::IFeatureById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFeatureById.html)

[IPartDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FeatureByName.html) and [IPartDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFeatureByName.html)

[IPartDoc::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FirstFeature.html) and [IPartDoc::IFirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFirstFeature.html)

[IPartDoc::ICreateFeatureFromBody4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html)

[IPartDoc::InsertPart](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~InsertPart.html)

[IPartDoc::MirrorPart2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~MirrorPart2.html)

[IProfileGroupFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetFeature.html)

[IProfileGroupFolder::GetStructureSystemMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers.html)

[IPunchTable::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable~GetFeature.html)

[IReplaceFaceFeatureData::IGetReplacementSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.html)

[IReplaceFaceFeatureData::ReplacementSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.html)

[IRevisionTableFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature~GetFeature.html)

[ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)

[ISheetMetalFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFolder~GetFeature.html)

[ISheetMetalFolder::GetSheetMetals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFolder~GetSheetMetals.html)

[ISimpleFilletFeatureData2::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures.html)

[ISimpleFilletFeatureData2::Features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~Features.html)

[ISimulation::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation~GetFeature.html)

[ISketchBlockDefinition::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetFeature.html)

[ISketchPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.html)

[ISketchPicture::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~GetFeature.html)

[IStructureSystemFolder::GetCornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetCornerManagementFolder.html)

[IStructureSystemFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetFeature.html)

[IStructureSystemMemberFeatureData::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetFeature.html)

[ISweepFeatureData::IGetGuideCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)

[ISweepFeatureData::GuideCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html)

[ISweepFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html)

[ISweepFeatureData::Profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html)

[ITableAnchor::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnchor~GetFeature.html)

[ITablePatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.html)

[ITitleBlockTableFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableFeature~GetFeature.html)

[IWeldmentCutListFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListFeature~GetFeature.html)

## Access Diagram

[Feature](SWObjectModel.pdf#Feature)

## See Also

[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
