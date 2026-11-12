---
title: "ISimpleFilletFeatureData2 Interface"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html"
---

# ISimpleFilletFeatureData2 Interface

Allows access to a simple fillet feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISimpleFilletFeatureData2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
```

### C#

```csharp
public interface ISimpleFilletFeatureData2
```

### C++/CLI

```cpp
public interface class ISimpleFilletFeatureData2
```

## VBA Syntax

See [SimpleFilletFeatureData2](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2.html).

## Examples

'VBA

'Preconditions: Open `Public_documents`**\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\cube.sldprt**.

'Postconditions:

'1. Creates an asymmetric face fillet between the selected faces.

'2. Inspect the graphics area.

'NOTE: Because the model is used elsewhere, do not save changes to it.

'===============================================================

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim swFeat As SldWorks.Feature
Dim swFilletData As SldWorks.SimpleFilletFeatureData2
Dim swFeatDataObj As Object
Dim boolstatus As Boolean

Option Explicit

Sub main()
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
Set swFeatMgr = swModel.FeatureManager

' Create the fillet feature data object
Set swFeatDataObj = swFeatMgr.**CreateDefinition**(swFmFillet)
Set swFilletData = swFeatDataObj

' Initialize the fillet feature data object with a simple fillet type
swFilletData.**Initialize** swFaceFillet

' Select adjacent faces using Marks 2 and 4
boolstatus = swModel.Extension.SelectByRay(-8.1276449166694E-03, 7.23380744250335E-02, 5.97881679346983E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.27210389793168E-03, 2, False, 2, 0)
boolstatus = swModel.Extension.SelectByRay(5.01369231146214E-02, 6.23282644744449E-03, 5.13547742943388E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.27210389793168E-03, 2, True, 4, 0)
swFilletData.**AsymmetricFillet** = True
swFilletData.**DefaultRadius** = 0.01
swFilletData.**DefaultDistance** = 0.02

' Narrow the fillet type by specifying the feature fillet profile type
swFilletData.**ConicTypeForCrossSectionProfile** = swFeatureFilletCircular

' Create the fillet feature
Set swFeat = swFeatMgr.**CreateFeature**(swFilletData)
End Sub

## Examples

[Get Data for Fillet Feature (VBA)](Get_Data_for_Simple_Fillet_Example_VB.htm)
[Get Data for Fillet Feature (VB.NET)](Get_Data_for_Simple_Fillet_Example_VBNET.htm)
[Get Data for Fillet Feature (C#)](Get_Data_for_Simple_Fillet_Example_CSharp.htm)

## Remarks

To create a simple fillet feature:

1. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), passing Type = [swFeatureNameID_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html).swFmFillet, to create an instance of ISimpleFilletFeatureData2.
2. Initialize the fillet/chamfer to a simple fillet type as follows:

  | For... | Call ISimpleFilletFeatureData2::Initialize , passing FilletType = swSimpleFilletType_e ... |
  | --- | --- |
  | Constant radius fillet Offset face chamfer | swConstRadiusFillet |
  | Face fillet Face-face chamfer | swFaceFillet |
  | Full round fillet | swFullRoundFillet |
3. Complete the fillet/chamfer type specification by specifying a feature fillet profile type:

  | For... | Set ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile to swFeatureFilletProfileType_e .... |
  | --- | --- |
  | Constant radius fillet | swFeatureFilletCircular (symmetric or asymmetric) swFeatureFilletConicRho (symmetric or asymmetric) swFeatureFilletConicRadius (symmetric) |
  | Offset face chamfer | swFeatureFilletConicRhoZeroChamfer |
  | Face fillet | swFeatureFilletCircular (symmetric, asymmetric, chord width, or hold line) swFeatureFilletConicRho (symmetric, asymmetric, or chord width) swFeatureFilletConicRadius (symmetric or chord width) |
  | Face-face chamfer | swFeatureFilletConicRhoZeroChamfer |
  | Full round fillet | swFeatureFilletCircular |
4. Specify other ISimpleFilletFeatureData2 properties as follows:.

  | To create... | You must... |
  | --- | --- |
  | Constant radius fillet/offset face chamfer | Call IModelDocExtension::SelectByID2 with Mark = 1 to select the edges, faces, features, or loops to fillet. Set ISimpleFilletFeatureData2::OverflowType . (Optional) For both fillets and chamfers, set ISimpleFilletFeatureData2::KeepFeatures and ISimpleFilletFeatureData2::PropagateToTangentFaces . (Optional) For fillets only, set ISimpleFilletFeatureData2::RoundCorners , ISimpleFilletFeatureData2::ConstantWidth , and ISimpleFilletFeatureData2::CurvatureContinuous (if set to true, then ISimpleFilletFeatureData2::RoundCorners and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile are not valid). If a symmetric fillet/chamfer : - For fillets or chamfers, set ISimpleFilletFeatureData2::DefaultRadius to a default fillet radius or chamfer offset distance. - For fillets, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletCircular, then you can set ISimpleFilletFeatureData2::IsMultipleRadius . If MultipleRadius is set to true, then you can call ISimpleFilletFeatureData2::SetRadius to specify multiple edge radii. If ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho value between 0.05 and 0.95, inclusive, or a conic radius value, respectively. - For chamfers, if ISimpleFilletFeatureData2::IsMultipleRadius is set to true, then you can call ISimpleFilletFeatureData2::SetRadius to set multiple offset distances. If an asymmetric fillet/chamfer : - Set ISimpleFilletFeatureData2::AsymmetricFillet . - Set ISimpleFilletFeatureData2::DefaultRadius to the fillet Distance 1 radius or chamfer Offset Distance 1. - Set ISimpleFilletFeatureData2::DefaultDistance to the fillet Distance 2 radius or chamfer Offset Distance 2. - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho value between 0.05 and 0.95, inclusive. For more information, see the Constant Size Fillets and Chamfer PropertyManager topics in the SOLIDWORKS Design user-interface help. |
  | Face fillet/face-face chamfer | Call IModelDocExtension::SelectByID2 with: - Mark = 2 to select Face Set 1. - Mark = 4 to select Face Set 2. (Optional) For both fillets and chamfers, set ISimpleFilletFeatureData2::PropagateToTangentFaces and ISimpleFilletFeatureData2::HelpPoint . (Optional) For fillets only, set ISimpleFilletFeatureData2::CurvatureContinuous (if set to true, then ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is not valid). If a symmetric fillet/chamfer : - Set ISimpleFilletFeatureData2::DefaultRadius for the fillet radius or the chamfer offset distance. - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho or conic radius value. If a chord width fillet/chamfer : - Set ISimpleFilletFeatureData2::DefaultRadius to set the chord width. - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho or conic radius value. If an asymmetric fillet/chamfer : - Set ISimpleFilletFeatureData2::AsymmetricFillet. - Set ISimpleFilletFeatureData2::DefaultRadius to the fillet Distance 1 radius or the chamfer Offset Distance 1. - Set ISimpleFilletFeatureData2::DefaultDistance to the fillet Distance 2 radius or the chamfer Offset Distance 2. - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho value. If a hold line fillet/chamfer : - Call IModelDocExtension::SelectByID2 with Mark = 8 to select the hold line edges. - Set ISimpleFilletFeatureData2::HoldLines to the hold line edges. For more information, see the Face Fillets and Chamfer PropertyManager topics in the SOLIDWORKS Design user-interface help. |
  | Full round fillet | Call IModelDocExtension::SelectByID2 with: - Mark = 2 to select Face Set 1. - Mark = 512 to select Center Face Set. - Mark = 4 to select Face Set 2. (Optional) Set ISimpleFilletFeatureData2::PropagateToTangentFaces. For more information, see the Full Round Fillets topic in the SOLIDWORKS Design user-interface help. |
  | Setback fillet | Follow the instructions above to create a constant radius fillet. Use the setback methods on ISimpleFilletFeatureData2 to set the setback distances from setback vertices of fillet corners. For more information, see the Constant Size Fillets topic in the SOLIDWORKS Design user-interface help. |
  | Partial edge fillet/chamfer | Follow the instructions above to create a constant radius fillet or offset face chamfer. Set ISimpleFilletFeatureData2::EnablePartialEdgeParameters to true. Call ISimpleFilletFeatureData2::GetPartialEdgeFilletData . Set other properties of IPartialEdgeFilletData as required. Call ISimpleFilletFeatureData2::SetPartialEdgeFilletData , passing in the IPartialEdgeFilletData populated in step d. Repeat steps c-e for each edge to partially fillet. For more information, see the Constant Size Fillets and Chamfer PropertyManager topics in the SOLIDWORKS Design user-interface help. |
5. Create the fillet/chamfer feature by calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html).

For more information about fillets, see the **Fillets** topic in the SOLIDWORKS Design user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

IFeatureManager::CreateDefinition

## Access Diagram

[SimpleFilletFeatureData2](SWObjectModel.pdf#SimpleFilletFeatureData2)

## See Also

[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.html)
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
