---
title: "Get Corresponding Note in Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Note_in_Assembly_Example_VB.htm"
---

# Get Corresponding Note in Assembly Example (VBA)

This example shows how to determine if the selected note in an assembly corresponds to the selected note in a part that is a component of the assembly.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Copy public_documents\samples\tutorial\api\block.sldprt to c:\temp.
' 2. Open c:\temp\block.sldprt and add a note containing the text Note1.
' 3. Save the part.
' 4. Create an assembly of the part.
' 5. Save the assembly as c:\temp\block.sldasm.
'
' Postconditions:
' 1. At Stop, select the note and press F5.
' 2. Gets the Note object in the assembly.
' 3. Activates the part document.
' 4. At Stop, select the note and press F5.
' 5. Gets the Note object in the assembly.
' 6. Re-activates the assembly.
' 7. Gets whether the notes in the part and assembly are the same.
' 8. Click OK to close the message box.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swAssembly As SldWorks.AssemblyDoc
Dim swPart As SldWorks.PartDoc
Dim swModel As SldWorks.ModelDoc2
Dim swCompModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swCompModelDocExt As SldWorks.ModelDocExtension
Dim swAnnotation As SldWorks.Annotation
Dim swAssemComp As SldWorks.Component2
Dim swAssemNoteCorresp As SldWorks.Note
Dim swAssyNote As SldWorks.Note
Dim swPartNote As SldWorks.Note
Dim boolstatus As Boolean
Dim nRetVal As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    Stop
    ' Select the note in the assembly
    ' Press F5
```

```
    ' Get the note
    Set swAssyNote = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set swAnnotation = swAssyNote.GetAnnotation
    boolstatus = swAnnotation.Select3(False, Nothing)
```

```
    ' Activate the part document
    Set swPart = swApp.ActivateDoc2("Block.SLDPRT", True, nRetVal)
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    swModel.ClearSelection2 True
```

```
    Stop
    ' Select the note
    ' Press F5
```

```
    ' Get the note
    Set swPartNote = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set swAnnotation = swPartNote.GetAnnotation
    boolstatus = swAnnotation.Select3(False, Nothing)
```

```
    ' Re-activate the assembly
    Set swAssembly = swApp.ActivateDoc2("Block.SLDASM", True, nRetVal)
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    swModel.ClearSelection2 True
```

```
    ' Select the Block component in the assembly
    boolstatus = swModelDocExt.SelectByID2("Block-1@Block", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swAssemComp = swSelMgr.GetSelectedObject6(1, 0)
    Set swCompModel = swAssemComp.GetModelDoc
    Set swCompModelDocExt = swCompModel.Extension
```

```
    swModel.ClearSelection2 True
```

```
    ' Get whether the selected notes are the same note
    Set swAssemNoteCorresp = swCompModelDocExt.GetCorresponding(swPartNote)
    Dim strOutput As String
```

```
    ' Test feature returned by swCompMondelDocExt::GetCorresponding
    If swAssemNoteCorresp Is Nothing Then
        strOutput = "Note not obtained."
    Else
        If TypeOf swAssemNoteCorresp Is SldWorks.Note Then
            Set swAnnotation = swAssemNoteCorresp.GetAnnotation
            boolstatus = swAnnotation.Select3(False, Nothing)
            swAssemNoteCorresp.GetText
```

```
            'If swAssemNoteCorresp Is swAssyNote then
            'the pointers are different, but they point to the same note
            If swAssemNoteCorresp.GetText = "Note1" Then
                strOutput = "Note obtained correctly."
            Else
                strOutput = "swAssemNoteCorresp Is not swAssyNote."
            End If
        End If
    End If
```

```
    strOutput = strOutput + vbNewLine
    swModel.ClearSelection2 True
    strOutput = strOutput + vbNewLine
    MsgBox strOutput
```

```
End Sub
```
