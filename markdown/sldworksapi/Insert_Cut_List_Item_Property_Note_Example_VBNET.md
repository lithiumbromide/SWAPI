---
title: "Insert Cut List Item Property Note Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_List_Item_Property_Note_Example_VBNET.htm"
---

# Insert Cut List Item Property Note Example (VB.NET)

This example shows how to insert a note containing all of the cut list item properties into the selected flat pattern drawing view of a sheet metal part.

```
'---------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\2012-sm.slddrw.
'
' Postconditions:
' 1. Inserts a note with all of the cut list item properties in Drawing View1.
' 2. Examine the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim SelMgr As SelectionMgr

	    Dim aView As View

	    Dim boolstatus As Boolean

	    Sub main()

	        Part = swApp.ActiveDoc

	        boolstatus = Part.Extension.SelectByID2("Drawing
	View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)

	        SelMgr = Part.SelectionManager

	        aView = SelMgr.GetSelectedObject6(1, -1)

	        aView.InsertCutListPropertyNote(0.11, 0.17, 0.0#)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
