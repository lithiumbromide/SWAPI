---
title: "Create Break View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Broken_View_Example_VBNET.htm"
---

# Create Break View Example (VB.NET)

This example shows how to create and remove a broken view.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified file to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing and selects **Drawing View1**.
' 2. Examine the drawing, then press F5.
' 3. Inserts break lines in **Drawing View1**.
' 4. Examine the drawing, then press F5.
' 5. Modifies the positions of the break lines and breaks the view.
' 6. Examine the drawing, then press F5.
' 7. Removes the break from **Drawing View1**.
' 8. Examine the drawing and the Immediate window.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

Public Sub Main()

Dim swModel As ModelDoc2
Dim swDrawingDoc As DrawingDoc
Dim swModelDocExt As ModelDocExtension
Dim swSelectionManager As SelectionMgr
Dim swSelectData As SelectData
Dim swView As View
Dim swBreakLine As BreakLine
Dim fileName As String
Dim status As Boolean
Dim errors As Integer
Dim warnings As Integer

fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
swDrawingDoc = swModel
swModelDocExt = swModel.**Extension**

' Activate and select the view to break
status = swDrawingDoc.**ActivateView**("Drawing View1")
status = swModelDocExt.**SelectByID2**("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
swSelectionManager = swModel.**SelectionManager**
swSelectData = swSelectionManager.**CreateSelectData**
swView = swSelectionManager.**GetSelectedObject6**(1, -1)

Stop
' Examine the drawing; press F5

' Insert the break lines
swBreakLine = swView.**InsertBreak**(0, -0.0291950859897372, 0.0198236302285804, 1)

Stop
' Break lines inserted; press F5

' Reset position of break lines
status = swBreakLine.**SetPosition**(-0.03, 0.05)
swModel.**EditRebuild3**
Debug.Print("Break line: ")
Debug.Print(" Selected: " & swBreakLine.**Select**(True, Nothing))
Debug.Print(" Style: " & swBreakLine.**Style**)
Debug.Print(" Orientation: " & swBreakLine.**Orientation**)
Debug.Print(" Position: " & swBreakLine.**GetPosition**(0))

swDrawingDoc.**BreakView**()

Stop
' Positions of the break lines are modified, and the view is broken
' Press F5

' Remove the break lines
status = swModelDocExt.**SelectByID2**("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
swDrawingDoc.**UnBreakView**()

' Break is removed

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
