---
title: "Get Top-level Components Using Component IDs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Top-level_Component_Using_Component_IDs_Example_VB.htm"
---

# Get Top-level Components Using Component IDs Example (VBA)

This example shows how to get the top-level components in an assembly using their component IDs.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document containing subassemblies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the assembly.
' 2. Gets the name and component ID of each top-level component
'    in the assembly.
' 3. Adds each component ID to an array and traverses the array.
'    a. Gets each top-level component using its component ID.
'    b. Gets the name and component ID of each top-level component
'       in the assembly.
' 4. Examine the Immediate window and FeatureManager design tree.
'---------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssemblyDoc As SldWorks.AssemblyDoc
    Dim swConfMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim i As Long
    Dim compID As Long
    Dim compIDs() As Long
    Dim nbrComp As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssemblyDoc = swModel
    Set swConfMgr = swModel.ConfigurationManager
    Set swConf = swConfMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
```

```
    Debug.Print "Get top-level components by traversing assembly:"
    vChildComp = swRootComp.GetChildren
    nbrComp = UBound(vChildComp)
    ReDim compIDs(nbrComp)
    For i = 0 To nbrComp
        Set swChildComp = vChildComp(i)
        compID = swChildComp.GetID
        Debug.Print "  Component name: " & swChildComp.Name2 & ", Component ID: " & compID
        ' Add component ID to an array
        compIDs(i) = compID
    Next i
```

```
    Debug.Print ""

    Debug.Print "Get top-level components using component IDs:"
    Set swChildComp = Nothing
    nbrComp = UBound(compIDs)
    For i = 0 To UBound(compIDs)
        compID = compIDs(i)
        Set swChildComp = swAssemblyDoc.GetComponentByID(compID)
        Debug.Print "  Component name: " & swChildComp.Name2 & ", Component ID: " & swChildComp.GetID
    Next i
```

```
End Sub
```
