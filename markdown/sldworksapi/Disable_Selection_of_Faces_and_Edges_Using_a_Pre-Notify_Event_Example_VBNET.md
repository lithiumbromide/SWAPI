---
title: "Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VBNET.htm"
---

# Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VB.NET)

This example shows how to disable the interactive selection of these entities using a pre-notify event:

- faces in part and assembly documents
- edges in drawing documents

```vb
'---------------------------------------------------
 ' Preconditions: Open a part, assembly, or drawing.
 '
 ' NOTE: Tools > Options > System > Stop VSTA debugger
 '    on macro exit must be cleared for this macro
 ' to run to completion.
 '
 ' Postconditions:
 ' 1. Disables interactively selecting faces in
 '    a part or assembly.
 '    - or -
 '    Disables interactively selecting edges in a
 '    drawing.
 ' 2. Click the Stop Debugging button in the
 '    SOLIDWORKS Visual Studio Tools for
 '    Applications IDE to re-enable the
 '    interactive selection of faces in
 '    a part or assembly document or edges in
 '    a drawing document.
 '----------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Collections
 Partial Class SolidWorksMacro
     Public WithEvents pDoc As PartDoc
     Public WithEvents aDoc As AssemblyDoc
     Public WithEvents dDoc As DrawingDoc
     Public Sub main()
         Dim swModel As ModelDoc2
         Dim openPart As Hashtable
         Dim openAssembly As Hashtable
         Dim openDrawing As Hashtable
        swModel = swApp.ActiveDoc
        ' Determine the document type
         ' and set up event handlers
         If swModel.GetType = swDocumentTypes_e.swDocPART Then
             pDoc = swModel
             openPart = New Hashtable
         ElseIf swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then
             aDoc = swModel
             openAssembly = New Hashtable
         ElseIf swModel.GetType = swDocumentTypes_e.swDocDRAWING Then
             dDoc = swModel
             openDrawing = New Hashtable
         End If
         AttachEventHandlers()
    End Sub
    Sub AttachEventHandlers()
         AttachSWEvents()
     End Sub
    Sub AttachSWEvents()
         If Not pDoc Is Nothing Then
             AddHandler pDoc.UserSelectionPreNotify, AddressOf Me.pDoc_UserSelectionPreNotify
         End If
         If Not aDoc Is Nothing Then
             AddHandler aDoc.UserSelectionPreNotify, AddressOf Me.aDoc_UserSelectionPreNotify
         End If
         If Not dDoc Is Nothing Then
             AddHandler dDoc.UserSelectionPreNotify, AddressOf Me.dDoc_UserSelectionPreNotify
         End If
     End Sub
    Private Function pDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
         ' Disable the selection of faces in this part
         If SelectionType = swSelectType_e.swSelFACES Then
             pDoc_UserSelectionPreNotify = True
         End If
     End Function
    Public Function aDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
         ' Disable the selection of faces in this assembly
         If SelectionType = swSelectType_e.swSelFACES Then
             aDoc_UserSelectionPreNotify = True
         End If
     End Function
    Private Function dDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
         ' Disable the selection of edges in this drawing
         If SelectionType = swSelectType_e.swSelEDGES Then
             dDoc_UserSelectionPreNotify = True
         End If
     End Function
    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
End Class
```
