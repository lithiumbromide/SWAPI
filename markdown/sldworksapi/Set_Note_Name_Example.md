---
title: "Set Note Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Note_Name_Example.htm"
---

# Set Note Name Example (VBA)

This example shows how to set the name of a selected note. You can combine this code with a dialog that prompts the user for a desired name, or you can programmatically determine the new note name.

```vb
'------------------------------------------------------------------
Sub SetNoteName( newNoteName As String )

' Define variable used to hold the SldWorks object
Dim swApp As Object

' Define variable used to hold the ModelDoc object
Dim Model As Object

' Define variable used to hold the SelectionMgr object
Dim SelMgr As Object
Dim note As Object
Dim checkNoteName As String

Const swSelNOTES = 15
Const swDocDRAWING = 3

' Attach to or open SOLIDWORKS Design session
Set swApp = CreateObject("SldWorks.Application")
' Grab the current document
Set Model = swApp.ActiveDoc

' Verify that the document is a drawing
If (Model Is Nothing) Or (Model.GetType <> swDocDRAWING) Then
Exit Sub
End If

Set SelMgr = Model.SelectionManager

' Make sure a selection exists
If (SelMgr.GetSelectedObjectCount = 0) Then
swApp.SendMsgToUser "Select a Note first..."

Else
' If selected object is a note
If (SelMgr.GetSelectedObjectType(1) = 15) Then
' Get the Note object from the selection list
Set note = SelMgr.GetSelectedObject2(1)
' Use the Note object to change the note name
res = note.SetName (newNoteName)
checkNoteName = note.GetName

' If note name does not match
If (checkNoteName <> newNoteName) Then
swApp.SendMsgToUser "Error changing note name."
End If

End If

End If

End Sub
```
