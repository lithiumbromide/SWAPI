---
title: "Drawing Views and Model Entities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Drawing_Views_and_Model_Entities.htm"
---

# Drawing Views and Model Entities

[IView::GetPolylines7](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetPolylines7.html) and [IView::IGetPolylines7](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetPolylines7.html) return all of the polylines in a drawing view, including visible and partially and completely obscured polylines. Because these polylines are not related to the topology of the model, you do not know their relationship to the model, making it difficult to work with them.

[IView::GetVisibleComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetVisibleComponents.html), [IView::IGetVisibleComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetVisibleComponents.html), [IView::GetVisibleEntities](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetVisibleEntities.html), and [IView::IGetVisibleEntities](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetVisibleEntities.html) return the visible components, edges, faces, and vertices in relation to the topology of the model, which simplifies working with them. Visible components, edges, faces, and vertices are all of the components and entities not completely obscured by other components in the drawing view.

Typical uses of IView::GetVisibleComponents or IView::IGetVisibleComponents and IView::GetVisibleEnities or IView::IGetVisibleEntities might be to get a component or an entity in order to get its properties or to add an annotation to it.

The following example shows how to retrieve all of the visible components, edges, faces, and vertices in a drawing view.

```vb
'--------------------------------------------------
' Preconditions: Drawing document is open, and
' a drawing view containing at least one component
' is selected.
'
' Postconditions: None
'--------------------------------------------------
Option Explicit

Sub main()
```

```vb
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDrawing As SldWorks.DrawingDoc
Dim drView As SldWorks.View
Dim Comp As SldWorks.Component2
Dim selData As SldWorks.SelectData
Dim ent As SldWorks.Entity
Dim EntComp As SldWorks.Component2
Dim itr As Long
Dim CompCount As Long
Dim vComps As Variant
Dim vEdges As Variant
Dim vVerts As Variant
Dim vFaces As Variant
Dim i As Long
Dim boolstatus As Boolean

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swDrawing = swModel
Set swSelMgr = swModel.SelectionManager
Set drView = swDrawing.ActiveDrawingView
Debug.Assert Not drView Is Nothing
Debug.Print "Name of drawing view: "; drView.Name
Debug.Print

CompCount = drView.GetVisibleComponentCount
Debug.Assert CompCount <> 0
Debug.Print "Number of visible components = "; CompCount

vComps = drView.GetVisibleComponents
Debug.Assert Not IsEmpty(vComps)
For i = LBound(vComps) To UBound(vComps)
    swModel.ClearSelection2 True
    Debug.Print ""
    Debug.Print "Component " & i & " name is " & vComps(i).Name2

    Set Comp = vComps(i)
    'Get all edges of this component that are visible in this drawing view
    vEdges = drView.GetVisibleEntities(Comp, swViewEntityType_Edge)

    Set selData = swSelMgr.CreateSelectData
    selData.View = drView

    If IsEmpty(vEdges) Then
        Debug.Print "   No edges"
    Else
        Debug.Print "   This component has " & UBound(vEdges) + 1 & " visible edges in this view."
        For itr = 0 To UBound(vEdges)
            Set ent = vEdges(itr)
            boolstatus = ent.Select4(False, selData)
        Next itr
    End If

    'Get all vertices of this component that are visible in this drawing view
    vVerts = drView.GetVisibleEntities(Comp, swViewEntityType_Vertex)
    If IsEmpty(vVerts) Then
        Debug.Print "   No vertices"
    Else
        Debug.Print "   This component has " & UBound(vVerts) + 1 & " visible vertices in this view"
        For itr = 0 To UBound(vVerts)
            Set ent = vVerts(itr)
            boolstatus = ent.Select4(False, selData)
        Next itr
    End If

    swModel.ClearSelection2 True

    'Get all faces of this component that are visible in this drawing view
    vFaces = drView.GetVisibleEntities(Comp, swViewEntityType_Face)
    If IsEmpty(vFaces) Then
        Debug.Print "   No faces"
    Else
        Debug.Print "   This component has " & UBound(vFaces) + 1 & " visible faces in this view."
        For itr = 0 To UBound(vFaces)
            Set ent = vFaces(itr)
            boolstatus = ent.Select4(False, selData)
        Next itr
    End If

Next i
```

```vb
    'Get all the entities (edges, faces, and vertices) that are visible in the drawing view
    Debug.Print
    swModel.ClearSelection2 True
    Set Comp = Nothing

    Set EntComp = Nothing

    'Get all edges of all components that are visible in this drawing view
    vEdges = drView.GetVisibleEntities(Comp, swViewEntityType_Edge)
    Debug.Print "There are a total of " & UBound(vEdges) + 1 & " visible edges in this view."
    For itr = 0 To UBound(vEdges)
        Set ent = vEdges(itr)
        'boolstatus = ent.Select4(False, selData)
        Set EntComp = ent.GetComponent
        Set EntComp = Nothing
    Next itr

    'Get all vertices of all components that are visible in this drawing view
    vVerts = drView.GetVisibleEntities(Comp, swViewEntityType_Vertex)
    Debug.Print "There are a total of " & UBound(vVerts) + 1 & " visible vertices in this view."
    For itr = 0 To UBound(vVerts)
        Set ent = vVerts(itr)
        'boolstatus = ent.Select4(False, selData)
        Set EntComp = ent.GetComponent
        Set EntComp = Nothing
    Next itr

    swModel.ClearSelection2 True

    'Get all faces of all components that are visible in this drawing view
    vFaces = drView.GetVisibleEntities(Comp, swViewEntityType_Face)
    Debug.Print "There are a total of " & UBound(vFaces) + 1 & " visible faces in this view."
    For itr = 0 To UBound(vFaces)
        Set ent = vFaces(itr)
        'boolstatus = ent.Select4(False, selData)
    Next itr

End Sub
```
