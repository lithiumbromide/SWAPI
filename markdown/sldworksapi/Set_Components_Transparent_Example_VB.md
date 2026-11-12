---
title: "Set Components Transparent Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Components_Transparent_Example_VB.htm"
---

# Set Components Transparent Example (VBA)

This example shows how to make one or more selected components transparent

```vb
'-------------------------------------------
'
' Preconditions: Assembly document is open and one
'                or more components are selected.
'
' Postconditions: Selected components are transparent.
'
'-------------------------------------------
Option Explicit

    Dim swApp As SldWorks.SldWorks
    Dim swModelDoc As SldWorks.ModelDoc2
    Dim swAssembly As SldWorks.AssemblyDoc
    Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swAssembly = swModelDoc

    ' Set the selected component to transparent
    boolstatus = swAssembly.SetComponentTransparent(True)

    'Set the selected component to not transparent
    'boolstatus = swAssembly.SetComponentTransparent(False)

End Sub
```
