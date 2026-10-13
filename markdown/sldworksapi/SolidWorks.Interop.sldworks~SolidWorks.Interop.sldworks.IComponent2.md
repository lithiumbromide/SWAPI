---
title: "IComponent2 Interface"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html"
---

# IComponent2 Interface

Allows access to the components within assemblies.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IComponent2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
```

### C#

```csharp
public interface IComponent2
```

### C++/CLI

```cpp
public interface class IComponent2
```

## VBA Syntax

See [Component2](ms-its:sldworksapivb6.chm::/sldworks~Component2.html).

## Examples

[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)
[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)
[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)
[Get Model Textures (VBA)](Get_Model_Texture_Example_VB.htm)
[Get Model Textures (VB.NET)](Get_Model_Texture_Example_VBNET.htm)
[Get Model Textures (C#)](Get_Model_Texture_Example_CSharp.htm)
[Get Model Material Property Values (VBA)](Get_Model_Material_Property_Values_Example_VB.htm)
[Get Model Material Property Values (VB.NET)](Get_Model_Material_Property_Values_Example_VBNET.htm)
[Get Model Material Property Values (C#)](Get_Model_Material_Property_Values_Example_CSharp.htm)
[Get Referenced Display State (VBA)](Get_Referenced_Display_State_Example_VB.htm)
[Get Referenced Display State (VB.NET)](Get_Referenced_Display_State_Example_VBNET.htm)
[Get Referenced Display State (C#)](Get_Referenced_Display_State_Example_CSharp.htm)

## Remarks

Use this interface to traverse assemblies.

Information returned from the methods and properties of this interface is based on the current configuration and might vary if the user displays a different configuration.

## Accessors

[IAssemblyDoc::AddComponents3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponents3.html) and [IAssemblyDoc::IAddComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IAddComponents2.html)

[IAssemblyDoc::AddComponent5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent5.html)

[IAssemblyDoc::AddPLMComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPLMComponent.html)

[IAssemblyDoc::GetComponentByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html)

[IAssemblyDoc::GetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetComponents.html) and [IAssemblyDoc::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetComponents.html)

[IAssemblyDoc::GetComponentByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetComponentByName.html)

[IAssemblyDoc::GetEditTargetComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.html)

[IAssemblyDoc::GetFeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html) and [IAssemblyDoc::IGetFeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html)

[IAssemblyDoc::GetVisibleComponentsInView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInView.html) and [IAssemblyDoc::IGetVisibleComponentsInView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.html)

[IAssemblyDoc::InsertEnvelope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~InsertEnvelope.html)

[IAssemblyDoc::MirrorComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~MirrorComponents2.html)

[IAssemblyDoc::ToolsCheckInterference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html) and [IAssemblyDoc::IToolsCheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)

[IAttribute::GetComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetComponent.html) and [IAttribute::IGetComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~IGetComponent2.html)

[IBomTableAnnotation::GetComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetComponents2.html) and [IBomTableAnnotation::IGetComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html)

[ICavityFeatureData::Components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~Components.html)

[ICavityFeatureData::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~IGetComponents.html)

[IChainPatternFeatureData::Group1PatternComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.html)

[IChainPatternFeatureData::Group2PatternComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.html)

[IClearanceResult::ComponentsOrFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ComponentsOrFaces.html)

[IClearanceVerificationMgr::GetComponentsOrFacesToCheck](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetComponentsOrFacesToCheck.html)

[ICollision::GetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~GetComponents.html)

[ICollisionDetectionGroup::GetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~GetComponents.html)

[IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html) and [IComponent2::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetChildren.html)

[IComponent2::GetParent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetParent.html)

[IConfiguration::GetDisplayStateComponentProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.html)

[IConfiguration::GetDisplayStateComponentVisibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.html)

[IConfiguration::GetRootComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent3.html)

[IDrawingComponent::Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~Component.html)

[IEntity::GetComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~GetComponent.html) and [IEntity::IGetComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~IGetComponent2.html)

[IEnumComponents2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2~Next.html)

[IExplodeStep::GetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent.html) and [IExplodeStep::IGetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponent.html)

[IExplodeStep::GetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html)

[IHoleSeriesFeatureData2::GetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetComponents.html) and [IHoleSeriesFeatureData2::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetComponents.html)

[IInterference::Components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference~Components.html) and [IInterference::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference~IGetComponents.html)

[IInterferenceDetectionMgr::GetComponentsAndTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.html)

[IInterferenceDetectionMgr::GetInterferenceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html) and [IInterferenceDetectionMgr::IGetInterferenceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)

[IJoinFeatureData::IGetJoinedParts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.html)

[IJoinFeatureData::JoinedParts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJoinFeatureData~JoinedParts.html)

[ILinearCouplerMateFeatureData::ReferenceComponent1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~ReferenceComponent1.html)

[ILinearCouplerMateFeatureData::ReferenceComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~ReferenceComponent2.html)

[ILocalCurvePatternFeatureData::PatternComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~PatternComponentArray.html)

[ILocalSketchPatternFeatureData::PatternComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalSketchPatternFeatureData~PatternComponentArray.html)

[IMassProperty2::SelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.html)

[IMateEntity2::ReferenceComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateEntity2~ReferenceComponent.html)

[IMateInPlace::Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateInPlace~Component.html)

[IMateLoadReference::Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference~Component.html)

[IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html)

[IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html)

[ISectionViewData::SelectiveSectioningList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.html)

[ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html)

[ISelectionMgr::GetSelectedObjectsComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)

[ISimulationSpringFeatureData::BaseComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~BaseComponent.html)

[IView::GetVisibleComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleComponents.html) and [IView::IGetVisibleComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetVisibleComponents.html)

## Access Diagram

[Component2](SWObjectModel.pdf#Component2)

## See Also

[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html)
