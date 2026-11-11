---
title: "Get Distance Between Two Math Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Distance_Between_Two_Math_Points_Example_VBNET.htm"
---

# Get Distance Between Two Math Points Example (VB.NET)

This example shows how to get the distance between two math points.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight.
 ' 6. Run the macro.
 ' 7. Select two points when prompted in the DraftSight command window.
 '
 ' Postconditions: The distance between two math points is printed in
 ' the command window.
 '----------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms

 Module Module1
     Dim dsApp As DraftSight.Interop.dsAutomation.Application

     Sub Main(ByVal args As String())
         'Connect to DraftSight application
         dsApp = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get math utility
         Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()

         'Get distance between two points
         GetDistance(dsMathUtility)
     End Sub

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

     Sub GetDistance(ByVal dsMathUtility As MathUtility)
         'Get command message
         Dim dsCommandMessage As CommandMessage = dsApp.GetCommandMessage()

         dsCommandMessage.PrintLine("Get distance between two points")

         'Prompt to select the first point and second points
         'to calculate the distance between them
         Dim firstX As Double, firstY As Double, firstZ As Double
         Dim secondX As Double, secondY As Double, secondZ As Double
         If dsCommandMessage.PromptForPoint("Specify the first point", firstX, firstY, firstZ) AndAlso dsCommandMessage.PromptForPoint("Specify the second point", secondX, secondY, secondZ) Then
             'Create the first math point
             Dim dsFirstMathPoint As MathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ)

             'Create the second math point
             Dim dsSecondMathPoint As MathPoint = dsMathUtility.CreatePoint(secondX, secondY, secondZ)

             'Get distance between points
             Dim dsResultPoint1 As MathPoint = Nothing
             Dim dsResultPoint2 As MathPoint = Nothing
             Dim distance As Double = dsMathUtility.Distance(dsFirstMathPoint, dsSecondMathPoint, dsResultPoint1, dsResultPoint2)

             'Get result point coordinates
             dsResultPoint1.GetPosition(firstX, firstY, firstZ)
             dsResultPoint2.GetPosition(secondX, secondY, secondZ)

             Dim message As String = String.Format("The distance between ({0},{1},{2}) and ({3},{4},{5}) point is {6}." & vbLf, firstX, firstY, firstZ, secondX, secondY, _
              secondZ, distance)
             dsCommandMessage.PrintLine(message)
         End If
     End Sub
 End Module
```
