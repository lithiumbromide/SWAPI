---
title: "Fire Event After Selection Made Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Event_After_Selection_Made_Example_VB.htm"
---

# Fire Event After Selection Made Example (VBA)

This example shows how to fire an event after a selection is made in a part, assembly, or drawing document.

```
'----------------------------------------------
' Preconditions:
' 1. Copy Main into your macro.
' 2. Click Insert > Class Module and copy Class1
'    into that module.
' 3. Click Insert > Class Module and copy Class2
'    into that module.
' 4. Click Insert > Class Module and copy Class3
'    into that module.
' 5. Open a part, assembly, or drawing.
'
' Postconditions:
' 1. Select an entity.
' 2. Displays a message box confirming your
'    selection.
' 3. Click OK to close the message box.
'----------------------------------------------
```

###### Main

```
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
Back to top
```

###### Class1

```
Public WithEvents doc As partDoc
```

```
Public Function init(ByRef docin As Object)
    Set doc = docin
End Function
```

```
Private Function doc_UserSelectionPostNotify() As Long
    MsgBox "Entity selected in a part document."
End Function
```

```
Back to top
```

###### Class2

```
Public WithEvents doc As assemblyDoc
```

```
Public Function init(ByRef docin As Object)
    Set doc = docin
End Function
```

```
Private Function doc_UserSelectionPostNotify() As Long
    MsgBox "Entity selected in an assembly document."
End Function
```

```
Back to top
```

###### Class3

```
Public WithEvents doc As drawingDoc
```

```
Public Function init(ByRef docin As Object)
    Set doc = docin
End Function
```

```
Private Function doc_UserSelectionPostNotify() As Long
    MsgBox "Entity selected in a drawing document."
End Function
```

```
Back to top
```
