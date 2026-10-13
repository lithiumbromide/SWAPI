---
title: "InsertSheetMetalBaseFlange2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalBaseFlange2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange2.html"
---

# InsertSheetMetalBaseFlange2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalBaseFlange2( _
   ByVal Thickness As System.Double, _
   ByVal ThickenDir As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal ExtrudeDist1 As System.Double, _
   ByVal ExtrudeDist2 As System.Double, _
   ByVal FlipExtruDir As System.Boolean, _
   ByVal EndCondition1 As System.Integer, _
   ByVal EndCondition2 As System.Integer, _
   ByVal DirToUse As System.Integer, _
   ByVal PCBA As CustomBendAllowance, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double, _
   ByVal ReliefRatio As System.Double, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim ThickenDir As System.Boolean
Dim Radius As System.Double
Dim ExtrudeDist1 As System.Double
Dim ExtrudeDist2 As System.Double
Dim FlipExtruDir As System.Boolean
Dim EndCondition1 As System.Integer
Dim EndCondition2 As System.Integer
Dim DirToUse As System.Integer
Dim PCBA As CustomBendAllowance
Dim UseDefaultRelief As System.Boolean
Dim ReliefType As System.Integer
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim ReliefRatio As System.Double
Dim UseReliefRatio As System.Boolean
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature

value = instance.InsertSheetMetalBaseFlange2(Thickness, ThickenDir, Radius, ExtrudeDist1, ExtrudeDist2, FlipExtruDir, EndCondition1, EndCondition2, DirToUse, PCBA, UseDefaultRelief, ReliefType, ReliefWidth, ReliefDepth, ReliefRatio, UseReliefRatio, Merge, UseFeatScope, UseAutoSelect)
```

### C#

```csharp
Feature InsertSheetMetalBaseFlange2(
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse,
   CustomBendAllowance PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.double ReliefRatio,
   System.bool UseReliefRatio,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalBaseFlange2(
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse,
   CustomBendAllowance^ PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.double ReliefRatio,
   System.bool UseReliefRatio,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Wall thickness of the sheet metal feature
- `ThickenDir`: Direction to thicken the sheet metal
- `Radius`: Global bend radius to insert at the corners
- `ExtrudeDist1`: Distance of the sheet metal extrusion for the Direction 1
- `ExtrudeDist2`: Distance of the sheet metal extrusion for the Direction 2
- `FlipExtruDir`: True to reverse the direction of the extrude, false to not
- `EndCondition1`: End condition for first extrude distance
- `EndCondition2`: End condition for second extrude distance
- `DirToUse`: End condition type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)
- `PCBA`: Pointer to the [custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) object
- `UseDefaultRelief`: True to use the default relief, false to not
- `ReliefType`: Relief type as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)
- `ReliefWidth`: Width of the relief
- `ReliefDepth`: Depth of the relief
- `ReliefRatio`: Value for the relief ratio
- `UseReliefRatio`: True to use the relief ratio, false to not
- `Merge`: True to connect bodies into a single sheet metal body; false to not
- `UseFeatScope`: True to use selected bodies, false to use all bodies
- `UseAutoSelect`: True to auto select bodies (see **Remarks**)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSheetMetalBaseFlange2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalBaseFlange2.html).

## Examples

[Insert Sheet Metal Base Flange (VBA)](Insert_Sheet_Metal_Base_Flange_Example_VB.htm)
[Insert Sheet Metal Base Flange (VB.NET)](Insert_Sheet_Metal_Base_Flange_Example_VBNET.htm)
[Insert Sheet Metal Base Flange (C#)](Insert_Sheet_Metal_Base_Flange_Example_CSharp.htm)

## Remarks

When UseAutoSelect is set to false and bodies are selected using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) or other select methods, use selection mark 8 for the bodies.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
