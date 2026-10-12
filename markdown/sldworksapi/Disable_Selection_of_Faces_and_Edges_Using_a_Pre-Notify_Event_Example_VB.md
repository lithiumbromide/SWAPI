---
title: "Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VB.htm"
---

# Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VBA)

This example shows how to disable the interactive selection of these entities using a pre-notify event:

- faces in part and assembly documents
- edges in drawing documents

```
'------------------------------------
' Preconditions:
' 1. Copy Module into the macro.
' 2. Click Insert > Class Module and copy Class1 into
'    that module.
' 3. Click Insert > Class Module and copy Class2 into
'    that module.
' 4. Click Insert > Class Module and copy Class3 into
'    that module.
' 5. Open a part, assembly, or drawing.
'
'
' Postconditions:
' 1. Disables interactively selecting faces in
'    a part or assembly.
'    - or -
'    Disables interactively selecting edges in a
'    drawing.
' 2. Click the Reset button in the Microsoft Visual
'    Basic IDE to re-enable the interactive selection
'    of faces in a part or assembly or edges
'    in a drawing.
'----------------------------------------
'Module
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

```vb
Back to top
```

###### ' Class1 Public WithEvents doc As partDoc

```vb
Public Function init(ByRef docIn As Object)
     Set doc = docIn
 End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
     ' Disable the selection of faces in this part
     If SelectionType = swSelFACES Then
         doc_UserSelectionPreNotify = True
     End If
End Function
```

[Back to top](#Top)

###### 'Class2

```vb
Public WithEvents doc As assemblyDoc

Public Function init(ByRef docIn As Object)
    Set doc = docIn
End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
    ' Disable selection of faces in this assembly
    If SelectionType = swSelFACES Then
        doc_UserSelectionPreNotify = True
    End If
End Function
```

[Back to top](#Top)

###### 'Class3

```vb
Public WithEvents doc As drawingDoc

Public Function init(ByRef docIn As Object)
    Set doc = docIn
End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
    ' Disable the selection of edges in drawings
    If SelectionType = swSelEDGES Then
        doc_UserSelectionPreNotify = True
    End If
End Function
Back to top
```
