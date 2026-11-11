---
title: "Prompt for Mouse or Keyword Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Prompt_for_Mouse_or_Keyword_Example_VBNET.htm"
---

# Prompt for Mouse or Keyword Example (VB.NET)

This example shows how to create a prompting cursor (tracker) that displays a simple note as you prompt the user for where to insert the simple note in the graphics area.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to
' `install_dir\`**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
' 4. Start DraftSight.
' 5. Press F5 to debug the project.
'
' Postconditions:
' 1. Prompts the user for some text and its properties.
' 2. Creates a prompting tracker with the text.
' 3. Prompts the user for the insertion point of the text.
' 4. Inserts the text at the user-specified location.
'----------------------------------------------------------------

```vb
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Runtime.InteropServices
 Imports DraftSight.Interop.dsAutomation

 Module   Module1

       Dim m_note  As SimpleNote
       Public  WithEvents tracker  As Tracker

       Sub Main()

            Dim Application  As DraftSight.Interop.dsAutomation.Application
           Application =   CType(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

            If application  Is   Nothing   Then
                   Return
              End  If

              application.AbortRunningCommand()
               Dim dsCommandMessage  As CommandMessage = application.GetCommandMessage()

               If dsCommandMessage  Is   Nothing   Then
                   Return
               End  If

               Dim dsDoc  As Document = application.GetActiveDocument()

               If dsDoc  Is  Nothing   Then
                   Return
               End  If

               Dim dsMathUtility  As MathUtility = application.GetMathUtility()

               If dsMathUtility  Is   Nothing   Then
                   Return
               End  If

               Dim dsModel  As Model = dsDoc.GetModel()

               If dsModel  Is  Nothing   Then
                   Return
               End  If

               Dim dsSketchManager  As SketchManager = dsModel.GetSketchManager()

               If dsSketchManager  Is   Nothing   Then
                   Return
               End  If

               Dim result  As  Boolean
               Dim text  As  String =   "Hello, World!"
               Dim height  As  Double = 1.2
               Dim angle  As  Double = 0
               Dim x  As  Double = 0, y  As  Double = 0, z  As   Double = 0
              result = dsCommandMessage.PromptForString(True,  "Specify text", text, text)
               If  Not result  Then  Return
              result = dsCommandMessage.PromptForDouble("Specify text height", height, height)
               If  Not result  Then  Return
              result = dsCommandMessage.PromptForDouble("Specify text angle [deg]", angle, angle)
               If  Not result  Then  Return
              angle = angle * 3.1415926535897931 / 180
              result = dsCommandMessage.PromptForPoint("Specify insertion point", x, y, z)
               If  Not result  Then  Return
              application.TemporaryEntityMode =   True
              m_note = dsSketchManager.InsertSimpleNote(x, y, z, height, angle, text)
              application.TemporaryEntityMode =   False
               Dim tracker  As Tracker = application.CreateTracker()
              tracker.AddTemporaryEntity(m_note)
               dsCommandMessage.AddTracker(tracker)
                AddHandler tracker.UpdateNotify,   AddressOf UpdateNotify
                Dim keyword  As  String =   ""
                Dim global_keywords  As   Object =   Nothing
                Dim local_keywords  As   Object =   Nothing
                Dim insertion_point  As MathPoint = dsMathUtility.CreatePoint(0, 0, 0)
               Dim xy_plane  As MathPlane = dsMathUtility.CreateXYPlane()
               Dim dsPromptResult  As dsPromptResultType_e = dsPromptResultType_e.dsPromptResultType_None
               Dim keyboardModificator  As dsPromptKeyboardModificators2_e = dsPromptKeyboardModificators2_e.dsPromptKeyboardModificators_Unknown
               Dim mouseEvnt  As dsMouseEventType_e = dsMouseEventType_e.dsMouseEventType_Unknown
              dsPromptResult = dsCommandMessage.PromptForMouseOrKeyword2("Specify insertion point",   "Invalid input", global_keywords, local_keywords, 0,   False, insertion_point, insertion_point, xy_plane, keyword, insertion_point, keyboardModificator, mouseEvnt)
              dsCommandMessage.PrintLine(vbLf)
              dsCommandMessage.PrintLine("Keyboard modificator: " & keyboardModificator.ToString())
              dsCommandMessage.PrintLine(vbLf)
               dsCommandMessage.PrintLine("Mouse event: " & mouseEvnt.ToString())
               dsCommandMessage.PrintLine(vbLf)
                RemoveHandler tracker.UpdateNotify,  AddressOf UpdateNotify
               dsCommandMessage.RemoveTracker(tracker)
               insertion_point.GetPosition(x, y, z)
               m_note.SetPosition(x, y, z)
               dsSketchManager.AddTemporaryEntity(m_note)
            End  Sub

        Public   Sub UpdateNotify(ByVal CursorPosition  As MathPoint)   Handles tracker.UpdateNotify
            If CursorPosition  Is   Nothing   OrElse m_note  Is   Nothing   Then   Return
            Dim x  As  Double = 0.0, y  As  Double = 0.0, z  As   Double = 0.0
           CursorPosition.GetPosition(x, y, z)
           m_note.SetPosition(x, y, z)
       End  Sub

 End  Module
```
