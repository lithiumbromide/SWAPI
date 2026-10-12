---
title: "Get Corresponding Note in Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Note_in_Part_Example_VB.htm"
---

# Get Corresponding Note in Part Example (VBA)

This example shows how to determine if the selected note in a part corresponds to the selected note in an assembly to which the part belongs.

```
'-----------------------------------------
' Preconditions:
' 1. Copy public_documents\samples\tutorial\api\block.sldprt to c:\temp.
' 2. Open c:\temp\block.sldprt and add a note containing the text Note1.
' 3. Save the part.
' 4. Create an assembly of the part.
' 5. Save the assembly as c:\temp\block.sldasm.
' 6. Open the Immediate window.
'
' Postconditions:
' 1. At Stop, select the note and press F5.
' 2. Gets the Note object in the assembly.
' 3. Activates the part document.
' 4. At Stop, select the note and press F5.
' 5. Gets the Note object in the assembly.
' 6. Gets whether the notes in the part and assembly are the same.
' 7. Examine the Immediate window.
'------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swPart As SldWorks.PartDoc
Dim swAssemNote As SldWorks.Note
Dim swPartNote As SldWorks.Note
Dim swPartNoteCorresp As Object
Dim swAnnotation As SldWorks.Annotation
Dim status As Boolean
Dim errors As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    Stop
    ' Select Note1 and press F5
```

```
    Set swAssemNote = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
```

```
    ' Activate the part document
    Set swPart = swApp.ActivateDoc3("Block.SLDPRT", True, swRebuildOnActivation_e.swUserDecision, errors)
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swPart.Extension
```

```
    swModel.ClearSelection2 True
```

```
    Stop
    ' Select Note1 and press F5
```

```
    Set swPartNote = swSelMgr.GetSelectedObject6(1, 0)
```

```
    ' Get whether the selected notes are the same note
    Set swPartNoteCorresp = swModelDocExt.GetCorresponding(swAssemNote)
    If swPartNoteCorresp Is Nothing Then
        Debug.Print ("Note not obtained.")
    Else
        If TypeOf swPartNoteCorresp Is SldWorks.Note Then
            Set swAnnotation = swPartNoteCorresp.GetAnnotation
            swModel.ClearSelection2 True
            status = swAnnotation.Select3(False, Nothing)
            swPartNoteCorresp.GetText
            ' If swAssemNoteCorresp is swAssyNote, then
            ' the pointers are different, but they point to the same note
            If swPartNoteCorresp.GetText = "Note1" Then
                Debug.Print ("Note obtained correctly.")
            Else
                Debug.Print ("swPartNoteCorresp Is Not swAssyNote.")
            End If
        End If
    End If
End Sub
```
