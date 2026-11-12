---
title: "Get Component by Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_by_Name_Example_VB.htm"
---

# Get Component by Name Example (VBA)

This examples shows how to get a component by name and to determine if that component is fixed or floating.

```
'-------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\EDraw\claw\claw-mechanism.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the specified component.
' 2. Gets whether the specified component is fixed.
' 3. Examine the Immediate window.
'-------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
```

```
    Set swComp = swAssy.GetComponentByName("center-1")
    Debug.Print "Is component fixed: " & swComp.IsFixed
```

```
End Sub
```
