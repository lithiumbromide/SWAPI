---
title: "Make Assembly Components Lightweight Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Assembly_Components_Lightweight_Example_VB.htm"
---

# Make Assembly Components Lightweight Example (VBA)

This example shows how to change the selected components in an assembly from fully resolved to lightweight.

```
'----------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select the fully resolved components that you want to
'    change to lightweight.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Changes the selected components to lightweight.
' 2. Examine the Immediate window and the FeatureManager
'    design tree.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim nSelCount As Long
    Dim i As Long
    Dim bRet As Boolean
    Dim nRetVal As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
    Debug.Print "Number of selected components = " & nSelCount
    Debug.Print ""
```

```
    Debug.Print "Selected components"
```

```
    For i = 1 To nSelCount
        Set swComp = swSelMgr.GetSelectedObjectsComponent4(i, -1)
        Debug.Print "  Component = " & swComp.Name2
        Debug.Print "    Path = " & swComp.GetPathName
        Debug.Print "    Suppressed state = " & swComp.GetSuppression
        Debug.Print "    Is suppressed? " & swComp.IsSuppressed
    Next i
```

```
    swAssy.MakeLightWeight
```

```
    Debug.Print ""
    Debug.Print "Number of lightweight components = " & swAssy.GetLightWeightComponentCount
```

```
End Sub
```
