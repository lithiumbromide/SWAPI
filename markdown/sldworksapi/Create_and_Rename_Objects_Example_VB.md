---
title: "Select and Rename Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Rename_Objects_Example_VB.htm"
---

# Select and Rename Object Example (VBA)

The example shows how to verify the name of the edge and then change it, if it doesn't already have a name.

**NOTE:** You could also select the edge programmatically using IFace2::GetEdges or ICoEdge::GetEdge.

```
'------------------------------------------------------------
' Precondtions:
' 1. Open a part.
' 2. Select an edge on the part.
'
' Postconditions:
' 1. Verifies that the user made a selection.
' 2. Gets the selected object and gets whether the selected
'    object is an edge.
' 3. If an edge, renames the edge if the edge doesn't already
'    have a name and the name is unique to the part.
' 4. Click OK to close the message box.
'------------------------------------------------------------
Option Explicit
```

```
Sub amin()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEntity As SldWorks.Entity
    Dim swSelObj As Object
    Dim edgeName As String
    Dim messageString As String
    Dim ret As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    If (swSelMgr.GetSelectedObjectCount <> 0) Then
        Set swSelObj = swSelMgr.GetSelectedObject6(1, -1)
        Set swEntity = swSelObj
        If (swSelMgr.GetSelectedObjectType(1) = swSelEDGES) Then
            edgeName = swPart.GetEntityName(swEntity)
            If (edgeName = "") Then
                ret = swPart.SetEntityName(swEntity, "NewEdgeName")
                If ret Then
                    swApp.SendMsgToUser ("Successfully set name of edge")
                Else
                    swApp.SendMsgToUser ("Error setting name of edge")
                End If
            Else
                messageString = "Edge already has name of " + edgeName
                swApp.SendMsgToUser (messageString)
            End If
        Else
            swApp.SendMsgToUser ("Select an edge and run the macro again")
        End If
    End If
```

```
End Sub
```
