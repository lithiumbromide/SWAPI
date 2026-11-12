---
title: "Insert Hatch by Entities or Internal Points (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_by_Entities_or_Internal_Points_Example_VBNET.htm"
---

# Insert Hatch by Entities or Internal Points (VB.NET)

## Insert Hatch by Entities or Internal Points Example (VB.NET)

This example shows how to insert a Hatch either by selecting sketch entities that form the Hatch boundary or by selecting internal points of enclosed areas of a drawing.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this example into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a drawing document with sketch entities.
 ' 6. Start debugging the project.
 '
 ' In the DraftSight command window, specify how the Hatch should be inserted:
 '    1. Type Entities.
 '    2. Select the sketch entities that form the boundary of the area to be hatched.
 '    3. Press Enter.
 '    - or -
 '    1. Type InternalPoints.
 '    2. Select three points that are in enclosed areas of the drawing.
 '
 ' Postconditions: A Hatch is inserted, and the drawing document
 ' is zoomed to fit.
 '----------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1
     Dim dsApp As DraftSight.Interop.dsAutomation.Application
     Dim dsDoc As Document

     Sub Main(ByVal args As String())
         'Connect to DraftSight application
         dsApp = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         dsDoc = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get sketch manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Get command message object
         Dim dsCommandMessage As CommandMessage = dsApp.GetCommandMessage()

         'Display a prompt at the command line to create Hatch by entities or by internal points
         Dim keywords As String() = {"Entities", "InternalPoints"}
         Dim selectedKeyword As String = ""
         Dim promptResult As Boolean = dsCommandMessage.PromptForKeyword("Insert Hatch by:", keywords, keywords(0), selectedKeyword)
         If promptResult Then
             'The user selected "By Entities" option
             If selectedKeyword.ToUpper() = "_" & keywords(0).ToUpper() OrElse selectedKeyword.ToUpper() = keywords(0).ToUpper()  Then
                 Dim selectedEntities As DispatchWrapper() = SelectEntities(dsCommandMessage)

                 InsertHatchByEntities(dsSketchMgr, selectedEntities)
             End If

             'The user selected "By Internal Points" option
             If selectedKeyword.ToUpper() = "_" & keywords(1).ToUpper() Then
                 'Select three internal points
                 Dim pointsCount As Integer = 3

                 dsCommandMessage.PrintLine("Select three internal points for a Hatch")

                 Dim internalPoints As Double() = SelectPoints(dsCommandMessage, pointsCount)

                 InsertHatchByInternalPoints(dsSketchMgr, internalPoints)
             End If
         End If
     End Sub

     Sub InsertHatchByInternalPoints(ByVal dsSketchMgr As SketchManager, ByVal internalPoints As Double())
         'Hatch parameters
         Dim patternName As String = "ANSI31"
         Dim patternScale As Double = 1
         Dim patternAngle As Double = 0

         'Insert Hatch
         Dim dsHatch As Hatch = dsSketchMgr.InsertHatchByInternalPoints(internalPoints, patternName, patternScale, patternAngle)
         If dsHatch IsNot Nothing Then
             'Change color of Hatch
             Dim dsColor As Color = dsHatch.Color
             dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green)
             dsHatch.Color = dsColor

             'Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
         Else
             MessageBox.Show("Hatch entity was not added to the current drawing.")
         End If
     End Sub

     Function SelectPoints(ByVal dsCommandMessage As CommandMessage, ByVal internalPointsCount As Integer) As  Double()
         Dim internalPoints As New List(Of Double)()

         'Display prompt for point
         Dim x As  Double, y  As  Double, z  As  Double
         Dim count As Integer = 0
         While count < internalPointsCount
             If dsCommandMessage.PromptForPoint("Specify internal point", x, y, z)  Then
                 internalPoints.Add(x)
                 internalPoints.Add(y)
             End If

             count += 1
         End While

         Return internalPoints.ToArray()
     End Function

     Sub InsertHatchByEntities(ByVal dsSketchMgr As SketchManager, ByVal dsEntities As DispatchWrapper())
         'Hatch parameters
         Dim patternName As String = "GRASS"
         Dim patternScale As Double = 1
         Dim patternAngle As Double = 0

         'Insert Hatch
         Dim dsHatch As Hatch = dsSketchMgr.InsertHatchByEntities(dsEntities, patternName, patternScale, patternAngle)
         If dsHatch IsNot Nothing Then
             'Change color of Hatch
             Dim dsColor As Color = dsHatch.Color
             dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue)
             dsHatch.Color = dsColor

             'Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
         Else
             MessageBox.Show("Hatch entity was not added to the current drawing.")
         End If
     End Sub

     Function SelectEntities(ByVal dsCommandMessage As CommandMessage) As DispatchWrapper()
         Dim selectedEntities As DispatchWrapper() = Nothing

         'Prompt for multiple selection of entities
         If dsCommandMessage.PromptForSelection(False, "Specify entities", "It is not an entity") Then
             'Get selection manager
             Dim dsSelectionMgr As SelectionManager = dsDoc.GetSelectionManager()

             'Get count of selected entities
             Dim selectionType As dsSelectionSetType_e = dsSelectionSetType_e.dsSelectionSetType_Previous
             Dim count As Integer = dsSelectionMgr.GetSelectedObjectCount(selectionType)
             If count > 0 Then
                 selectedEntities =  New DispatchWrapper(count - 1) {}
                 For index As Integer = 0 To count - 1
                     Dim entityType As dsObjectType_e
                     selectedEntities(index) =  New DispatchWrapper(dsSelectionMgr.GetSelectedObject(selectionType, index, entityType))
                 Next
             End If
         End If

         Return selectedEntities
     End Function

     Function ConnectToDraftSight() As DraftSight.Interop.dsAutomation.Application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application =  Nothing

         Try
             'Connect to DraftSight
             dsApp =  DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
         Catch ex As Exception
             MessageBox.Show("Failed to connect to DraftSight. Cause: " & ex.Message)
             dsApp = Nothing
         End Try

         Return dsApp
     End Function
 End Module
```
