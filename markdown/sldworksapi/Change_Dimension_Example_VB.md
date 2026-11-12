---
title: "Change Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Example_VB.htm"
---

# Change Dimension Example (VBA)

This example shows how to change a dimension value in a model.

#### NOTE: Most of the SOLIDWORKS API functions operate in meters. Thus, if you pass in XValue_Passed = 2.0 and your model units are millimeters, then it appears as a 2000.0 in the model. If you need to determine the units used in the model, you can use the IModelDoc2::LengthUnit property and perform the appropriate conversion.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Changes the specified dimension parameter of the selected feature.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeature As SldWorks.Feature
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swDim As SldWorks.Dimension
Dim fileName As String
Dim boolstatus As Boolean
Dim errors As Long
Dim warnings As Long
Dim val As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    boolstatus = swModel.Extension.SelectByID2("LocalCirPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionManager = swModel.SelectionManager
    Set swFeature = swSelectionManager.GetSelectedObject6(1, -1)
```

```
    Set swDim = swFeature.Parameter("D3")
```

```
    ' Get D3 of LocalCirPattern1
    Debug.Print "D3@LocalCirPattern1 is " & swFeature.Parameter("D3").SystemValue & " before changing it."
```

```
    ' Change D3 of LocalCirPattern1 from 360 degrees to 270 degrees (4.72 radians)
    errors = swDim.SetSystemValue3(4.72, swSetValue_InThisConfiguration, Empty)
```

```
    swModel.EditRebuild3
```

```
    Debug.Print "D3@LocalCirPattern1 is " & swFeature.Parameter("D3").SystemValue & " after changing it."
```

```
End Sub
```
