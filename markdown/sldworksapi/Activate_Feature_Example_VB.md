---
title: "Activate Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Feature_Example_VB.htm"
---

# Activate Feature Example (VBA)

This example shows how to show the dimensions of the selected feature by activating the feature.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select the feature for which you want to show
'    its dimensions.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Displays the selected feature's dimensions.
' 2. Examine the graphics area and Immediate window.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFeat                  As SldWorks.Feature
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ActivateSelectedFeature
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Feature = " + swFeat.Name + " [" + swFeat.GetTypeName + "]"
```

```
End Sub
```
