---
title: "Get Component IDs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_IDs_Example_VB.htm"
---

# Get Component IDs Example (VBA)

This example shows how to get the component IDs of the components in an assembly and subassemblies.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document containing nested subassemblies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the assembly and subassemblies.
' 2. Gets the name and component ID of each component in the assembly and
'    subassemblies.
' 3. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```
Sub TraverseComponent(swComp As SldWorks.Component2, nLevel As Long)
    Dim vChildComp                  As Variant
    Dim swChildComp                 As SldWorks.Component2
    Dim sPadStr                     As String
    Dim i                           As Long
```

```
    For i = 0 To nLevel - 1
        sPadStr = sPadStr + "  "
    Next i
    vChildComp = swComp.GetChildren
    For i = 0 To UBound(vChildComp)
        Set swChildComp = vChildComp(i)
        Debug.Print sPadStr & "Component name: " & swChildComp.Name2 & ", Component ID: " & swChildComp.GetID
        TraverseComponent swChildComp, nLevel + 1
    Next i
End Sub
```

```
Sub main()

    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swConfMgr                   As SldWorks.ConfigurationManager
    Dim swConf                      As SldWorks.Configuration
    Dim swRootComp                  As SldWorks.Component2
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swConfMgr = swModel.ConfigurationManager
    Set swConf = swConfMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
    Debug.Print "File = " & swModel.GetPathName
    If swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then
        TraverseComponent swRootComp, 1
    End If
```

```
End Sub
```
