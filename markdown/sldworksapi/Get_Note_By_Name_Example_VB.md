---
title: "Get Note By Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Note_By_Name_Example_VB.htm"
---

# Get Note By Name Example (VBA)

This example shows how to get a note by its name using two separate methods: note traversal and note selection. The note selection method is faster because it avoids traversing all of the notes on the template.

```
'----------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\assem20.slddrw.
'
' Postconditions:
' 1. Opens the drawing template for editing.
' 2. Traverses the notes on the drawing template
'    until the note named DetailItem300 is found.
' 3. Click OK to close the message box.
' 4. Selects the note by its name.
' 5. Changes the text of the note to A.1.
' 6. Click OK to close the message box.
' 7. Examine the revision number note in the
'    drawing's title block.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDrawing As SldWorks.DrawingDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swNote As SldWorks.note
    Dim swView As SldWorks.view
    Dim swSelObj As Object
    Dim theCurrentRev As String
    Dim foundNote As Boolean
    Dim ret As Boolean
    Dim descriptionText As String
```

```
    Const swSelNOTES = 15
    Const swDocDRAWING = 3
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    ' Verify that the document is a drawing
    If (swModel Is Nothing) Or (swModel.GetType <> swDocDRAWING) Then
        Exit Sub
    End If
    Set swDrawing = swModel
```

```
    ' Edit the current drawing template
    swDrawing.EditTemplate
```

```
    ' This is the template
    Set swView = swDrawing.GetFirstView
```

```
    ' This section shows a slower method for
    ' selecting a note by name by using note
    ' traversal (swView::GetFirstNote and SwView::GetNext)
```

```
    ' Get the first note object
    Set swNote = swView.GetFirstNote
    ' While you have a valid note
    Do While Not swNote Is Nothing
        ' Verify if you have the desired note by checking its name
        ' This can also be done by checking the position or the existing
        ' text string in the note
        If (swNote.GetName = "DetailItem300") Then
            foundNote = True
            theCurrentRev = swNote.GetText
            swApp.SendMsgToUser ("Note found")
        End If
        Set swNote = swNote.GetNext
        ' Continue until no more notes
    Loop
```

```
    ' This section shows a faster method
    ' for selecting a note by using its name
    If (foundNote) Then
        ret = swModel.SelectByID("DetailItem300@Sheet Format1", "NOTE", 0, 0, 0)
        'Get the SelectionMgr object
        Set swSelMgr = swModel.SelectionManager
        ' If user has selected something
        If (swSelMgr.GetSelectedObjectCount <> 0) Then
            ' Get the first item in the selection list
            Set swSelObj = swSelMgr.GetSelectedObject2(1)
            ' If selected object is a note
            If (swSelMgr.GetSelectedObjectType(1) = swSelNOTES) Then
                descriptionText = theCurrentRev + "A.1"
                ' Change the text in the note
                ret = swSelObj.SetText(descriptionText)
                ' If change is successful
                If (ret = True) Then
                    swApp.SendMsgToUser ("Note text changed")
                ' If name change failed
                Else
                    swApp.SendMsgToUser ("Error changing note text")
                End If
            End If
        ' If selection change failed
        Else
            swApp.SendMsgToUser ("Error selecting note")
        End If
    End If
```

```
End Sub
```
