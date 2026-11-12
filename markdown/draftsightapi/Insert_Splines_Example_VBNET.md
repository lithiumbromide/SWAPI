---
title: "Insert Splines Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Splines_Example_VBNET.htm"
---

# Insert Splines Example (VB.NET)

This example shows how to:

- construct several Splines, which are displayed as the Dassault Systèmes logo in a DraftSight drawing.
- fire events before and after commands are executed.
- select a group of entities and modify a member in that group of entities.
- execute a command using IApplication::RunCommand.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add references to System and System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
'
' Postconditions:
' 1. CommandPreNotify event is fired. Click OK to close the
'    message box.
' 2. Click anywhere in the drawing when you are prompted
'    in the command window to Click to insert a point
'    for the lower-left corner for the 3DS logo.
' 3. CommandPostNotify event is fired. Click OK to close
'    the message box.
' 4. The Dassault Systemes logo is constructed in the drawing.
'    a. Examine the drawing to verify.
'    b. Press F5 in the IDE.
'       The Dassault Systemes logo's letter D is changed
'       from blue to yellow.
'    c. Press F5 to in the IDE.
'       The Dassault Systemes logo's letter D is changed
'       back to blue.
'    d. Press F5 in the IDE.
' 5. CommandPreNotify event is fired. Click OK to close the
'    the message box.
' 6. CommandPostNotify event is fired. Click OK to close the
'    message box.
' 7. The Dassault Systemes logo is deleted.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Imports System
Imports System.Windows.Forms

Module Module1
```

```
    Dim WithEvents dsApp As DraftSight.Interop.dsAutomation.Application
    Dim commandPreNotifyCommand As String = " "
    Dim commandPostNotifyCommand As String = " "

    Dim dsDoc As Document

    Sub Main()
```

```
        Dim dsSketchMgr As SketchManager
        Dim dsSelectionManager As SelectionManager
        Dim dsSelectionFilter As SelectionFilter
        Dim dsEntityHelper As EntityHelper

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        ' Abort any command currently running in DraftSight to
        ' avoid nested commands
        dsApp.AbortRunningCommand()
```

```
        'Get command message object
        Dim dsCommandMessage As CommandMessage
        dsCommandMessage = dsApp.GetCommandMessage

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If

        'Get model space
        Dim dsModel As Model
        dsModel = dsDoc.GetModel()

        'Get Sketch Manager
        Dim dsSketchMgr As SketchManager
        dsSketchMgr = dsModel.GetSketchManager()

        Dim x As Double
        Dim y As Double
        Dim z As Double

        ' Prompt to insert the a point for lower-left corner of the 3DS logo
        Dim dsMathUtility As MathUtility
        Dim dsMathPlane As MathPlane
        dsMathUtility = dsApp.GetMathUtility()
        dsMathPlane = dsMathUtility.CreateXYPlane()
        Dim status As Boolean
        status = dsCommandMessage.PromptForPoint2("Click to insert a point for the lower-left corner for the 3DS logo", True, 0, 0, 0, x, y, z, dsMathPlane)

        Dim spArray1(26) As Double
        Dim spArray2(23) As Double
        Dim spArray3(17) As Double

        ' Construct the D
        spArray1(0) = x + 0.4513
        spArray1(1) = y + 0.3825
        spArray1(2) = z + 0.0#
        spArray1(3) = x + 0.324
        spArray1(4) = y + 0.1912
        spArray1(5) = z + 0.0#
        spArray1(6) = x + 0.1261
        spArray1(7) = y + 0.0932
        spArray1(8) = z + 0.0#
        spArray1(9) = x + 0.2571
        spArray1(10) = y + 0.3839
        spArray1(11) = z + 0.0#
        spArray1(12) = x + 0.0023
        spArray1(13) = y + 0.0086
        spArray1(14) = z + 0.0#
        spArray1(15) = x + 0.2132
        spArray1(16) = y + 0.0711
        spArray1(17) = z + 0.0#
        spArray1(18) = x + 0.5275
        spArray1(19) = y + 0.4664
        spArray1(20) = z + 0.0#
        spArray1(21) = x + 0.428
        spArray1(22) = y + 0.5052
        spArray1(23) = z + 0.0#
        spArray1(24) = x + 0.1237
        spArray1(25) = y + 0.4568
        spArray1(26) = z + 0.0#

        Dim spline1 As Spline
        spline1 = dsSketchMgr.InsertSpline(spArray1, True, 0, 0, 0, 0, 0, 0)

        ' Construct the S
        spArray2(0) = x + 0.4659
        spArray2(1) = y + 0.1472
        spArray2(2) = 0.0#
        spArray2(3) = x + 0.8218
        spArray2(4) = y + 0.2052
        spArray2(5) = z + 0.0#
        spArray2(6) = x + 0.6099
        spArray2(7) = y + 0.5472
        spArray2(8) = z + 0.0#
        spArray2(9) = x + 0.7898
        spArray2(10) = y + 0.6372
        spArray2(11) = z + 0.0#
        spArray2(12) = x + 0.9877
        spArray2(13) = y + 0.5952
        spArray2(14) = z + 0.0#
        spArray2(15) = x + 0.7158
        spArray2(16) = y + 0.5472
        spArray2(17) = z + 0.0#
        spArray2(18) = x + 0.9318
        spArray2(19) = y + 0.2232
        spArray2(20) = z + 0.0#
        spArray2(21) = x + 0.7818
        spArray2(22) = y + 0.1112
        spArray2(23) = z + 0.0#

        Dim spline2 As Spline
        spline2 = dsSketchMgr.InsertSpline(spArray2, True, 0, 0, 0, 0, 0, 0)

        ' Construct the 3
        spArray3(0) = x + 0.6319
        spArray3(1) = y + 0.8672
        spArray3(2) = z + 0.0#
        spArray3(3) = x + 0.33
        spArray3(4) = y + 0.9233
        spArray3(5) = z + 0.0#
        spArray3(6) = x + 0.5
        spArray3(7) = y + 0.9642
        spArray3(8) = z + 0.0#
        spArray3(9) = x + 0.7318
        spArray3(10) = y + 0.8952
        spArray3(11) = z + 0.0#
        spArray3(12) = x + 0.6279
        spArray3(13) = y + 0.6892
        spArray3(14) = z + 0.0#
        spArray3(15) = x + 0.369
        spArray3(16) = y + 0.5563
        spArray3(17) = z + 0.0#

        Dim spline3 As Spline
        spline3 = dsSketchMgr.InsertSpline(spArray3, True, 0, 0, 0, 0, 0, 0)

        ' Set the colors for the logo
        Dim color1 As Color
        Dim color2 As Color
        Dim color3 As Color

        color1 = spline1.Color
        color2 = spline2.Color
        color3 = spline3.Color

        color1.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue)
        color2.SetNamedColor(dsNamedColor_e.dsNamedColor_Yellow)
        color3.SetNamedColor(dsNamedColor_e.dsNamedColor_Red)

        spline1.Color = color1
        spline2.Color = color2
        spline3.Color = color3
```

```
        ' Examine the drawing to verify
        ' that the logo was created
        ' and that the letter D is blue, the
        ' letter S is yellow, and the non-letter
        ' is red

         Stop
        ' Press F5 to change the colors of the logo

        'Get Selection Manager
        dsSelectionManager = dsDoc.GetSelectionManager

        'Get selection filter
        dsSelectionFilter = dsSelectionManager.GetSelectionFilter

        'Clear selection filter
        dsSelectionFilter.Clear()

        'Add Spline entities to the selection filter
        dsSelectionFilter.AddEntityType(dsObjectType_e.dsSplineType)

        'Activate selection filter
        dsSelectionFilter.Active = True

        'Get all layer names
        Dim layerNames As String() = GetLayers(dsDoc)

        Dim entityTypes() As Integer = Nothing
        Dim entityObjects() As Object = Nothing

        'Get Spline entities
        dsSketchMgr.GetEntities(dsSelectionFilter, layerNames, entityTypes, entityObjects)

        ' Get EntityHelper
        dsEntityHelper = dsApp.GetEntityHelper

        ' Change the letter D in the logo from blue to yellow
        dsEntityHelper.SetColor(entityObjects(0), color2)

        Stop
        ' Examine the drawing to verify that
        ' the color of D has changed from blue to yellow
        ' Press F5 to continue

        dsEntityHelper.SetColor(entityObjects(0), color1)

        Stop
        ' Examine the drawing to verify that the color
        ' of D has changed back to blue
        ' Press F5 to delete the logo

        Dim state As Integer
        state = dsApp.RunCommand2("DELETE ALL" & Chr(10) & Chr(10), Nothing, Nothing, False)

    End Sub
```

```
    Private Sub dsApp_CommandPreNotify(ByVal commandPreNotifycommand As String, ByVal doc As Document) Handles dsApp.CommandPreNotify
        MsgBox("CommandPreNotify event was fired before " & commandPreNotifycommand & " was executed.")
    End Sub

     Private Sub dsApp_CommandPostNotify(ByVal commandPostNotifycommand As String, ByVal doc As Document) Handles dsApp.CommandPostNotify
        MsgBox("CommandPostNotify event was fired after " & commandPostNotifycommand & " was executed.")
    End Sub
```

```
    Function GetLayers(ByVal dsDoc As Document) As String()
        'Get Layer Manager and Layer names
        Dim dsLayerManager As LayerManager = dsDoc.GetLayerManager()

        Dim dsLayers As Object() = DirectCast(dsLayerManager.GetLayers(), Object())

        Dim layerNames As String() = New String(dsLayers.Length - 1) {}

        For index As Integer = 0 To dsLayers.Length - 1
            Dim dsLayer As Layer = TryCast(dsLayers(index), Layer)
            layerNames(index) = dsLayer.Name
        Next

        Return layerNames
    End Function
```

```
End Module
```
