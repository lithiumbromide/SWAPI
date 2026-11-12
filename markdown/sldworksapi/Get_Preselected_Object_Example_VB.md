---
title: "Get Preselected Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Preselected_Object_Example_VB.htm"
---

# Get Preselected Object Example (VBA)

This example shows how to get a preselected object when a preselection event is fired.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing.
' 2. In the SOLIDWORKS Visual Basic IDE:
'    a. Copy and paste Main into the macro's main module.
'    b. Click Insert > Class Module and copy and paste
'       Class1 into that module.
'    c. Click Insert > Class Module and copy and paste
'       Class2 into that module.
'    d. Click Insert > Class Module and copy and paste
'       Class3 into that module.
' 3. If a part or assembly document is active, then
'    preselect (mouse over) a face.
'    - or -
'    If a drawing document is active, then preselect
'    an edge.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. When a face is preselected in a part or assembly
'    document, or an edge is preselected in a drawing document,
'    then that interface's UserSelectionPreNotify event is fired.
' 2. In the SOLIDWORKS Visual Basic IDE, click Run > Reset to
'    stop running the macro.
' 3. Examine the Immediate window.
'-----------------------------------------------------------
' Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim partDoc As New Class1
Dim assemblyDoc As New Class2
Dim drawingDoc As New Class3
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Determine the document type, then
    ' execute its corresponding class module
    If swModel.GetType = swDocPART Then
        partDoc.init swModel
    ElseIf swModel.GetType = swDocASSEMBLY Then
        assemblyDoc.init swModel
    ElseIf swModel.GetType = swDocDRAWING Then
        drawingDoc.init swModel
    End If
```

```
End Sub
```

```
Go to top
```

```
'Class1
```

```
Public WithEvents doc As partDoc
```

```
Public Function init(ByRef docIn As Object)
    Set doc = docIn
End Function
```

```
Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
    If SelectionType = swSelFACES Then
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
        Dim swSelMgr As SldWorks.SelectionMgr
        Dim SelectedObject As Object
        Dim swFace As SldWorks.Face2
        Dim swFeature As SldWorks.Feature
        Set swSelMgr = swModel.SelectionManager
        Set SelectedObject = swSelMgr.GetPreSelectedObject
        If SelectionType = swSelFACES Then
            Set swFace = SelectedObject
            Set swFeature = swFace.GetFeature
            Debug.Print "Name of feature whose face you preselected: " & swFeature.Name
            Debug.Print "   Select a different face, or in the IDE to stop running the macro, click Run > Reset"
            Debug.Print " "
        End If
    End If
```

```
End Function
```

```
Go to top
```

```
'Class2
```

```
Public WithEvents doc As assemblyDoc
```

```
Public Function init(ByRef docIn As Object)
    Set doc = docIn
End Function
```

```
Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
        Dim swSelMgr As SldWorks.SelectionMgr
        Dim SelectedObject As Object
        Dim swFace As SldWorks.Face2
        Dim swFeature As SldWorks.Feature
        Set swSelMgr = swModel.SelectionManager
        Set SelectedObject = swSelMgr.GetPreSelectedObject
        If SelectionType = swSelFACES Then
            Set swFace = SelectedObject
            Set swFeature = swFace.GetFeature
            Debug.Print "Name of feature whose face you preselected: " & swFeature.Name
            Debug.Print "   Select a different face, or in the IDE to stop running the macro, click Run > Reset"
            Debug.Print " "
        End If
End Function
```

```
Go to top
```

```
'Class3
```

```
Public WithEvents doc As drawingDoc
```

```
Public Function init(ByRef docIn As Object)
    Set doc = docIn
End Function
```

```
Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
        If SelectionType = swSelEDGES Then
            Set swApp = Application.SldWorks
            Set swModel = swApp.ActiveDoc
            Dim swSelMgr As SldWorks.SelectionMgr
            Dim SelectedObject As Object
            Dim swEdge As SldWorks.Edge
            Dim swBody As SldWorks.Body2
            Set swSelMgr = swModel.SelectionManager
            Set SelectedObject = swSelMgr.GetPreSelectedObject
            If SelectionType = swSelEDGES Then
                Set swEdge = SelectedObject
                Set swBody = swEdge.GetBody
                Debug.Print "Name of body whose edge you preselected: " & swBody.Name
                Debug.Print "   Select a different edge, or in the IDE to stop running the macro, click Run > Reset"
                Debug.Print " "
            End If
        End If
End Function
```

```
Go to top
```
