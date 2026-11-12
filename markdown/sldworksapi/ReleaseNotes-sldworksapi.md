---
title: "Release Notes"
project: "SOLIDWORKS API Help"
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/ReleaseNotes-sldworksapi.html"
---

# Release Notes

This topic provides you with quick access to the enhancements in SOLIDWORKS API 2026.

###### Service Pack 3

###### New interfaces, methods, and properties

##### IVersionCompatibilityItem Interface

- IVersionCompatibilityItem::IncompatibleObject
- IVersionCompatibilityItem::Version
- IVersionCompatibilityItem::ID
- IVersionCompatibilityItem::Message
- IVersionCompatibilityItem::Action

##### IModelDocExtension Interface

- [IModelDocExtension::CheckVersionCompatibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CheckVersionCompatibility.html)

##### DSldWorksEvents Handlers

- [DSldWorksEvents_FileSaveToVersionFailNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileSaveToVersionFailNotifyEventHandler.html)

##### DAssemblyDocEvents Handlers

- [DAssemblyDocEvents_AddDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddDependencyNotifyEventHandler.html)
- [DAssemblyDocEvents_DeleteDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteDependencyNotifyEventHandler.html)

##### DDrawingDocEvents Handlers

- [DDrawingDocEvents_AddDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AddDependencyNotifyEventHandler.html)
- [DDrawingDocEvents_DeleteDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DeleteDependencyNotifyEventHandler.html)

##### DPartDocEvents Handlers

- [DPartDocEvents_AddDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AddDependencyNotifyEventHandler.html)
- [DPartDocEvents_DeleteDependencyNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteDependencyNotifyEventHandler.html)

###### Service Pack 2

###### New interfaces, methods, and properties

##### IComponent2 Interface

- [IComponent2::HasAssemblyFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasAssemblyFeatures.html)

##### IDimXpertAngleBetweenCircularDimTol Interface

- IDimXpertAngleBetweenCircularDimTol::CenterFeature
- IDimXpertAngleBetweenCircularDimTol::GetActPlaneVector
- IDimXpertAngleBetweenCircularDimTol::GetNomPlaneVector
- IDimXpertAngleBetweenCircularDimTol::OriginFeature
- IDimXpertAngleBetweenCircularDimTol::Supplement

##### IDimXpertPart Interface

- IDimXpertPart::InsertAngleDimension

##### IDimXpertRefPlaneFeature Interface

- IDimXpertRefPlaneFeature::GetNominalPlane

##### IGTol Interface

- [IGTol::GetAllOver](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOver.html)
- [IGTol::SetAllOver](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOver.html)

##### IView Interface

- [IView::RootDrawingComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RootDrawingComponent2.html) (obsoletes IView::RootDrawingComponent)

###### Service Pack 1

###### New properties and method

##### IBoundingBoxFeatureData Interface

- [IBoundingBoxFeatureData::CoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~CoordinateSystem.html)
- [IBoundingBoxFeatureData::lwtaDirectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~lwtaDirectionType.html)

##### IDSPBRMaterial Interface

- [IDSPBRMaterial::ClearcoatNormalStrength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ClearcoatNormalStrength.html)
- [IDSPBRMaterial::EmissionColorTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionColorTexture.html)
- [IDSPBRMaterial::MetallicTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~MetallicTexture.html)
- [IDSPBRMaterial::NormalStrength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~NormalStrength.html)
- [IDSPBRMaterial::TransparencyTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~TransparencyTexture.html)

##### IModelDocExtension Interface

- [IModelDocExtension::ActivateFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html)
- [IModelDocExtension::AddFeatureMgrView3x64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddFeatureMgrView3x64.html)
- [IModelDocExtension::DeActivateFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeActivateFeatureMgrViewx64.html)

##### IModelView Interface

- [IModelView::UpAxisFlyout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~UpAxisFlyout.html)

###### Service Pack 0

- [New functionality](#NewFunctionality0)
- [New interfaces](#newinterfaces)
- [New delegates, methods, and properties](#NewMethods0)

###### New functionality

- Display the Dassault Systemes Physically Based Rendering (DSPBR) appearance visual style. See [IDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html), [IRenderMaterial::GetDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetDSPBRMaterial.html), and [IRenderMaterial::HasDSPBRProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HasDSPBRProperties.html).
- Add family tables to drawings and edit them. See [IFamilyTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation.html), [IFamilyTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html), [ISheet::InsertFamilyTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertFamilyTable.html).
- Get top-level items in body folders. See [IBodyFolder::GetTopLevelFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatureCount.html) and [IBodyFolder::GetTopLevelFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatures.html).
- Receive notifications when reordering solid body folders. See [DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler.html) and [DPartDocEvents_SolidBodyFolderReorderNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SolidBodyFolderReorderNotifyEventHandler.html).
- Get and set the edge thickness when the display style is set to "Shaded with Edges". See [ISldWorks::ShadedEdgeThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShadedEdgeThickness.html).
- Move parent drawing views independently of child views and receive notifications when changing view positions. See [IView::SetViewPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetViewPosition.html) and [DDrawingDocEvents_ViewPositionChangeNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewPositionChangeNotifyEventHandler.html).

###### New interfaces

##### IDSPBRMaterial Interface

- [IDSPBRMaterial::AbbeNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AbbeNumber.html)
- [IDSPBRMaterial::Albedo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Albedo.html)
- [IDSPBRMaterial::AlbedoTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AlbedoTexture.html)
- [IDSPBRMaterial::Anisotropy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Anisotropy.html)
- [IDSPBRMaterial::AnisotropyRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AnisotropyRotation.html)
- [IDSPBRMaterial::AttenuationColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AttenuationColor.html)
- [IDSPBRMaterial::AttenuationDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AttenuationDistance.html)
- [IDSPBRMaterial::ClearCoat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Clearcoat.html)
- [IDSPBRMaterial::ClearCoatNormalTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ClearcoatNormalTexture.html)
- [IDSPBRMaterial::ClearCoatRoughness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ClearcoatRoughness.html)
- [IDSPBRMaterial::CutoutOpacity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~CutoutOpacity.html)
- [IDSPBRMaterial::CutoutOpacityTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~CutoutOpacityTexture.html)
- [IDSPBRMaterial::Displacement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Displacement.html)
- [IDSPBRMaterial::DisplacementTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~DisplacementTexture.html)
- [IDSPBRMaterial::EmissionColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionColor.html)
- [IDSPBRMaterial::EmissionEnergyNormalization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionEnergyNormalization.html)
- [IDSPBRMaterial::EmissionMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionMode.html)
- [IDSPBRMaterial::EmissionValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionValue.html)
- [IDSPBRMaterial::FlakeColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeColor.html)
- [IDSPBRMaterial::FlakeCoverage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeCoverage.html)
- [IDSPBRMaterial::FlakeRoughness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeRoughness.html)
- [IDSPBRMaterial::FlakeSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeSize.html)
- [IDSPBRMaterial::FlakeTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeTexture.html)
- [IDSPBRMaterial::FlipFlop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlipFlop.html)
- [IDSPBRMaterial::FlipFlopColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlipFlopColor.html)
- [IDSPBRMaterial::IndexOfRefraction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~IndexOfRefraction.html)
- [IDSPBRMaterial::Metallic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Metallic.html)
- [IDSPBRMaterial::NormalTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~NormalTexture.html)
- [IDSPBRMaterial::RealViewToDSPBRTextureScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~RealViewToDSPBRTextureScale.html)
- [IDSPBRMaterial::Roughness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Roughness.html)
- [IDSPBRMaterial::RoughnessTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~RoughnessTexture.html)
- [IDSPBRMaterial::SheenColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SheenColor.html)
- [IDSPBRMaterial::SheenRoughness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SheenRoughness.html)
- [IDSPBRMaterial::Specular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Specular.html)
- [IDSPBRMaterial::SpecularTintColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SpecularTintColor.html)
- [IDSPBRMaterial::SubsurfaceAnisotropy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubsurfaceAnisotropy.html)
- [IDSPBRMaterial::SubsurfaceColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubsurfaceColor.html)
- [IDSPBRMaterial::SubType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubType.html)
- [IDSPBRMaterial::ThinFilm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilm.html)
- [IDSPBRMaterial::ThinFilmIOR](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmIOR.html)
- [IDSPBRMaterial::ThinFilmThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmThickness.html)
- [IDSPBRMaterial::ThinFilmThicknessTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmThicknessTexture.html)
- [IDSPBRMaterial::ThinWalled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinWalled.html)
- [IDSPBRMaterial::Translucency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Translucency.html)
- [IDSPBRMaterial::TranslucencyColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~TranslucencyColor.html)
- [IDSPBRMaterial::Transparency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Transparency.html)
- [IDSPBRMaterial::Version](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Version.html)

##### IFamilyTableAnnotation Interface

- [IFamilyTableAnnotation::FamilyTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation~FamilyTableFeature.html)
- [IFamilyTableAnnotation::GetSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation~GetSheet.html)

##### IFamilyTableFeature Interface

- [IFamilyTableFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetConfigurations.html)
- [IFamilyTableFeature::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetFeature.html)
- [IFamilyTableFeature::GetFollowConfigTreeOrder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetFollowConfigTreeOrder.html)
- [IFamilyTableFeature::GetModelName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetModelName.html)
- [IFamilyTableFeature::GetSequenceNumberIncrement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetSequenceNumberIncrement.html)
- [IFamilyTableFeature::GetSequenceStartNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetSequenceStartNumber.html)
- [IFamilyTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetTableAnnotationCount.html)
- [IFamilyTableFeature::GetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetTableAnnotations.html)
- [IFamilyTableFeature::GetUseAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetUseAllConfigurations.html)
- [IFamilyTableFeature::SetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetConfigurations.html)
- [IFamilyTableFeature::SetFollowConfigTreeOrder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetFollowConfigTreeOrder.html)
- [IFamilyTableFeature::SetSequenceNumberIncrement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetSequenceNumberIncrement.html)
- [IFamilyTableFeature::SetSequenceStartNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetSequenceStartNumber.html)
- [IFamilyTableFeature::SetUseAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetUseAllConfigurations.html)

###### New delegates, methods, and properties

##### DAssemblyDocEvents Handlers

- [DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SolidBodyFolderReorderNotifyEventHandler.html)

##### DDrawingDocEvents Handlers

- [DDrawingDocEvents_ViewPositionChangeNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewPositionChangeNotifyEventHandler.html)

##### DPartDocEvents Handlers

- [DPartDocEvents_SolidBodyFolderReorderNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SolidBodyFolderReorderNotifyEventHandler.html)

##### IBodyFolder Interface

- [IBodyFolder::GetTopLevelFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatureCount.html)
- [IBodyFolder::GetTopLevelFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatures.html)

##### ISheet Interface

- [ISheet::InsertFamilyTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertFamilyTable.html)

##### IRenderMaterial Interface

- [IRenderMaterial::GetDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetDSPBRMaterial.html)
- [IRenderMaterial::HasDSPBRProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HasDSPBRProperties.html)

##### ISldWorks Interface

- [ISldWorks::ShadedEdgeThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShadedEdgeThickness.html)

##### IView Interface

- [IView::SetViewPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetViewPosition.html)

[Back to top](#Top)
