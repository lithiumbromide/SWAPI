---
title: "Insert Forming Tool Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Form_Tool_Feature_Example_VBNET.htm"
---

# Insert Forming Tool Feature Example (VB.NET)

This example shows how to insert a forming tool feature into a sheet metal
part.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Verify that the specified forming tool part exists.
' 3. Select a face on which to apply the counter sink emboss forming tool from
'    the Design Library.
'
' Postconditions:
' 1. Inserts the counter sink emboss1 feature.
' 2. Examine the FeatureManager design tree and graphics area.
' ---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim myFeature As Feature

    Dim formingTool as String

	    Sub main()

	        Part = swApp.ActiveDoc

	        ' Insert a counter sink emboss
	forming tool feature

        formingTool = "C:\ProgramData\SolidWorks\SOLIDWORKS
	2025\design library\forming tools\embosses\counter sink emboss.sldprt"

	        myFeature = Part.FeatureManager.InsertFormToolFeature(formingTool, False,
	0.0#, "", True, True, True, True, False)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
