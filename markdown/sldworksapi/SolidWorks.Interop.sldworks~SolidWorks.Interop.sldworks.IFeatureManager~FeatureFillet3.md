---
title: "FeatureFillet3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureFillet3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet3.html"
---

# FeatureFillet3 Method (IFeatureManager)

Creates a fillet feature for selected edges and control point references.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillet3( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal R2 As System.Double, _
   ByVal Rho As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal ConicRhoType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal Dist2Arr As System.Object, _
   ByVal RhoArr As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object, _
   ByVal PointDist2Array As System.Object, _
   ByVal PointRhoArray As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim R2 As System.Double
Dim Rho As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim ConicRhoType As System.Integer
Dim Radii As System.Object
Dim Dist2Arr As System.Object
Dim RhoArr As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim PointDist2Array As System.Object
Dim PointRhoArray As System.Object
Dim value As System.Object

value = instance.FeatureFillet3(Options, R1, R2, Rho, Ftyp, OverflowType, ConicRhoType, Radii, Dist2Arr, RhoArr, SetBackDistances, PointRadiusArray, PointDist2Array, PointRhoArray)
```

### C#

```csharp
System.object FeatureFillet3(
   System.int Options,
   System.double R1,
   System.double R2,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.object Radii,
   System.object Dist2Arr,
   System.object RhoArr,
   System.object SetBackDistances,
   System.object PointRadiusArray,
   System.object PointDist2Array,
   System.object PointRhoArray
)
```

### C++/CLI

```cpp
System.Object^ FeatureFillet3(
   System.int Options,
   System.double R1,
   System.double R2,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.Object^ Radii,
   System.Object^ Dist2Arr,
   System.Object^ RhoArr,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray,
   System.Object^ PointDist2Array,
   System.Object^ PointRhoArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Feature fillet options as defined in [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html) (see **Remarks**)
- `R1`: Uniform radius of the symmetric fillet; valid only if:

  - Ftyp != swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletUniformRadius

  - or -

  Distance 1 radius of the asymmetric fillet; valid only if:

  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric
- `R2`: Distance 2 radius of the asymmetric fillet; valid only if:

  - Ftyp != swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric
- `Rho`: Value that determines the conic rho or radius of the fillet:

  - Ftyp != swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRho
  - Conic radius value, if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRadius

  (see **Remarks**)
- `Ftyp`: Type of fillet as defined in [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html) (see **Remarks**)
- `OverflowType`: Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html) (see **Remarks**)
- `ConicRhoType`: Fillet cross-section profile as defined in [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html); valid only if Options does not include swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous (see **Remarks**)
- `Radii`: Array containing the radii for selected edges for the symmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius

  - or -

  Array containing the Distance 1 radii for selected edges for the asymmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric

  (see **Remarks**)
- `Dist2Arr`: Array containing the Distance 2 radii for selected edges for the asymmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric

  (see **Remarks**)
- `RhoArr`: Array of conic rho or radius values for the specified ConicRhoType for selected edges for the variable radius fillet; valid only if:

  - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRho
  - Conic radius value, if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRadius
  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius

  (see **Remarks**)
- `SetBackDistances`: Array assigning setback distances on edges meeting at a selected fillet corner (see **Remarks**)
- `PointRadiusArray`: Array containing control point radii along the lengths of the selected edges for the symmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletVarRadiusType

  - or -

  Array containing Distance 1 control point radii along the lengths of the selected edges for the asymmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric

  (see **Remarks**)
- `PointDist2Array`: Array containing Distance 2 control point radii along the lengths of the selected edges for the asymmetric variable radius fillet; valid only if:

  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius
  - Options include swFeatureFilletOptions_e.swFeatureFilletAsymmetric

  (see **Remarks**)
- `PointRhoArray`: Array of conic rho or radius values for the specified ConicRhoType at various control points along the lengths of the selected edges for the variable radius fillet; valid only if:

  - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRho
  - Conic radius value, if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRadius
  - Ftyp = swFeatureFilletType_e.swFeatureFilletType_VariableRadius

  (see **Remarks**)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureFillet3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureFillet3.html).

## Examples

[Create Variable Radius Asymmetric Elliptical Fillet (VBA)](Create_Asymmetric_Elliptic_Fillets_Example_VB.htm)
[Create Variable Radius Asymmetric Elliptical Fillet (VB.NET)](Create_Asymmetric_Elliptic_Fillets_Example_VBNET.htm)
[Create Variable Radius Asymmetric Elliptical Fillet (C#)](Create_Asymmetric_Elliptic_Fillets_Example_CSharp.htm)

## Remarks

As of SOLIDWORKS 2020, this method is obsolete for creating:

- constant radius fillets
- offset face chamfers
- face fillets
- face-face chamfers
- full round fillets
- partial fillets
- partial chamfers

To create the fillet/chamfers above, use [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html), IPartialEdgeFilletData, and [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html).

All of the parameter arrays of this method scale with the number of selected edges to fillet. Take care to populate and order the arrays meaningfully, or this method will fail.

If the conic rho values of Rho, RhoArray, or PointRhoArray are not in the valid range, then this method replaces them with the closest value in the valid range. For example, 0.01 is replaced by 0.05, and 0.99 is replaced by 0.95.

| To create... | You must... |
| --- | --- |
| Variable radius fillets | Call IModelDocExtension::SelectByID2 with Mark = 1 to select the edges to fillet. Call IModelDocExtension::SelectByID2 with Mark = 256 to select the control point references along the lengths of the selected edges; select one control point reference for each radius in PointRadiusArray. Specify Ftyp with swFeatureFilletType_e.swFeatureFilletType_VariableRadius. (Optional) Specify OverflowType. (Optional) Include swFeatureFilletOptions_e.swFeatureFilletVarRadiusType in Options. (Optional) Include swFeatureFilletOptions_e.swFeatureFilletPropagate in Options. (Optional) Include swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous in Options. (Optional) If Options does not include swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous, then include swFeatureFilletOptions_e.swFeatureFilletCornerType in Options. (Optional) Include swFeatureFilletOptions_e.swFeatureFilletKeepFeatures in Options. If a symmetric fillet : - If Options does not include swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous, then specify ConicRhoType with swFeatureProfileType_e.swFeatureFilletCircular, swFeatureFilletConicRadius, or swFeatureFilletConicRho. - Specify Radii. - If ConicRhoType is not swFeatureFilletProfileType_e.swFeatureFilletCircular, then specify RhoArr with conic rho or radius values. - Specify PointRadiusArray with multiple control point radii, one radius for each control point reference selected in step 2. - If ConicRhoType is not swFeatureFilletProfileType_e.swFeatureFilletCircular, then specify PointRhoArray with conic rho or radius values. If an asymmetric fillet : - If Options does not include swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous, then specify ConicRhoType with swFeatureProfileType_e.swFeatureFilletCircular or swFeatureFilletConicRho. - Include swFeatureFilletOptions_e.swFeatureFilletAsymmetric in Options. - Specify Radii with the Distance 1 radii. - Specify Dist2Array with the Distance 2 radii. - If ConicRhoType is not swFeatureFilletProfileType_e.swFeatureFilletCircular, then specify RhoArr with conic rho or radius values. - Specify PointRadiusArray, one Distance 1 radius for each control point reference selected in step 2. - Specify PointDist2Array, one Distance 2 radius for each control point reference selected in step 2. - If ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRho, specify PointRhoArray with the conic rho values. |
| Setback fillets | Follow the instructions above to create a variable radius fillet. Call IModelDocExtension::SelectByID2 with Mark = 0 to select the vertex of the fillet corner whose setback parameters you want to set. Specify SetBackDistances and call this method. - or - Call this method. Use the setback methods on IVariableFilletFeatureData2 to set the setback distances from setback vertices of multiple fillet corners. |

For more information, read the **Variable Size Fillets** topic in the SOLIDWORKS Design user-interface help.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.html)
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
