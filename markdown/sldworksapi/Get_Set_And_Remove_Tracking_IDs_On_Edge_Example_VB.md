---
title: "Get, Set, And Remove Tracking IDs On Edge (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Set_And_Remove_Tracking_IDs_On_Edge_Example_VB.htm"
---

# Get, Set, And Remove Tracking IDs On Edge (VBA)

This example shows how to get, set, and remove tracking IDs on an edge. Tracking IDs reliably associate application-specific data across modeling operations.

```vb
'------------------------------------------
'
' Preconditions: Part document with a single part is open.
'                The selected edge on the part has not
'                been assigned any tracking IDs.
'
' Directions:     Run the macro once, and the
'                 the selected edge is assigned
'                 a tracking ID of 12. Run
'                 the macro again, and the selected edge
'                 is assigned a tracking ID of 16. The
'                 the tracking ID is then deleted from the
'                 edge.
'
' Postconditions: None
'
'------------------------------------------
Option Explicit

Sub main()

    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim swModelExtn         As ModelDocExtension
    Dim swSelMgr            As SldWorks.SelectionMgr
    Dim swEdge              As SldWorks.Edge
    Dim Cookies             As Long
    Dim vTrackingIDs        As Variant
    Dim TrackingID          As Long
    Dim bRebuild            As Boolean

    Set swApp = CreateObject("SldWorks.Application")

    Cookies = swApp.RegisterTrackingDefinition("Tracking_API")
    If (Cookies = -1) Then
        End  ' No valid cookies found
    End If

    Stop

    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager

    Stop ' Select and edge on the part

    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)

    Debug.Print "---------------------------------"
    Dim NbrTrackingIds As Long
    NbrTrackingIds = swEdge.GetTrackingIDsCount(Cookies)
    Debug.Print "Edge Tracking IDs:"
    If (NbrTrackingIds = 0) Then

        Debug.Print "  No tracking IDs"
        Debug.Print "    Setting tracking ID..."
        Debug.Print "      SetTrackingID Result (if 0, then call successful): " & swEdge.SetTrackingID(Cookies, 12)
        Debug.Print "      GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
        Debug.Print "      Tracking ID after SetTrackingID call : " & vTrackingIDs(0)
        End

    Else

        Debug.Print "  Tracking IDs exist..."
        Debug.Print "    Getting tracking ID..."
        Debug.Print "      GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
        Debug.Print "      Tracking ID before SetTracingID call : " & vTrackingIDs(0)

        Debug.Print " "
        Debug.Print "      SetTrackingID Result (if 0, then call successful): " & swEdge.SetTrackingID(Cookies, 16)
        Debug.Print "      GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
        Debug.Print "      Tracking ID after SetTrackingID call: " & vTrackingIDs(0)
        Debug.Print " "
        Debug.Print "      Remove Tracking ID..."
        Debug.Print "        RemoveTrackingID Result (if 0, then call successful): " & swEdge.RemoveTrackingID(Cookies)
        Debug.Print "        Number of tracking IDs on this body: " & swEdge.GetTrackingIDsCount(Cookies)

        Debug.Print "---------------------------------"

   End If

End Sub
```
