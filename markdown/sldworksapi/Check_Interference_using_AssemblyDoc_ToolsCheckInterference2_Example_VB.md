---
title: "Check Interference using AssemblyDoc::ToolsCheckInterference2 Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm"
---

# Check Interference using AssemblyDoc::ToolsCheckInterference2 Example (VBA)

## Check Interference using IAssemblyDoc::ToolsCheckInterference2 Example (VBA)

This example shows how to check an assembly for interference using IAssemblyDoc::ToolsCheckInterference2.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a fully resolved assembly that contains at least
'    two interfering components.
' 2. Select at least two interfering components.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Selects the interfering faces.
' 2. Examine the graphics area and Immediate window, then
'    press F5.
' 3. Selects the interfering components.
' 4. Examine the graphics area and Immediate window, then
'    press F5.
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const bCoincidentInterference   As Boolean = False
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim CompArray() As SldWorks.Component2
    Dim swSelData As SldWorks.SelectData
    Dim vCompArray As Variant
    Dim vIntCompArray As Variant
    Dim vIntFaceArray As Variant
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swComp As SldWorks.Component2
    Dim i As Long
    Dim nSelCount As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount
    ReDim CompArray(nSelCount - 1)
    Debug.Print "Number of selected components: " & nSelCount
    For i = 0 To (nSelCount - 1)
        Set CompArray(i) = swSelMgr.GetSelectedObjectsComponent2(i + 1)
        Debug.Print "  Comp[" & i & "] = " & CompArray(i).Name2
    Next i
    vCompArray = CompArray
    swAssy.ToolsCheckInterference2 nSelCount, (vCompArray), bCoincidentInterference, vIntCompArray, vIntFaceArray
    If (IsEmpty(vIntCompArray) = True) And (IsEmpty(vIntFaceArray) = True) Then
        Debug.Print "  No contact"
        Exit Sub
    End If
```

```
If Not IsEmpty(vIntFaceArray) Then
        Debug.Print "    " & UBound(vIntFaceArray) + 1 & " faces interfere!"
        swModel.ClearSelection2 True
        For i = 0 To UBound(vIntFaceArray)
            Set swFace = vIntFaceArray(i)
            Set swEnt = swFace
            Set swComp = swEnt.GetComponent
            Debug.Print "      Component face[" & i & "] = " & swComp.Name2
            bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet
        Next i
        ' Interfering faces selected
```

```
        Stop
        ' Examine the graphics area and Immediate window, then
        ' press F5 to continue
```

```
    Else
        Debug.Assert Not IsEmpty(vIntCompArray)
        Debug.Assert False = bCoincidentInterference
        Debug.Print "  Faces touch but not checking for coincident interference!"
    End If
```

```
    If Not IsEmpty(vIntCompArray) Then
        Debug.Print "  " & UBound(vIntCompArray) + 1 & " Components interfere!"
        swModel.ClearSelection2 True
        For i = 0 To UBound(vIntCompArray)
            Set swComp = vIntCompArray(i)
            Debug.Print "    Component [" & i & "] = " & swComp.Name2
            bRet = swComp.Select2(True, 0): Debug.Assert bRet
        Next i
```

```
        ' Interfering components selected
```

```
        Stop
        ' Examine the graphics area and Immediate window, then
        ' press F5 to continue
```

```
    End If
```

```
End Sub
```
