---
title: "Get Edge Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Points_Example_VB.htm"
---

# Get Edge Points Example (VBA)

This example shows how to get edge points.

NOTE: An edge point is a midpoint on an edge or an endpoint or midpoint on a reference curve.

```vb
'---------------------------------------------
'
' Preconditions: Part document is open and
'                at least one edge point is selected.
'
' Postconditions: None
'
'---------------------------------------------
Dim swApp As Object

Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim edgep As SldWorks.EdgePoint
    Dim swSelObj As Object
    Dim SelType As Long
    Dim SelCount As Long

    Set swApp = GetObject(, "SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    SelCount = swSelMgr.GetSelectedObjectCount

    For i = 1 To SelCount
        SelType = swSelMgr.GetSelectedObjectType(i)
        Debug.Print SelType
        If SwConst.swSelectType_e.swSelPOINTREFS = SelType Then
            Set swSelObj = swSelMgr.GetSelectedObject5(i)
            Set edgep = swSelObj
        End If
    Next i

End Sub
```
