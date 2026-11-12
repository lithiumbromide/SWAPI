---
title: "InsertNetBlend Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertNetBlend"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.html"
---

# InsertNetBlend Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertNetBlend2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNetBlend( _
   ByVal Type As System.Short, _
   ByVal NCurvesDir1 As System.Short, _
   ByVal NCurvesDir2 As System.Short, _
   ByVal HasCenterline As System.Boolean, _
   ByVal TessTolFactor As System.Double, _
   ByVal WantsSolid As System.Boolean, _
   ByVal MergeBody As System.Boolean, _
   ByVal FeatureScope As System.Boolean, _
   ByVal AutoSelect As System.Boolean, _
   ByVal Thin As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThickness As System.Boolean, _
   ByVal ThinSolidType As System.Short, _
   ByVal UseSharedThickness As System.Boolean, _
   ByVal CapEnds As System.Boolean, _
   ByVal EndThickness As System.Double, _
   ByVal AutoFillet As System.Boolean, _
   ByVal FilletRadius As System.Double, _
   ByVal ForceNonRational As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Short
Dim NCurvesDir1 As System.Short
Dim NCurvesDir2 As System.Short
Dim HasCenterline As System.Boolean
Dim TessTolFactor As System.Double
Dim WantsSolid As System.Boolean
Dim MergeBody As System.Boolean
Dim FeatureScope As System.Boolean
Dim AutoSelect As System.Boolean
Dim Thin As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ReverseThickness As System.Boolean
Dim ThinSolidType As System.Short
Dim UseSharedThickness As System.Boolean
Dim CapEnds As System.Boolean
Dim EndThickness As System.Double
Dim AutoFillet As System.Boolean
Dim FilletRadius As System.Double
Dim ForceNonRational As System.Boolean
Dim value As Feature

value = instance.InsertNetBlend(Type, NCurvesDir1, NCurvesDir2, HasCenterline, TessTolFactor, WantsSolid, MergeBody, FeatureScope, AutoSelect, Thin, Thickness1, Thickness2, ReverseThickness, ThinSolidType, UseSharedThickness, CapEnds, EndThickness, AutoFillet, FilletRadius, ForceNonRational)
```

### C#

```csharp
Feature InsertNetBlend(
   System.short Type,
   System.short NCurvesDir1,
   System.short NCurvesDir2,
   System.bool HasCenterline,
   System.double TessTolFactor,
   System.bool WantsSolid,
   System.bool MergeBody,
   System.bool FeatureScope,
   System.bool AutoSelect,
   System.bool Thin,
   System.double Thickness1,
   System.double Thickness2,
   System.bool ReverseThickness,
   System.short ThinSolidType,
   System.bool UseSharedThickness,
   System.bool CapEnds,
   System.double EndThickness,
   System.bool AutoFillet,
   System.double FilletRadius,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
Feature^ InsertNetBlend(
   System.short Type,
   System.short NCurvesDir1,
   System.short NCurvesDir2,
   System.bool HasCenterline,
   System.double TessTolFactor,
   System.bool WantsSolid,
   System.bool MergeBody,
   System.bool FeatureScope,
   System.bool AutoSelect,
   System.bool Thin,
   System.double Thickness1,
   System.double Thickness2,
   System.bool ReverseThickness,
   System.short ThinSolidType,
   System.bool UseSharedThickness,
   System.bool CapEnds,
   System.double EndThickness,
   System.bool AutoFillet,
   System.double FilletRadius,
   System.bool ForceNonRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: - 0 = Base
  - 1 = Boss
  - 2 = Surface
  - 3 = Cut
- `NCurvesDir1`: Number of curves in Direction 1
- `NCurvesDir2`: Number of curves in Direction 2
- `HasCenterline`: True if a centerline exists, false if not
- `TessTolFactor`: Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the value, the more intermediate sections created
- `WantsSolid`: True to create a solid body, false to create a surface body; only valid when Type = 0, 1, or 3
- `MergeBody`: True merges the results in a multibody part, false does not
- `FeatureScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `AutoSelect`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects
- `Thin`: True if this feature is a thin body, false if not
- `Thickness1`: Thickness value for the first direction
- `Thickness2`: Thickness value for the second direction
- `ReverseThickness`: True to reverse the thickness, false to not
- `ThinSolidType`: Thin wall type as defined in [swThinWallType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)
- `UseSharedThickness`: True to use shared thickness, false to not
- `CapEnds`: True to cap the ends, false to not
- `EndThickness`: End cap thickness
- `AutoFillet`: True to fillet the corners automatically, false to not
- `FilletRadius`: Fillet radius when AutoFillet is true
- `ForceNonRational`: True to force the resulting surface to be non-rational, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertNetBlend](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertNetBlend.html).

## Examples

[Insert Boundary Surface Feature (VBA)](Insert_Boundary_Surface_Feature_Example_VB.htm)
[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## Remarks

**Boundary feature**

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the entities for a boundary feature or boundary surface feature. The following table contains valid selection marks for this method and these features.

| Feature | Selection marks |
| --- | --- |
| Boundary | Sketch curves: Direction 1: 8193, 16385, 24577 Direction 2: 8194, 16386, 24578 Faces: Direction 1: 8193, 16385, 24577 Direction 2: 8194, 16386, 24578 Other sketch entities (3D sketch (Unknown/SELOBJGROUP): Direction 1: 12289, 24577 Direction 2: 16386, 28674 |
| Boundary surface | Sketch curves: Direction 1: 1 Direction 2: 2 |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::SetNetBlendCurveData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.html)
[IFeatureManager::SetNetBlendDirectionData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.html)
[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
