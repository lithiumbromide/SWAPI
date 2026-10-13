---
title: "FeatureFillet Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureFillet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.html"
---

# FeatureFillet Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureFillet2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillet( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim Radii As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim value As System.Object

value = instance.FeatureFillet(Options, R1, Ftyp, OverflowType, Radii, SetBackDistances, PointRadiusArray)
```

### C#

```csharp
System.object FeatureFillet(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.object Radii,
   System.object SetBackDistances,
   System.object PointRadiusArray
)
```

### C++/CLI

```cpp
System.Object^ FeatureFillet(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.Object^ Radii,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Feature fillet options as defined in [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)
- `R1`: Radius; valid only if:

  - Ftyp is not [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
  - Options is set with [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius
- `Ftyp`: Type of fillet as defined in [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html) (see **Remarks**)
- `OverflowType`: Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)
- `Radii`: Array containing the radii for the variable radius fillet; valid only if:

  - Ftyp is set to [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
  - Options is set with [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletVarRadiusType
  - Options is not set with [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius
- `SetBackDistances`: Array containing setback distances for the fillet along the edge
- `PointRadiusArray`: Array containing control point radii at various points along the length of the edge; valid only if Ftyp is set to [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureFillet](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureFillet.html).

## Remarks

| Before calling this method to create... | Do this... |
| --- | --- |
| Simple fillets | Call IModelDocExtension::SelectByID2 with Mark = 1 to select the edges to fillet. Specify Ftyp with swFeatureFilletType_e .swFeatureFilletType_Simple. |
| Face blend fillets | Call IModelDocExtension::SelectByID2 with: Mark = 2 to select the first set of faces. Mark = 4 to select the second set of faces. Specify Ftyp with swFeatureFilletType_e .swFeatureFilletType_Face. |
| Variable radius fillets | Call IModelDocExtension::SelectByID2 with Mark = 1 to select the edges to fillet. Call IModelDocExtension::SelectByID2 with Mark = 256 to select the control point references along the length of the selected edge, one control point reference for each radius in PointRadiusArray. Specify Ftyp with swFeatureFilletType_e .swFeatureFilletType_VariableRadius. Specify multiple radii in Radii. Specify multiple control point radii in PointRadiusArray. Do not set the Options parameter to swFeatureFilletOptions_e .swFilletUniformRadius. |
| Full-round fillets | Call IModelDocExtension::SelectByID2 with: Mark = 2 to select the first set of side faces. Mark = 512 to select the set of center faces. Mark = 4 to select the second set of side faces. Specify Ftyp with swFeatureFilletType_e .swFeatureFilletType_FullRound. |
| Setback fillets | See the SOLIDWORKS Help for details. |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[IFeatureManager::IFeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
