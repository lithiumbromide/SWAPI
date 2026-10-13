---
title: "IBaseFlangeFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html"
---

# IBaseFlangeFeatureData Interface

Allows access to a sheet metal base flange feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBaseFlangeFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
```

### C#

```csharp
public interface IBaseFlangeFeatureData
```

### C++/CLI

```cpp
public interface class IBaseFlangeFeatureData
```

## VBA Syntax

See [BaseFlangeFeatureData](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData.html).

## Examples

'VBA

'===========================================================
'Preconditions:
'1. Ensure the specified part template exists.
'2. Open the Immediate window.
'
'Postconditions:
'1. Creates a flange profile sketch.
'2. Creates **Base-Flange1** in the FeatureManager design tree.
'3. Inspect the Immediate window, graphics area,
' and FeatureManager design tree.
'==================================================
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim swPart As PartDoc
Dim swModel As SldWorks.ModelDoc2
Dim swSKFeat As SldWorks.Feature
Dim skSegment As SldWorks.SketchSegment
Dim swBaseFlangeFeat As SldWorks.BaseFlangeFeatureData
Dim baseFlangeFeatData As SldWorks.BaseFlangeFeatureData
Dim cba As SldWorks.CustomBendAllowance
Dim var As Variant
Dim parent As SldWorks.Feature
Dim SHFeat As SldWorks.Feature
Dim smFeatData As SldWorks.SheetMetalFeatureData
Dim cba1 As SldWorks.CustomBendAllowance
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

Dim swSheetWidth As Double
swSheetWidth = 0
Dim swSheetHeight As Double
swSheetHeight = 0

Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)
Set swPart = Part
Set swModel = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByID2("Top", "PLANE", -5.98881514598713E-02, 3.93749830258702E-02, 4.85137895479469E-03, False, 0, Nothing, 0)
Part.SketchManager.InsertSketch True
Part.ClearSelection2 True

Set skSegment = Part.SketchManager.CreateLine(-0.140779, 0.050824, 0#, -0.106481, -0.06735, 0#)
Set skSegment = Part.SketchManager.CreateLine(-0.106481, -0.06735, 0#, 0.084966, -0.049265, 0#)
Set skSegment = Part.SketchManager.CreateLine(0.084966, -0.049265, 0#, 0.143274, 0.063608, 0#)
Part.ClearSelection2 True
Part.SketchManager.InsertSketch True

Set swSKFeat = swModel.SelectionManager.GetSelectedObject6(1, -1)
Debug.Print "Flange profile name : " & swSKFeat.Name & " and type : " & swSKFeat.GetTypeName2

Set swBaseFlangeFeat = swModel.FeatureManager.**CreateDefinition**(swFmBaseFlange)

Set cba = swBaseFlangeFeat.**GetCustomBendAllowance**()

cba.**Type** = swBendAllowanceDirect
cba.**BendAllowance** = 0.05

swBaseFlangeFeat.**D1EndConditionType** = 1
swBaseFlangeFeat.**D1EndConditionDistance** = 0.02
swBaseFlangeFeat.**ReverseDirection** = True
swBaseFlangeFeat.**OffsetDirections** = 2
swBaseFlangeFeat.**D2EndConditionType** = 1
swBaseFlangeFeat.**D2EndConditionDistance** = 0.05
swBaseFlangeFeat.**OverrideDefaultSheetMetalParameters** = True
swBaseFlangeFeat.**Thickness** = 0.035

'Initialize the base flange feature
'Initialize(
'UseMaterialSheetMetalParameters=False,
'UseDefaultBendAllowance=False,
'CustomBendAllowance,
'UseDefaultBendRelief=False,
'ReliefType=swSheetMetalReliefTypes_e.swSheetMetalReliefRectangular,
'UseReliefRatio=True,
'ReliefRatio=0.8m,
'ReliefWidth,
'ReliefDepth)

Call swBaseFlangeFeat.**Initialize**(False, False, cba, False, swSheetMetalReliefRectangular, True, 0.8, 0#, 0#)

Set SHFeat = swModel.FeatureManager.**CreateFeature**(swBaseFlangeFeat)

Set baseFlangeFeatData = SHFeat.**GetDefinition**()

Debug.Print "Use material sheet metal parameters? " & baseFlangeFeatData.**UseMaterialSheetMetalParameters**
Debug.Print "Use default bend allowance? " & baseFlangeFeatData.**UseDefaultBendAllowance**
Debug.Print "Use default bend relief? " & baseFlangeFeatData.**UseDefaultBendRelief**
Debug.Print "Use relief ratio? " & baseFlangeFeatData.**UseReliefRatio**
Debug.Print "Relief type as defined by swSheetMetalReliefTypes_e: " & baseFlangeFeatData.**ReliefType**
Debug.Print "Relief width: " & baseFlangeFeatData.**ReliefWidth**
Debug.Print "Relief depth: " & baseFlangeFeatData.**ReliefDepth**
Debug.Print "Relief ratio: " & baseFlangeFeatData.**ReliefRatio**

'Modify the relief ratio and override default AutoRelief in the parent sheet metal feature
var = SHFeat.GetParents()
Set parent = var(1)
Debug.Print "Parent type: " & parent.GetTypeName2()

Set smFeatData = parent.**GetDefinition**()

Set cba1 = smFeatData.**GetCustomBendAllowance**()

Debug.Print "Custom bend allowance type as defined in swBendAllowanceTypes_e: " & cba1.**Type**
Debug.Print "Bend allowance: " & cba1.**BendAllowance**
Debug.Print "Result code for override of AutoRelief as defined by swSheetMetalModifierError_e: " & smFeatData.**SetOverrideDefaultParameter2**(swSheetMetalOverrideDefaultParameters_AutoRelief, True)
smFeatData.**ReliefRatio** = 0.7

Debug.Print "Base flange successfully modified? " & parent.**ModifyDefinition**(smFeatData, swModel, Nothing)
Debug.Print "Base flange feature name : " & SHFeat.Name & " and type : " & SHFeat.GetTypeName2

End Sub

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)
[Create Base Flange Feature (VB.NET)](Create_Base_Flange_Feature_Example_VBNET.htm)
[Create Base Flange Feature (C#)](Create_Base_Flange_Feature_Example_CSharp.htm)

## Remarks

For general information about sheet metal base flanges, see the **SOLIDWORKS Design user-interface help > Sheet Metal > Using Sheet Metal Tools > Base Flange/Tab > Base Flange PropertyManager** topic.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[BaseFlangeFeatureData](SWObjectModel.pdf#BaseFlangeFeatureData)

## See Also

[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
