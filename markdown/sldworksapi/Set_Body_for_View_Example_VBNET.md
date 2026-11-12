---
title: "Set Body for View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Body_for_View_Example_VBNET.htm"
---

# Set Body for View Example (VB.NET)

This example shows how to show just one body of a multibody part in a drawing view.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
' 2. Save the part document as a drawing document:
'    a. Click File > Make Drawing from Part.
'    b. Click OK on the Sheet Format/Size dialog.
'    c. Drag the *Isometric view from the View Palette onto
'       the drawing sheet.
' 3. Select the drawing view.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Shows one body of the multibody part
'    in the drawing view.
' 2. Examine the drawing and the Immediate window.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swView As View
        Dim nbrBodies As Long
        Dim arrBody As Object
        Dim swBody As Body2
        Dim swFace As Face2
        Dim swEnt As Entity
        Dim swSelData As SelectData
        Dim bool As Boolean
        Dim arrBodiesIn(0) As DispatchWrapper
        Dim Bodies(0) As Object
        Dim i As Long
        Dim objType As Long

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swView = swSelMgr.GetSelectedObject6(1, -1)
        If (swView Is Nothing) Then
            MsgBox("View not selected.")
            Exit Sub
        End If
        nbrBodies = swView.GetBodiesCount
        Debug.Print("Number of bodies: " & nbrBodies)
        If (nbrBodies < 1) Then
            MsgBox("No bodies in selected view.")
            Exit Sub
        End If
        arrBody = swView.Bodies
        For i = 0 To UBound(arrBody)
            swBody = arrBody(i)
            swSelData = swSelMgr.CreateSelectData
            swSelData.View = swView
            bool = swBody.Select2(False, swSelData)
            ' Object type 76 is a solid body
            objType = swSelMgr.GetSelectedObjectType3(1, -1)
            If (objType = 76) Then
                Debug.Print(" Object type: solid body")
            End If
            If (Not (swSelectType_e.swSelSOLIDBODIES = swSelMgr.GetSelectedObjectType3(1, -1))) Then
                MsgBox("Solid body not found.")
            End If
            swFace = swBody.GetFirstFace
            Do While Not swFace Is Nothing
                swEnt = swFace
                ' Select using IEntity
                bool = swEnt.Select4(True, swSelData) : Debug.Assert(bool)
                swFace = swFace.GetNextFace
            Loop
            Debug.Print("   Name of body: " & swBody.GetSelectionId)
        Next i

        swModel.ClearSelection2(True)

        ' Get the bodies from referenced model
        swModel = swView.ReferencedDocument
        arrBody = swModel.GetBodies2(swBodyType_e.swSolidBody, True)
        If (nbrBodies = 1) Then
            swView.Bodies = (arrBody)
        Else
            ' Set the body to include in the drawing view
            Bodies(0) = arrBody(0)
            arrBodiesIn(0) = New DispatchWrapper(Bodies(0))
            swView.Bodies = (arrBodiesIn)
        End If

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
