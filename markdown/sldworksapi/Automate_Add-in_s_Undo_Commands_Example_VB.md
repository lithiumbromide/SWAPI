---
title: "Automate Add-in's Undo Commands Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Automate_Add-in_s_Undo_Commands_Example_VB.htm"
---

# Automate Add-in's Undo Commands Example (VBA)

This example shows how to automate an add-in's undo commands.

- Module
- Class modules
- [swUndoApiHdlr1](#swUndoApiHdlr1)
- [swUndoApiHdlr2](#swUndoApiHdlr2)

Module macro1

```vb
'----------------------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions: None
'
'----------------------------------------------------
Option Explicit

Dim swApp As Object
Dim swModel  As SldWorks.ModelDoc2
Dim swModExt As SldWorks.ModelDocExtension
Dim Retval As Boolean
Dim name As String
Dim i As Long

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModExt = swModel.Extension()

For i = 1 To 2
    Dim swUndoObj1 As swUndoApiHdlr1
    Set swUndoObj1 = New swUndoApiHdlr1
    swUndoObj1.a = i
    name = "AddinUndo : " & i
    Retval = swModExt.SetApiUndoObject(swUndoObj1, name)

Next i

For i = 1 To 2
    Dim swUndoObj2 As swUndoApiHdlr2
    Set swUndoObj2 = New swUndoApiHdlr2
    swUndoObj2.a = i
    name = "AddinUndoReset : " & i
    Retval = swModExt.SetApiUndoObject(swUndoObj2, name)
Next i

End Sub
```

[Back to top](#Top)

Class module swUndoApiHdlr1

```vb
Option Explicit

Implements SwUndoAPIHandler
Public a As Long

Private Sub SwUndoAPIHandler_DoUndo()
    MsgBox "Add-in's undo called " & vbCrLf & "Undo object count : " + Str(a)
End Sub

Private Sub SwUndoAPIHandler_UndoReSet()
    MsgBox ("Add-in's undo list reset")
End Sub
```

[Back to top](#Top)

Class module swUndoApiHdlr2

```vb
Option Explicit

Implements SwUndoAPIHandler
Public a As Long

Private Sub SwUndoAPIHandler_DoUndo()
    MsgBox "Undo called " & vbCrLf & "Undo count : " + Str(a)
End Sub

Private Sub SwUndoAPIHandler_UndoReSet()
    MsgBox ("Undo reset called ")
End Sub
```

[Back to top](#Top)
