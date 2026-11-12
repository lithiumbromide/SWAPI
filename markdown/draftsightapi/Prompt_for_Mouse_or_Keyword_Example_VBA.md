---
title: "Prompt for Mouse or Keyword Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Prompt_for_Mouse_or_Keyword_Example_VBA.htm"
---

# Prompt for Mouse or Keyword Example (VBA)

This example shows how to create a prompting cursor (tracker) that displays a simple note as you prompt the user for where to insert the simple note in the graphics area.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
' embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' a. In Modules, copy and paste the [Main module](#Main_module).
' b. Insert a class called Class1, and paste the [Class1 module](#Class1_module).
' 3. Add a reference to the DraftSight type library,
' `install_dir`\**bin\dsAutomation.dll**.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions:
' 1. Prompts the user for some text and its properties.
' 2. Creates a prompting tracker with the text.
' 3. Prompts the user for the insertion point of the text.
' 4. Inserts the text at the user-specified location.
'----------------------------------------------------------------

```vb
 'Main module
 Public m_note As DraftSight.SimpleNote
 Public dsTrackerEvent As Class1

     Sub Main()

         Dim Application As DraftSight.Application
         Set Application = GetObject(, "DraftSight.Application")

         If Application Is Nothing Then
                 Return
             End If

             Application.AbortRunningCommand
             Dim dsCommandMessage As DraftSight.CommandMessage
             Set dsCommandMessage = Application.GetCommandMessage()

             If dsCommandMessage Is Nothing Then
                 Return
             End If

             Dim dsDoc As DraftSight.Document
             Set dsDoc = Application.GetActiveDocument()

             If dsDoc Is Nothing Then
                 Return
             End If

             Dim dsMathUtility As DraftSight.MathUtility
             Set dsMathUtility = Application.GetMathUtility()

             If dsMathUtility Is Nothing Then
                 Return
             End If

             Dim dsModel As DraftSight.Model
             Set dsModel = dsDoc.GetModel()

             If dsModel Is Nothing Then
                 Return
             End If

             Dim dsSketchManager As DraftSight.SketchManager
             Set dsSketchManager = dsModel.GetSketchManager()

             If dsSketchManager Is Nothing Then
                 Return
             End If

             Dim result As Boolean
             Dim text As String
             text = "Hello, World!"
             Dim height As Double
             height = 1.2
             Dim angle As Double
             angle = 0
             Dim x As Double
             x = 0
             Dim y As Double
             y = 0
             Dim z As Double
             z = 0
             result = dsCommandMessage.PromptForString(True, "Specify text", "Hello, World!", text)
             If Not result Then Return
             result = dsCommandMessage.PromptForDouble("Specify text height", 1.2, height)
             If Not result Then Return
             result = dsCommandMessage.PromptForDouble("Specify text angle [deg]", 0, angle)
             If Not result Then Return
             angle = angle * 3.14159265358979 / 180
             result = dsCommandMessage.PromptForPoint("Specify insertion point", x, y, z)
             If Not result Then Return
             Application.TemporaryEntityMode = True
             Set m_note = dsSketchManager.InsertSimpleNote(x, y, z, height, angle, text)
             Application.TemporaryEntityMode = False
             Dim tracker As tracker
             Set tracker = Application.CreateTracker()
             tracker.AddTemporaryEntity m_note

              'Set up event
             Set dsTrackerEvent = New Class1
             Set dsTrackerEvent.myTracker = tracker

             dsCommandMessage.AddTracker tracker

             Dim keyword As String
             keyword = ""
             Dim global_keywords As Object
             Dim local_keywords As Object
             Dim default_point As DraftSight.MathPoint
             Dim base_point As DraftSight.MathPoint
             Set base_point = dsMathUtility.CreatePoint(0, 0, 0)
             Dim insertion_point As DraftSight.MathPoint
             Set default_point = dsMathUtility.CreatePoint(0, 0, 0)
             Dim xy_plane As DraftSight.MathPlane
             Set xy_plane = dsMathUtility.CreateXYPlane()

             Dim dsPromptResult As dsPromptResultType_e
             dsPromptResult = dsPromptResultType_e.dsPromptResultType_None
             Dim keyboardModificator As dsPromptKeyboardModificators2_e
             keyboardModificator = dsPromptKeyboardModificators2_e.dsPromptKeyboardModificators_Unknown
             Dim mouseEvnt As dsMouseEventType_e
             mouseEvnt = dsMouseEventType_e.dsMouseEventType_Unknown

             dsPromptResult = dsCommandMessage.PromptForMouseOrKeyword2("Specify insertion point", "Invalid input", global_keywords, local_keywords, 0, False, default_point, base_point, xy_plane, keyword, insertion_point, keyboardModificator, mouseEvnt)

             dsCommandMessage.PrintLine (vbLf)
             dsCommandMessage.PrintLine ("Keyboard modificator: " & keyboardModificator)
             dsCommandMessage.PrintLine (vbLf)
             dsCommandMessage.PrintLine ("Mouse event: " & mouseEvnt)
             dsCommandMessage.PrintLine (vbLf)

             insertion_point.GetPosition x, y, z
             m_note.SetPosition x, y, z
             dsSketchManager.AddTemporaryEntity m_note

             dsCommandMessage.RemoveTracker tracker

         End Sub
```

'Class1 module

```vb
 Option Explicit
 Public WithEvents myTracker As DraftSight.tracker
 Public Sub myTracker_UpdateNotify(ByVal CursorPosition As DraftSight.MathPoint)
         If CursorPosition Is Nothing Then
             Return
         End If

         Dim x As Double
         x = 0#
         Dim y As Double
         y = 0#
         Dim z As Double
         z = 0#

         CursorPosition.GetPosition x, y, z
         m_note.SetPosition x, y, z
 End Sub
```
