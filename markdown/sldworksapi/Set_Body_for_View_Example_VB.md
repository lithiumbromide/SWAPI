---
title: "Set Body for View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Body_for_View_Example_VB.htm"
---

# Set Body for View Example (VBA)

This example shows how to show just one body of a multibody part in a drawing view.

```vb
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
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim nbrBodies As Long
Dim arrBody As Variant
Dim swBody As SldWorks.Body2
Dim swFace As SldWorks.Face2
Dim swEnt As SldWorks.Entity
Dim swSelData As SldWorks.SelectData
Dim bool As Boolean
Dim arrBodiesIn As Variant
Dim Bodies(0) As Object
Dim i As Long
Dim objType As Long

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swView = swSelMgr.GetSelectedObject6(1, -1)
If (swView Is Nothing) Then
    MsgBox "View not selected."
    Exit Sub
End If
nbrBodies = swView.GetBodiesCount
    Debug.Print "Number of bodies: " & nbrBodies
    If (nbrBodies < 1) Then
        MsgBox "No bodies in selected view."
        Exit Sub
    End If
arrBody = swView.Bodies
For i = 0 To UBound(arrBody)
    Set swBody = arrBody(i)
    Set swSelData = swSelMgr.CreateSelectData
    swSelData.View = swView
    bool = swBody.Select2(False, swSelData)
        ' Object type 76 is a solid body
        objType = swSelMgr.GetSelectedObjectType3(1, -1)
        If (objType = 76) Then
            Debug.Print " Object type: solid body"
        End If
        If (Not (swSelSOLIDBODIES = swSelMgr.GetSelectedObjectType3(1, -1))) Then
            MsgBox "Solid body not found."
        End If
        Set swFace = swBody.GetFirstFace
        Do While Not swFace Is Nothing
            Set swEnt = swFace
            ' Select using IEntity
            bool = swEnt.Select4(True, swSelData): Debug.Assert bool
            Set swFace = swFace.GetNextFace
        Loop
        Debug.Print "   Name of body: " & swBody.GetSelectionId
    Next i

swModel.ClearSelection2 True

' Get the bodies from referenced model
Set swModel = swView.ReferencedDocument
arrBody = swModel.GetBodies2(swSolidBody, True)
If (nbrBodies = 1) Then
   swView.Bodies = (arrBody)
Else
   ' Set the body to view
   Set Bodies(0) = arrBody(0)
   arrBodiesIn = Bodies
   swView.Bodies = (arrBodiesIn)
End If

swModel.ClearSelection2 True
```

```vb
End Sub
```
