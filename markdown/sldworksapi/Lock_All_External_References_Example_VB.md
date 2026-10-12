---
title: "Lock All External References Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Lock_All_External_References_Example_VB.htm"
---

# Lock All External References Example (VBA)

This example shows how to lock all external references in a part or assembly in reverse chronological order.

```
'---------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 1. Open the Immediate window.
'
' Postconditions:
' 1. Locks all external references.
' 2. Examine the Immediate window.
'---------------------------------------
Option Explicit
```

```
Sub ProcessModel(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, sPadStr As String)
    Debug.Print sPadStr & "  Locking: " & swModel.GetPathName
    swModel.LockAllExternalReferences
End Sub
```

```
Sub ProcessComponent(swApp As SldWorks.SldWorks, swComp As SldWorks.Component2, sPadStr As String)
    Dim vChildCompArr As Variant
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim swChildModel As SldWorks.ModelDoc2
```

```
    vChildCompArr = swComp.GetChildren
    For Each vChildComp In vChildCompArr
        Set swChildComp = vChildComp
        Debug.Print sPadStr & swChildComp.Name2
        ProcessComponent swApp, swChildComp, sPadStr & "  "
        Set swChildModel = swChildComp.GetModelDoc
        ProcessModel swApp, swChildModel, sPadStr
    Next vChildComp
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim nStatus As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConf = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Select Case swModel.GetType
        Case swDocPART
            ProcessModel swApp, swModel, "  "
        Case swDocASSEMBLY
            Set swAssy = swModel
            nStatus = swAssy.ResolveAllLightWeightComponents(False)
            Set swRootComp = swConf.GetRootComponent
            ProcessComponent swApp, swRootComp, "  "
        Case Else
            Exit Sub
    End Select
```

```
End Sub
```
