---
title: "Get Parent Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parent_Component_Example_VB.htm"
---

# Get Parent Component Example (VBA)

This example shows how to get the parent component of the selected assembly or subassembly component.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select an assembly or subassembly component.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the parent component of the selected assembly
'    or subassembly component.
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
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim swComp As SldWorks.Component2
    Dim swParentComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
```

```
    ' Returns Nothing if selected component is a top-level assembly component
    Set swParentComp = swComp.GetParent
    If Nothing Is swParentComp Then
        Set swConfigMgr = swModel.ConfigurationManager
        Set swConf = swConfigMgr.ActiveConfiguration
        Set swParentComp = swConf.GetRootComponent3(True)
    End If
```

```
    Debug.Assert Not swParentComp Is Nothing
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Component = " & swComp.Name2 & " [" & swComp.GetPathName & "]"
    Debug.Print "    Parent component = " & swParentComp.Name2 & " [" & swParentComp.GetPathName & "]"
```

```
End Sub
```
