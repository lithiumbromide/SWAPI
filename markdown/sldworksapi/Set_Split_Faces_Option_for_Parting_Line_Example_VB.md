---
title: "Set Options for Parting Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Split_Faces_Option_for_Parting_Line_Example_VB.htm"
---

# Set Options for Parting Line Example (VBA)

This example shows how to set the split faces and core/cavity split options for a parting line.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a part document containing a parting line
'    feature.
' 2. Select the parting line feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sets the split faces and core/cavity split
'    options.
' 2. Examine the Immediate window.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swPartingLine As SldWorks.PartingLineFeatureData
    Dim i As Long
    Dim bRet As Boolean
    Dim SplitFaceOption As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swPartingLine = swFeat.GetDefinition
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    Debug.Print "    " & swPartingLine.Angle
    Debug.Print "    Split faces = " & swPartingLine.SplitFaces
    Debug.Print "    Core/cavity split = " & swPartingLine.CoreCavitySplit
```

```
    SplitFaceOption = swPartingLine.SplitFacesOption
    swPartingLine.SplitFacesOption = swSplitFacesAtPlusMinusDraftTransition
    Debug.Print "    Split faces option = " & swPartingLine.SplitFacesOption
```

```
    bRet = swPartingLine.AccessSelections(swModel, Nothing): Debug.Assert bRet
```

```
    swPartingLine.SplitFaces = True
    swPartingLine.CoreCavitySplit = True
```

```
    Debug.Print " "
    Debug.Print "    Split faces = " & swPartingLine.SplitFaces
    Debug.Print "    Core/cavity split = " & swPartingLine.CoreCavitySplit
    swPartingLine.SplitFacesOption = swSplitFacesAtSpecifiedAngle
    Debug.Print "    Split faces option = " & swPartingLine.SplitFacesOption
```

```
    bRet = swFeat.ModifyDefinition(swPartingLine, swModel, Nothing): Debug.Assert bRet
```

```
End Sub
```
