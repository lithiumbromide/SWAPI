---
title: "Get Selected Objects and Types in Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Objects_and_Types_in_Assembly_Example_VB.htm"
---

# Get Selected Objects and Types in Assembly Example (VBA)

## Get Selected Objects and Types in an Assembly Example (VBA)

This example shows how to determine what is currently selected in an assembly document.

**NOTE**: You can select many features and entities in SOLIDWORKS Design. In most cases, it is obvious what is selected, but sometimes it is not clear or it is ambiguous. This example is a diagnostic tool to determine what is currently selected. It shows several techniques and methods to get a reference to what is selected.

```
'-----------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select a feature or entity in the assembly.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelObj As Object
    Dim swFeat As SldWorks.Feature
    Dim swEnt As SldWorks.Entity
    Dim swBody As SldWorks.Body2
    Dim swSelComp As SldWorks.Component2
    Dim swSelModel As SldWorks.ModelDoc2
    Dim nSelType As Long
    Dim sFeatName As String
    Dim bRet As Boolean
```

```
    ' Disables Visual Basic's implicit error on QueryInterface
    On Error Resume Next
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Could either have a feature or entity selected
    ' Do not try to get entity directly
    ' from feature because feature might be Nothing
    ' Instead, use ISelectionMgr
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swEnt = swSelMgr.GetSelectedObject6(1, -1)
    Set swBody = swSelMgr.GetSelectedObject6(1, -1)
    Set swSelObj = swSelMgr.GetSelectedObject6(1, -1)
    Set swSelComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
    Debug.Print "Selected Type      = " & swSelMgr.GetSelectedObjectType3(1, -1)
    If Not swFeat Is Nothing Then
        Debug.Print "Feature            = " + swFeat.Name + " [" + swFeat.GetTypeName + "]"
    End If
```

```
    If Not swBody Is Nothing Then
        Debug.Print "  Body selected"
    End If
```

```
    If swFeat Is Nothing And swEnt Is Nothing And swBody Is Nothing And Not swSelObj Is Nothing Then
        Debug.Print "  Unknown object"
    End If
```

```
    ' Could not get component from ISelectionMgr,
    ' so try and get component through IEntity
    If swSelComp Is Nothing Then
        Set swSelComp = swEnt.GetComponent
    End If
```

```
    If Not swSelComp Is Nothing Then
        Set swSelModel = swSelComp.GetModelDoc2
        Debug.Print "Component Name     = " + swSelComp.Name2
        Debug.Print "Model Path         = " + swSelModel.GetPathName
    End If

End Sub
```
