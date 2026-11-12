---
title: "Get Distance Between Two Math Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Distance_Between_Two_Math_Points_Example_VBA.htm"
---

# Get Distance Between Two Math Points Example (VBA)

This example shows how to get the distance between two math points.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Start DraftSight.
 ' 5. Run the macro.
 ' 6. Select two points when prompted in the DraftSight command window.
 '
 ' Postconditions: The distance between two math points is printed in
 ' the DraftSight command window.
 '----------------------------------------------------------------
 Option Explicit
 Dim dsApp As DraftSight.Application
Sub Main()
     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")
     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand
    'Get active document
     Dim dsDoc As DraftSight.Document
     Set dsDoc = dsApp.GetActiveDocument
     If dsDoc Is Nothing Then
         MsgBox ("There are no open documents in DraftSight.")
         Return
     End If
    'Get math utility
     Dim dsMathUtility As DraftSight.MathUtility
     Set dsMathUtility = dsApp.GetMathUtility
    'Get distance between two points
     Call GetDistance(dsMathUtility)
 End Sub

Sub GetDistance(dsMathUtility As DraftSight.MathUtility)
     'Get command message
     Dim dsCommandMessage As DraftSight.CommandMessage
     Set dsCommandMessage = dsApp.GetCommandMessage
    dsCommandMessage.PrintLine ("Get distance between two points")
    'Prompt to select the first point and second points
     'to calculate the distance between them
     Dim firstX As Double, firstY As Double, firstZ As Double
     Dim secondX As Double, secondY As Double, secondZ As Double
     If dsCommandMessage.PromptForPoint("Specify the first point", firstX, firstY, firstZ) And dsCommandMessage.PromptForPoint("Specify the second point", secondX, secondY, secondZ) Then
         'Create the first math point
         Dim dsFirstMathPoint As DraftSight.MathPoint
         Set dsFirstMathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ)
        'Create the second math point
         Dim dsSecondMathPoint As DraftSight.MathPoint
         Set dsSecondMathPoint = dsMathUtility.CreatePoint(secondX, secondY, secondZ)
        'Get distance between points
         Dim dsResultPoint1 As DraftSight.MathPoint
         Dim dsResultPoint2 As DraftSight.MathPoint
         Dim distance As Double
         distance = dsMathUtility.Distance(dsFirstMathPoint, dsSecondMathPoint, dsResultPoint1, dsResultPoint2)
        'Get result point cordinates
         dsResultPoint1.GetPosition firstX, firstY, firstZ
         dsResultPoint2.GetPosition secondX, secondY, secondZ
        Dim message As String
         message = "The distance between " & firstX & ", " & firstY & ", " & firstZ & " and " & secondX & ", " & secondY & ", " & secondZ & " points is " & distance
         dsCommandMessage.PrintLine (message)
     End If
 End Sub
```
