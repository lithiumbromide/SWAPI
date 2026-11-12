---
title: "Change Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Example_VBNET.htm"
---

# Change Dimension Example (VB.NET)

This example shows how to change a dimension value in a model.

#### NOTE: Most of the SOLIDWORKS API functions operate in meters. Thus, if you pass in XValue_Passed = 2.0 and your model units are millimeters, then it appears as a 2000.0 in the model. If you need to determine the units used in the model, you can use the IModelDoc2::LengthUnit property and perform the appropriate conversion.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Changes the specified dimension parameter of the selected feature.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swFeature As Feature

	    Dim swSelectionManager As SelectionMgr

	    Dim swDim As Dimension

	    Dim fileName As String

	    Dim boolstatus As Boolean

	    Dim errors As Integer

	    Dim warnings As Integer

	    Sub main()

	        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"

	        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "",
	errors, warnings)

	        boolstatus = swModel.Extension.SelectByID2("LocalCirPattern1", "COMPPATTERN",
	0, 0, 0, False,
	0, Nothing,
	0)

	        swSelectionManager = swModel.SelectionManager

	        swFeature = swSelectionManager.GetSelectedObject6(1, -1)

	        swDim = swFeature.Parameter("D3")

	' Get D3 of LocalCirPattern1
	Debug.Print("D3@LocalCirPattern1 is " & swDim.SystemValue & " before changing it.")

	        ' Change D3 of LocalCirPattern1
	from 360 degrees to 270 degrees (4.72 radians)

	        errors = swDim.SetSystemValue3(4.72, swSetValueInConfiguration_e.swSetValue_InThisConfiguration, Nothing)

	        swModel.EditRebuild3()

	        swDim = swFeature.Parameter("D3")

	        Debug.Print("D3@LocalCirPattern1 is " & swDim.SystemValue & " after changing it.")

	    End Sub

	    Public swApp As SldWorks

	End Class
```
