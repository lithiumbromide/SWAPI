---
title: "Reload Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reload_Model_Example_VB.htm"
---

# Reload Model Example (VBA)

This example shows how to reload the active model with the last saved version of the model.

```
'----------------------------------
' Preconditions:
' 1. Open a part or assembly document.
' 2. Suppress a feature in the part or a
'    component in the assembly.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Replaces the active part or assembly model
'    with last saved model.
' 2. Examine graphics area and the Immediate window.
'
' NOTE: Any changes made to the model in the current
' session are discarded if they were not saved
' previous to running this macro.
'-----------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim nRetVal As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    ' Fails for drawings because functionality is not supported in user interface
    nRetVal = swModel.Extension.ReloadOrReplace(False, swModel.GetPathName, True, True)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  ReloadOrReplace (0 = swComponentReloadError_e.swReloadOkay) = " & nRetVal
```

```
End Sub
```
