---
title: "Get Drawing View Names and Types Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Drawing_View_Names_and_Types_Example_VBNET.htm"
---

# Get Drawing View Names and Types Example (VB.NET)

This example shows how to get the names and types of all of the drawing views on the current sheet.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the views on the current sheet and gets each view's type.
' 2. Inspect the Immediate window.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Sub main()

	        Dim swModel As ModelDoc2

	        Dim swDraw As DrawingDoc

	        Dim swSheet As Sheet

	        Dim swView As View

	        swModel = swApp.ActiveDoc

	        swDraw = swModel

	        swSheet = swDraw.GetCurrentSheet

	        swView = swDraw.GetFirstView

	        Debug.Print("File = " & swModel.GetPathName)

	        Debug.Print("  " & swSheet.GetName)

	        While Not swView Is Nothing

	            Debug.Print("    " & swView.GetName2 & " [" & swView.Type & "]")

	            swView = swView.GetNextView

	        End While

	    End Sub

	    Public swApp As SldWorks

	End Class
```
