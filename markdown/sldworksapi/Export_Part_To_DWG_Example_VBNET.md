---
title: "Export Part to DWG Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_Part_To_DWG_Example_VBNET.htm"
---

# Export Part to DWG Example (VB.NET)

This example shows how to export sheet metal and annotation views of a part to DWG files.

```
'---------------------------------------------------------------------------
' Preconditions: Copy public_documents\samples\tutorial\api\2012-sm.sldprt to
' c:\temp.
'
' Postconditions:
' 1. Creates three DWG files containing:
'    * Current annotation view
'    * Front annotation view
'    * flat-pattern sheet metal
' 2. Locate and open the just-created DWG files in c:\temp.
'--------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swPart As PartDoc

	    Dim sModelName As String

	    Dim sPathName As String

	    Dim varAlignment As Object

	    Dim dataAlignment(11) As Double

	    Dim varViews As Object

	    Dim dataViews(1) As String

	    Dim options As Integer

	    Sub main()

	        swModel = swApp.ActiveDoc

	        sModelName = swModel.GetPathName

	        sPathName = swModel.GetPathName

	        sPathName = Left(sPathName, Len(sPathName) - 6)

	        sPathName = sPathName + "dwg"

	        swPart = swModel

	        dataAlignment(0) = 0.0#

	        dataAlignment(1) = 0.0#

	        dataAlignment(2) = 0.0#

	        dataAlignment(3) = 1.0#

	        dataAlignment(4) = 0.0#

	        dataAlignment(5) = 0.0#

	        dataAlignment(6) = 0.0#

	        dataAlignment(7) = 1.0#

	        dataAlignment(8) = 0.0#

	        dataAlignment(9) = 0.0#

	        dataAlignment(10) = 0.0#

	        dataAlignment(11) = 1.0#

	        varAlignment = dataAlignment

	        dataViews(0) = "*Current"

	        dataViews(1) = "*Front"

	        varViews = dataViews

	        'Export each annotation view to a
	separate drawing file

	        swPart.ExportToDWG2(sPathName, sModelName, swExportToDWG_e.swExportToDWG_ExportAnnotationViews, False, varAlignment, False, False, 0, varViews)

	        'Export sheet metal to a single
	drawing file

	        options = 1   'include flat-pattern geometry

	        swPart.ExportToDWG2(sPathName, sModelName, swExportToDWG_e.swExportToDWG_ExportSheetMetal, True, varAlignment, False, False,
	options, Nothing)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
