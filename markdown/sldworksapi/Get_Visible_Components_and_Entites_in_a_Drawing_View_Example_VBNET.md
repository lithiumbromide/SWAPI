---
title: "Get Visible Components and Entities in Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_VBNET.htm"
---

# Get Visible Components and Entities in Drawing View Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swDrawing As DrawingDoc
         Dim drView As View
         Dim Comp As Component2
         Dim selData As SelectData
         Dim ent As Entity
         Dim itr As Integer
         Dim CompCount As Integer
         Dim vComps As Object
         Dim vEdges As Object
         Dim vVerts As Object
         Dim vFaces As Object
         Dim vSilhouetteEdges As Object
         Dim i As  Integer
         Dim boolstatus As Boolean

         swModel = swApp.ActiveDoc
         swDrawing = swModel
         swSelMgr = swModel.SelectionManager
         drView = swDrawing.ActiveDrawingView

         Debug.Assert(Not drView Is Nothing)
         Debug.Print("Name of drawing view: " & drView.GetName2)
         Debug.Print("")

         CompCount = drView.GetVisibleComponentCount

         Debug.Assert(CompCount <> 0)
         Debug.Print("Number of visible components = " & CompCount)

         vComps = drView.GetVisibleComponents

         Debug.Assert(Not IsNothing(vComps))

         For i = LBound(vComps) To UBound(vComps)
             swModel.ClearSelection2(True)
             Debug.Print("")
             Debug.Print("Component " & i & " name is " & vComps(i).Name2)

             Comp = vComps(i)

             'Get all edges of this component that are visible in this drawing view
             vEdges = drView.GetVisibleEntities2(Comp, swViewEntityType_e.swViewEntityType_Edge)

             selData = swSelMgr.CreateSelectData

             selData.View = drView

             If IsNothing(vEdges) Then
                 Debug.Print("   No edges.")
             Else
                 Debug.Print("   This component has " & UBound(vEdges) + 1 & " visible edges in this view.")
                 For itr = 0 To UBound(vEdges)
                     ent = vEdges(itr)
                     boolstatus = ent.Select4(False, selData)
                 Next itr
             End If

             'Get all vertices of this component that are visible in this drawing view
             vVerts = drView.GetVisibleEntities2(Comp, swViewEntityType_e.swViewEntityType_Vertex)

             If IsNothing(vVerts) Then
                 Debug.Print("   No vertices.")
             Else
                 Debug.Print("   This component has " & UBound(vVerts) + 1 & " visible vertices in this view.")
                 For itr = 0 To UBound(vVerts)
                     ent = vVerts(itr)
                     boolstatus = ent.Select4(False, selData)
                 Next itr
             End If

             swModel.ClearSelection2(True)

             'Get all faces of this component that are visible in this drawing view
             vFaces = drView.GetVisibleEntities2(Comp, swViewEntityType_e.swViewEntityType_Face)

             If IsNothing(vFaces) Then
                 Debug.Print("   No faces.")
             Else
                 Debug.Print("   This component has " & UBound(vFaces) + 1 & " visible faces in this view.")
                 For itr = 0 To UBound(vFaces)
                     ent = vFaces(itr)
                     boolstatus = ent.Select4(False, selData)
                 Next itr
             End If

             'Get all silhouette edges of this component that are visible in this drawing view
             vSilhouetteEdges = drView.GetVisibleEntities2(Comp, swViewEntityType_e.swViewEntityType_SilhouetteEdge)

             Dim silEdge As SilhouetteEdge
             If IsNothing(vSilhouetteEdges) Then
                 Debug.Print("   No silhouette edges.")
             Else
                 Debug.Print("   This component has " & UBound(vSilhouetteEdges) + 1 & " visible silhouette edges in this view.")
                 For itr = 0 To UBound(vSilhouetteEdges)
                     silEdge = vSilhouetteEdges(itr)
                     boolstatus = silEdge.Select(False, selData)
                 Next itr
             End If
         Next i

     End Sub

     Public swApp As SldWorks

 End  Class
```
