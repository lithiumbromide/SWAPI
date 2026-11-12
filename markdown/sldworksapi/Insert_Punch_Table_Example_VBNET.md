---
title: "Insert Punch Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Punch_Table_Example_VBNET.htm"
---

# Insert Punch Table Example (VB.NET)

This example shows how to insert a punch table in the flat pattern view of a sheet metal part that contains one or more forming tool features.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains a flat pattern view of a sheet
'    metal part with one or more forming tool features.
' 2. Modify the x- and y-coordinates in the IModelDocExtension::SelectByID2
'    methods for the specified VERTEX and FACE.
' 3. Verify that the punch table template exists.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a punch table in the drawing.
' 2. Inspect the Immediate window for punch table feature details.
' ---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim boolstatus As Boolean

	    Dim myView As View

	    Dim myTableAnn As PunchTableAnnotation

	    Dim MyTable As PunchTable

	    Dim featRet As Feature

	    Dim rVar As Object

	    Sub main()

	        Part = swApp.ActiveDoc

	        boolstatus = Part.ActivateView("Drawing View1")

	        boolstatus = Part.Extension.SelectByID2("Drawing
	View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)

	        'Select a vertex in the drawing
	view to be the origin of all datums in the table

	        'All
	X LOCATION and Y LOCATION table column values will be relative to this datum
	origin

	        boolstatus =
	Part.Extension.SelectByID2("", "VERTEX",
	0.1344949308616, 0.0948467785893, 0, False,
	1, Nothing,
	0)

	        'Select a face that contains the
	punches that will be annotated in the table

	        boolstatus =
	Part.Extension.SelectByID2("", "FACE",
	0.1562337360869, 0.1059474450873, 0, True,
	2, Nothing,
	0)

	        myView = Part.SelectionManager.GetSelectedObjectsDrawingView(1)

	        myTableAnn = myView.InsertPunchTable(False,
	0.2178779310824, 0.2022819591903, 1, "A", "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\punchtable-standard.sldpuntbt")

	        If myTableAnn Is Nothing Then MsgBox("Failed to insert Punch Table")

	        MyTable = myTableAnn.PunchTable

	        Debug.Print("Default punch table
	properties:")

	        Debug.Print("")

	        Debug.Print("Tag style (swPunchTableTagStyle_e):
	" & MyTable.TagStyle)

	        Debug.Print("Starting tag: " & MyTable.StartingValue)

	        Debug.Print("Merge cells with the
	punch ID for a given tag? " & MyTable.CombineSameSize)

	        Debug.Print("Combine rows with
	the same punch ID? " & MyTable.CombineTags)

	        Debug.Print("Display dual
	dimensions? " & MyTable.DualDimensions)

	        Debug.Print("Display units for
	dual dimensions? " & MyTable.ShowUnits)

	        Debug.Print("Punch table
	annotation count: " & MyTable.GetTableAnnotationCount)

	        rVar = MyTable.GetTableAnnotations

	        featRet = MyTable.GetFeature

	        Debug.Print("Feature name: " & featRet.Name)

	        Part.ClearSelection2(True)

	        boolstatus = Part.ActivateSheet("Sheet1")

	    End Sub

	    Public swApp As SldWorks

	End Class
```
