---
title: "Insert Reference Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Plane_Example_VBNET.htm"
---

# Insert Reference Plane Example (VB.NET)

This example shows how to create a constraint-based angle reference plane.

```
'-----------------------------------------------------------
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a constraint-based reference plane.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swRefPlane As RefPlane
        Dim swSelMgr As SelectionMgr
        Dim swRefPlaneFeatureData As RefPlaneFeatureData
        Dim fileerror As Long
        Dim filewarning As Long
        Dim boolstatus As Boolean
        Dim planeType As Long

        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager
        swSelMgr = swModel.SelectionManager

        ' Create a constraint-based reference plane
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.028424218552, 0.07057725774359, 0, True, 0, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.05976462601598, 0.0718389621656, 0.0001242036435087, True, 1, Nothing, 0)
        swRefPlane = swFeatureManager.InsertRefPlane(16, 0.7853981633975, 4, 0, 0, 0)

        ' Get type of the just-created reference plane
        boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swRefPlaneFeatureData = swFeature.GetDefinition

        planeType = swRefPlaneFeatureData.Type2
        Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type2: ")
        Select Case planeType
            Case 0
                Debug.Print("  Invalid")
            Case 1
                Debug.Print("  Undefined")
            Case 2
                Debug.Print("  Line Point")
            Case 3
                Debug.Print("  Three Points")
            Case 4
                Debug.Print("  Line Line")
            Case 5
                Debug.Print("  Distance")
            Case 6
                Debug.Print("  Parallel")
            Case 7
                Debug.Print("  Angle")
            Case 8
                Debug.Print("  Normal")
            Case 9
                Debug.Print("  On Surface")
            Case 10
                Debug.Print("  Standard")
            Case 11
                Debug.Print("  Constraint-based")
        End Select
        Debug.Print("")

        planeType = swRefPlaneFeatureData.Type
        Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type: ")
        Select Case planeType
            Case 0
                Debug.Print("  Invalid")
            Case 1
                Debug.Print("  Undefined")
            Case 2
                Debug.Print("  Line Point")
            Case 3
                Debug.Print("  Three Points")
            Case 4
                Debug.Print("  Line Line")
            Case 5
                Debug.Print("  Distance")
            Case 6
                Debug.Print("  Parallel")
            Case 7
                Debug.Print("  Angle")
            Case 8
                Debug.Print("  Normal")
            Case 9
                Debug.Print("  On Surface")
            Case 10
                Debug.Print("  Standard")
            Case 11
                Debug.Print("  Constraint-based")
        End Select
        Debug.Print("")

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
