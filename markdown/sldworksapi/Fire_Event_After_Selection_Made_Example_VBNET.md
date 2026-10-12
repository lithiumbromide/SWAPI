---
title: "Fire Event After Selection Made Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Event_After_Selection_Made_Example_VBNET.htm"
---

# Fire Event After Selection Made Example (VB.NET)

This example shows how to fire an event after a selection is made in a part, assembly, or drawing document.

```
'------------------------------------------------------
' Preconditions: Open a part, assembly, or drawing.
'
' Postconditions:
' 1. Select an entity.
' 2. Displays a message box confirming your
'    selection.
'    NOTE: If necessary, click the message box icon
'    on the Windows taskbar to display the message box.
' 3. Click OK to close the message box.
'
' NOTE: Tools > Options > System>  Stop VSTA debugger
' on macro exit must be cleared for this macro to run to
' completion.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Partial Class SolidWorksMacro

    Public WithEvents pDoc As PartDoc

    Public WithEvents aDoc As AssemblyDoc

    Public WithEvents dDoc As DrawingDoc

    Public Sub main()

        Dim swModel As ModelDoc2

        swModel = swApp.ActiveDoc

        ' Determine the document type

        ' and set up event
handlers

        If swModel.GetType = swDocumentTypes_e.swDocPART Then

            pDoc = swModel

        ElseIf swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then

            aDoc = swModel

        ElseIf swModel.GetType = swDocumentTypes_e.swDocDRAWING Then

            dDoc = swModel

        End If

        AttachEventHandlers()

    End Sub
```

Sub AttachEventHandlers()
AttachSWEvents()
End Sub

Sub AttachSWEvents()
If Not pDoc Is Nothing Then
AddHandler pDoc.UserSelectionPostNotify, AddressOf Me.pDoc_UserSelectionPostNotify
End If

If Not aDoc Is Nothing Then
AddHandler aDoc.UserSelectionPostNotify, AddressOf Me.aDoc_UserSelectionPostNotify
End If

If Not dDoc Is Nothing Then
AddHandler dDoc.UserSelectionPostNotify, AddressOf Me.dDoc_UserSelectionPostNotify
End If

End Sub

Private Function pDoc_**UserSelectionPostNotify**() As Integer
MsgBox("Entity selected in part document.")
End Function

Public Function aDoc_**UserSelectionPostNotify**() As Integer
MsgBox("Entity selected in assembly document.")
End Function

Private Function dDoc_**UserSelectionPostNotify**() As Integer
MsgBox("Entity selected in drawing document.")
End Function

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
