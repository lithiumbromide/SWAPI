---
title: "Change Referenced Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Referenced_Configuration_Example_VB.htm"
---

# Change Referenced Configuration Example (VBA)

This example shows how to change the configuration of a component in an assembly without opening the part.

```
'---------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component.
'
' Postconditions:
' 1. Changes the referenced configuration.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swModel As SldWorks.ModelDoc
    Dim swComp As SldWorks.Component
    Dim RefCfg As String
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swComp = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Change component configuration to "in-use"
    swComp.ReferencedConfiguration = ""
    RefCfg = swComp.ReferencedConfiguration
    Debug.Print "Referenced configuration: " & RefCfg
```

```
    ' For changes to take effect
    swModel.EditRebuild3
```

```
End Sub
```
