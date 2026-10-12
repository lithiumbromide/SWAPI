---
title: "Get Visible Components and Entities in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm"
---

# Get Visible Components and Entities in Drawing View Example (VBA)

This example shows how to get the visible components and entities in a drawing view.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 ' 2. Select Drawing View2.
 '
 ' Postconditions:
 ' 1. Gets the visible entities in Drawing View2.
 ' 2. Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swDrawing As SldWorks.DrawingDoc
     Dim drView As SldWorks.View
     Dim Comp As SldWorks.Component2
     Dim selData As SldWorks.SelectData
     Dim ent As SldWorks.Entity
     Dim itr As Long
     Dim CompCount As Long
     Dim vComps As Variant
     Dim vEdges As Variant
     Dim vVerts As Variant
     Dim vFaces As Variant
     Dim vSilhouetteEdges As Variant
     Dim i As Long
     Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDrawing = swModel
     Set swSelMgr = swModel.SelectionManager
     Set drView = swDrawing.ActiveDrawingView

    Debug.Assert Not drView Is Nothing
     Debug.Print "Name of drawing view: " & drView.GetName2
     Debug.Print

    CompCount = drView.GetVisibleComponentCount

    Debug.Assert CompCount <> 0
     Debug.Print "Number of visible components = " & CompCount

    vComps = drView.GetVisibleComponents

    Debug.Assert Not IsEmpty(vComps)

    For i = LBound(vComps) To UBound(vComps)
         swModel.ClearSelection2 True
         Debug.Print ""
         Debug.Print "Component " & i & " name is " & vComps(i).Name2

        Set Comp = vComps(i)

        'Get all edges of this component that are visible in this drawing view
         vEdges = drView.GetVisibleEntities2(Comp, swViewEntityType_Edge)

        Set selData = swSelMgr.CreateSelectData

        selData.View = drView

        If IsEmpty(vEdges) Then
             Debug.Print "   No edges."
         Else
             Debug.Print "   This component has " & UBound(vEdges) + 1 & " visible edges in this view."
             For itr = 0 To UBound(vEdges)
                 Set ent = vEdges(itr)
                 boolstatus = ent.Select4(False, selData)
             Next itr
         End If

        'Get all vertices of this component that are visible in this drawing view
         vVerts = drView.GetVisibleEntities2(Comp, swViewEntityType_Vertex)

        If IsEmpty(vVerts) Then
             Debug.Print "   No vertices."
         Else
             Debug.Print "   This component has " & UBound(vVerts) + 1 & " visible vertices in this view."
             For itr = 0 To UBound(vVerts)
                 Set ent = vVerts(itr)
                 boolstatus = ent.Select4(False, selData)
             Next itr
         End If

        swModel.ClearSelection2 True

        'Get all faces of this component that are visible in this drawing view
         vFaces = drView.GetVisibleEntities2(Comp, swViewEntityType_Face)

        If IsEmpty(vFaces) Then
             Debug.Print "   No faces."
         Else
             Debug.Print "   This component has " & UBound(vFaces) + 1 & " visible faces in this view."
             For itr = 0 To UBound(vFaces)
                 Set ent = vFaces(itr)
                 boolstatus = ent.Select4(False, selData)
             Next itr
         End If

        'Get all silhouette edges of this component that are visible in this drawing view
         vSilhouetteEdges = drView.GetVisibleEntities2(Comp, swViewEntityType_SilhouetteEdge)

        Dim silEdge As SldWorks.SilhouetteEdge
         If IsEmpty(vSilhouetteEdges) Then
             Debug.Print "   No silhouette edges."
         Else
             Debug.Print "   This component has " & UBound(vSilhouetteEdges) + 1 & " visible silhouette edges in this view."
              For itr = 0 To UBound(vSilhouetteEdges)
                 Set silEdge = vSilhouetteEdges(itr)
                 boolstatus = silEdge.Select(False, selData)
             Next itr
         End If
     Next i
End Sub
```
