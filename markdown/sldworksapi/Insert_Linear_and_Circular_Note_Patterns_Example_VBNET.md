---
title: "Insert Linear and Circular Note Patterns (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Linear_and_Circular_Note_Patterns_Example_VBNET.htm"
---

# Insert Linear and Circular Note Patterns (VB.NET)

This example shows how to insert linear and circular note patterns in a drawing.

'---------------------------------------------------------
' Preconditions: Verify that the specified drawing document
' to open exists.
'
' Postconditions:
' 1. Inserts a note in the drawing and selects the note.
' 2. Inserts a linear note pattern (2 instances, including the
' original note) in the drawing.
' 3. Inserts a circular note pattern (4 instances, including
' the original note) in the drawing.
'
' NOTE: Because the model is used elsewhere, do not save
' changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

Public Sub Main()

Dim swModel As ModelDoc2
Dim swDrawingDoc As DrawingDoc
Dim swNote As Note
Dim status As Boolean
Dim errors As Integer
Dim warnings As Integer

' Open drawing document, activate sheet, and make it the active document
swModel = swApp.**OpenDoc6**("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", 3, 0, "", errors, warnings)
swApp.**ActivateDoc2**("foodprocessor - Sheet1", False, errors)
swDrawingDoc = swApp.**ActiveDoc**

' Insert a note
swNote = swModel.**InsertNote**("Test inserting linear and circular note patterns")

' Select the just-inserted note
status = swModel.Extension.**SelectByID2**("DetailItem174@Sheet1", "NOTE", 0.2558797881203, 0.3700526, 0, False, 0, Nothing, 0)

' Create a linear note pattern using the selected note
status = swDrawingDoc.**InsertLinearNotePattern**(2, 1, 0.01, 0.01, 0.7853981633975, 1.570796326795, "")

' Create a circular pattern using the selected note
status = swDrawingDoc.**InsertCircularNotePattern**(0.075, 4.03202193189, -4, 1.570796326795, True, "")

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
