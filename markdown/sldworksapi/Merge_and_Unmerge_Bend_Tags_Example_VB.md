---
title: "Merge and Unmerge Bend Tags Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_and_Unmerge_Bend_Tags_Example_VB.htm"
---

# Merge and Unmerge Bend Tags Example (VBA)

This example shows how to merge and unmerge bend tags in a drawing.

'---------------------------------------------------------------
' Preconditions:
' 1. The specified drawing document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. The specified drawing document opens.
' 2. Press F5 repeatedly after examining the changes
' in the bend tags and the output in the Immediate window.
'---------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.note
Dim swView As SldWorks.view
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim fileName As String
Dim status As Boolean
Dim errors As Long, warnings As Long
Dim noteList(1) As SldWorks.note

Sub main()

Set swApp = Application.SldWorks
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.slddrw"
swApp.**OpenDoc6** fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings
Set swModel = swApp.**ActiveDoc**
Set swSelectionMgr = swModel.**SelectionManager**
Set swModelDocExt = swModel.**Extension**

Stop
' Locate the bend tags (A, B, C, and D)
' in the drawing
' Press F5 to continue

' Select a bend tag to merge
status = swModelDocExt.**SelectByID2**("DetailItem37@Drawing View1", "NOTE", 9.02750427561398E-02, 0.24484926035503, 0, False, 0, Nothing, 0)
Set swNote = swSelectionMgr.**GetSelectedObject6**(1, 0)
Set noteList(0) = swNote
Debug.Print ("Is a bendline note? " & swNote.**IsBendLineNote**)
swModel.**ClearSelection2** True

' Select another bend tag with which to merge
' the previously selected bend tag
status = swModelDocExt.**SelectByID2**("DetailItem38@Drawing View1", "NOTE", 9.78933563656073E-02, 0.244401124260355, 0, True, 0, Nothing, 0)
Set swNote = swSelectionMgr.**GetSelectedObject6**(1, 0)
Set noteList(1) = swNote
Debug.Print ("Is a bendline note? " & swNote.**IsBendLineNote**)
swModel.**ClearSelection2** True

' Select the drawing view in which to
' merge bend tags
status = swModelDocExt.**SelectByID2**("Drawing View1", "DRAWINGVIEW", 7.65893917313017E-02, 0.16302919597189, 0, False, 0, Nothing, 0)
Set swView = swSelectionMgr.**GetSelectedObject6**(1, 0)
swModel.**ClearSelection2** True

'Merge the selected bend tags
status = swView.**MergeBendTags**(True, noteList)

swModel.EditRebuild3

Stop
' Verify that bend tag A and B merged into
' bend tag A, bend tag C was renamed to B,
' and bend tag D was renamed to C
' Press F5 to continue

' Select the merged bend tag
Set swDrawingDoc = swModel
status = swDrawingDoc.**ActivateView**("Drawing View1")
status = swModelDocExt.**SelectByID2**("DetailItem38@Drawing View1", "NOTE", 0.098037379978424, 0.245097849056604, 0, False, 0, Nothing, 0)
Set swNote = swSelectionMgr.**GetSelectedObject6**(1, 0)
set noteList(0) = swNote

' Unmerge the merged bend tag
swView.**MergeBendTags** False, noteList

Stop
' Verify that bend tag A and B unmerged,
' bend tag B was renamed back to C, and bend tag C
' was renamed back to D
' Press F5 to finish

End Sub
