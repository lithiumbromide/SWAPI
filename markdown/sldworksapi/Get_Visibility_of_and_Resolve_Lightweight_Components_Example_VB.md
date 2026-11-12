---
title: "Get Visibility of and Resolve Lightweight Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visibility_of_and_Resolve_Lightweight_Components_Example_VB.htm"
---

# Get Visibility of and Resolve Lightweight Components Example (VBA)

This example shows how to get the visibility of and resolve lightweight components.

```
'----------------------------------------------------
' Preconditions:
' 1. Open an assembly lightweight (click File > Open >
'    assembly_file_name.sldasm > change Mode to
'    Lightweight > Open.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree and resolves
'    all components.
' 2. Examine the Immediate window and the FeatureManager
'    design tree.
'----------------------------------------------------
Option Explicit
```

```
Sub GetComponentVisib(swComp As SldWorks.Component2, sPadStr As String)
```

```
    Dim vChildArray As Variant
    Dim swChildComp As SldWorks.Component2
    Dim i As Long
```

```
    ' Root component has no name (empty string)
    Debug.Print sPadStr & swComp.Name2 & " [" & swComp.Visible & "]"
```

```
    vChildArray = swComp.GetChildren
    For i = 0 To UBound(vChildArray)
        Set swChildComp = vChildArray(i)
        GetComponentVisib swChildComp, sPadStr & "  "
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConfig As SldWorks.Configuration
    Dim swConfMgr As SldWorks.ConfigurationManager
    Dim swRootComp As SldWorks.Component2
    Dim nStatus As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swConfMgr = swModel.ConfigurationManager
    Set swConfig = swConfMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
```

```
    nStatus = swAssy.ResolveAllLightWeightComponents(False)
    Debug.Assert swResolveOk = nStatus
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    GetComponentVisib swRootComp, "  "
```

```
End Sub
```
