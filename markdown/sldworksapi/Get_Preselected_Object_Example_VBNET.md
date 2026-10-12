---
title: "Get Preselected Object Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Preselected_Object_Example_VBNET.htm"
---

# Get Preselected Object Example (VB.NET)

This example shows how to get a preselected object when a preselection event is fired.

```
'------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing.
' 2. Click Tools > Options > System Options > top VSTA debugger
'    on macro exit if the check box is selected.
' 3. If a part or assembly document is active, then
'    preselect (mouse over) a face.
'    - or -
'    If a drawing document is active, then preselect
'    an edge.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. When a face is preselected in a part or assembly
'    document, or an edge is pre-selected in a drawing document,
'    then that interface's UserSelectionPreNotify event is fired.
' 2. To stop running the macro, click Debug > Stop Debugging
'    in the SolidWorks Visual Studio Tools for Applications IDE.
' 3. Examine the Immediate window.
' 4. Click Tools > Options > System Options > Stop VSTA debugger
'    on macro exit to select the check box.
'----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Imports System.Diagnostics

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
        If SelectionType = swSelectType_e.swSelFACES Then
            Dim swModel As ModelDoc2
            Dim swSelMgr As SelectionMgr
            Dim SelectedObject As Object
            Dim swFace As Face2
            Dim swFeature As Feature

            swModel = swApp.ActiveDoc
            swSelMgr = swModel.SelectionManager
            SelectedObject = swSelMgr.GetPreSelectedObject()
            If SelectionType = swSelectType_e.swSelFACES Then
                swFace = SelectedObject
                swFeature = swFace.GetFeature
                Debug.Print("Name of feature whose face you preselected: " & swFeature.Name)
                Debug.Print("   Mouse over a different face, or click Debug > Stop Debugging to stop running macro")
                Debug.Print(" ")
            End If
        End If
    End Function

    Private Function aDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
        If SelectionType = swSelectType_e.swSelFACES Then
            Dim swModel As ModelDoc2
            Dim swSelMgr As SelectionMgr
            Dim SelectedObject As Object
            Dim swFace As Face2
            Dim swFeature As Feature

            swModel = swApp.ActiveDoc
            swSelMgr = swModel.SelectionManager
            SelectedObject = swSelMgr.GetPreSelectedObject()
            If SelectionType = swSelectType_e.swSelFACES Then
                swFace = SelectedObject
                swFeature = swFace.GetFeature
                Debug.Print("Name of feature whose face you preselected: " & swFeature.Name)
                Debug.Print("   Mouse over a different face, or click Debug > Stop Debugging to stop running macro")
                Debug.Print(" ")
            End If
        End If
    End Function

    Private Function dDoc_UserSelectionPreNotify(ByVal SelectionType As Integer) As Integer
        If SelectionType = swSelectType_e.swSelEDGES Then
            Dim swModel As ModelDoc2
            Dim swSelMgr As SelectionMgr
            Dim SelectedObject As Object
            Dim swEdge As Edge
            Dim swBody As Body2

            swModel = swApp.ActiveDoc
            swSelMgr = swModel.SelectionManager
            SelectedObject = swSelMgr.GetPreSelectedObject()
            If SelectionType = swSelectType_e.swSelEDGES Then
                swEdge = SelectedObject
                swBody = swEdge.GetBody
                Debug.Print("Name of body whose edge you preselected: " & swBody.Name)
                Debug.Print("   Mouse over a different edge, or click Debug > Stop Debugging to stop running macro")
                Debug.Print(" ")
            End If
        End If
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>

    Public swApp As SldWorks

End Class
```
