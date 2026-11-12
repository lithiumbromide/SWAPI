---
title: "Get Number of Bodies in Save Bodies Feature (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Bodies_in_Save_Bodies_Feature_Example_VB.htm"
---

# Get Number of Bodies in Save Bodies Feature (VBA)

This example shows how to get the number of bodies in a Save Bodies feature.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part that contains a Save Bodies feature.
' 2. Select the Save Bodies feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of bodies in the Save Bodies feature.
' 2. Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swSaveBodyFeat As SldWorks.SaveBodyFeatureData
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSaveBodyFeat = swFeat.GetDefinition
    swSaveBodyFeat.AccessSelections swModel, Nothing
    Dim bodyCount As Long
    bodyCount = swSaveBodyFeat.GetSaveBodiesCount
    Debug.Print ("Number of bodies in this Save Bodies feature: ") & bodyCount;
    swSaveBodyFeat.ReleaseSelectionAccess
```

```
End Sub
```
