---
title: "Change Width of FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Width_of_FeatureManager_Design_Tree_Example_VB.htm"
---

# Change Width of FeatureManager Design Tree Example (VBA)

This example shows how to change the width of the FeatureManager design tree.

```
'----------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Doubles the width of FeatureManager design tree.
' 2. Examine the Immediate window and FeatureManager
'    design tree.
'----------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim nWidth As Long
    Dim NewWidth As Long
    Dim nRetVal As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    nWidth = swModel.GetFeatureManagerWidth
    nRetVal = swModel.SetFeatureManagerWidth(nWidth * 2)
    NewWidth = nWidth * 2
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Old width = " & nWidth & " pixels"
    Debug.Print "  New width = " & NewWidth & " pixels"
```

```
End Sub
```
