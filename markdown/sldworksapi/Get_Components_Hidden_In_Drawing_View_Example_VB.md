---
title: "Get Components Hidden In Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_Hidden_In_Drawing_View_Example_VB.htm"
---

# Get Components Hidden In Drawing View Example (VBA)

This example shows how to get the components hidden in the selected drawing view.

```
'----------------------------------------------
' Preconditions:
' 1. Open a drawing of an assembly.
' 2. Hide some components in a drawing view (expand a drawing view,
'    right-click the component, and click Show/Hide > Hide Component).
' 3. Select the drawing view where you hid the components.
'
' Postconditions:
' 1. Gets the hidden components in the selected drawing view.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDrView As SldWorks.View
    Dim vCompArr As Variant
    Dim vComp As Variant
    Dim swComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swDrView = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swDrView.Name
```

```
    vCompArr = swDrView.GetHiddenComponents
    If IsEmpty(vCompArr) Then Exit Sub
    For Each vComp In vCompArr
        Set swComp = vComp
        Debug.Print "    " & swComp.Name2
    Next
```

```
End Sub
```
