---
title: "Get Points of Repeating Elements in Table-driven Pattern (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm"
---

# Get Points of Repeating Elements in Table-driven Pattern (VB.NET)

This example shows that the points that describe the locations of the repeating elements in a table-driven pattern are based on the table-driven pattern's coordinate system.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the coordinates of the
'    points for the two repeating elements in the
'    table-driven pattern.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do
' not save changes.
'---------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Public Sub main()

	        Dim swModel As ModelDoc2

	        Dim swModelDocExt As ModelDocExtension

	        Dim swSelMgr As SelectionMgr

	        Dim swFeat As Feature

	        Dim swCoordinateData As CoordinateSystemFeatureData

	        Dim swTablePatternFeatData As TablePatternFeatureData

	        Dim swMathTransform As MathTransform

	        Dim swMathUtility As MathUtility

	        Dim swMathPoint As MathPoint

	        Dim status As Boolean

	        Dim errors As Integer

	        Dim warnings As Integer

	        Dim filename As String

	        Dim points As Object

	        Dim point As String

	        Dim pointsArray(2) As Double

	        Dim i As Integer

	        filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tablepattern.sldprt"

	        swModel = swApp.OpenDoc6(filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "",
	errors, warnings)

	        swModelDocExt = swModel.Extension

	        swSelMgr = swModel.SelectionManager

	        ' Select the table-driven
	pattern

	        status = swModelDocExt.SelectByID2("TPattern1", "BODYFEATURE",
	0, 0, 0, False,
	0, Nothing,
	0)

	        swFeat = swModel.SelectionManager.GetSelectedObject6(1, -1)

	        swTablePatternFeatData = swFeat.GetDefinition

	        swTablePatternFeatData.AccessSelections(swModel, Nothing)

	        ' Get the points of the repeating
	elements in the table-driven pattern

	        '
	and transform them to coordinates

	        swCoordinateData = swTablePatternFeatData.CoordinateSystem.GetDefinition

	        swCoordinateData.AccessSelections(swModel, Nothing)

	        swMathTransform = swCoordinateData.Transform

	        swCoordinateData.ReleaseSelectionAccess()

	        swMathUtility = swApp.GetMathUtility

	        points = swTablePatternFeatData.PointArray
```

```vb
         Debug.Print("Number of points: " & swTablePatternFeatData.GetPointCount)

         For i = 0 To UBound(points) Step 3
             pointsArray(0) = points(i) : pointsArray(1) = points(i + 1) : pointsArray(2) = points(i + 2)
             swMathPoint = swMathUtility.CreatePoint(pointsArray)

             swMathPoint = swMathPoint.MultiplyTransform(swMathTransform.Inverse)

             ' Print the coordinates for the two repeating elements in the table-driven pattern
             point =  "x: " & swMathPoint.ArrayData(0) & " y: " & swMathPoint.ArrayData(1) & " z: " & swMathPoint.ArrayData(2)

             Debug.Print(point)

         Next

         swTablePatternFeatData.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
