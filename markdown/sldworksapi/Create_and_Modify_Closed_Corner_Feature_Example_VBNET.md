---
title: "Create and Modify Closed Corner Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm"
---

# Create and Modify Closed Corner Feature Example (VB.NET)

This example shows how to create and modify a closed corner feature in a sheet metal part.

'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified sheet metal part document to
' open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet metal part document.
' 2. Selects two faces.
' 3. Inserts a closed corner feature.
' 4. Modifies properties of the closed corner feature.
' 5. Examine the graphics area and Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

Public Sub main()

Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim swFeature As Feature
Dim swSelectionMgr As SelectionMgr
Dim swClosedCornerFeatureData As ClosedCornerFeatureData
Dim status As Boolean
Dim errors As Integer
Dim warnings As Integer
Dim fileName As String
Dim faces() As Object
Dim swFace As Face2
Dim i As Integer

fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\sheetmetal\formtools\cover.sldprt"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
swModelDocExt = swModel.**Extension**
swSelectionMgr = swModel.**SelectionManager**

'Select the faces for the closed corner feature
status = swModelDocExt.**SelectByID2**("", "FACE", 0.0110595835492404, 0.0280018934407167, 0.0497348782814129, True, 1, Nothing, 0)
status = swModelDocExt.**SelectByID2**("", "FACE", 0.0181424245698736, 0.0110595835492404, 0.0495671179450028, True, 1073741824, Nothing, 0)

'Insert the closed corner feature
swModel.**InsertSheetMetalClosedCorner**()

'Select the closed corner feature
status = swModelDocExt.**SelectByID2**("Closed Corner1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
swFeature = swSelectionMgr.**GetSelectedObject6**(1, -1)
swClosedCornerFeatureData = swFeature.**GetDefinition**

'Access closed corner feature
status = swClosedCornerFeatureData.**AccessSelections**(swModel, Nothing)
Debug.Print("Original properties: ")
Debug.Print(" Corner type: " & swClosedCornerFeatureData.**CornerType**)
Debug.Print(" Gap distance: " & swClosedCornerFeatureData.**GapDistance**)
Debug.Print(" Open bend region? " & swClosedCornerFeatureData.**OpenBendRegion**)
Debug.Print(" Overlap/underlap ratio: " & swClosedCornerFeatureData.**OverlapUnderlapRatio**)
faces = swClosedCornerFeatureData.**Faces**
For i = 0 To UBound(faces)
swFace = faces(i)
Debug.Print(" Area of face " & i & ": " & swFace.**GetArea** * 1000 & " mm")
Next i
Debug.Print("Modified properties: ")
swClosedCornerFeatureData.**CornerType** = swClosedCornerTypes_e.swClosedCornerTypeUnderlap
swClosedCornerFeatureData.**GapDistance** = 0.005
swClosedCornerFeatureData.**OpenBendRegion** = True
swClosedCornerFeatureData.**OverlapUnderlapRatio** = 0.5
Debug.Print(" Corner type: " & swClosedCornerFeatureData.**CornerType**)
Debug.Print(" Gap distance: " & swClosedCornerFeatureData.**GapDistance**)
Debug.Print(" Open bend region? " & swClosedCornerFeatureData.**OpenBendRegion**)
Debug.Print(" Overlap/underlap ratio: " & swClosedCornerFeatureData.**OverlapUnderlapRatio**)

status = swFeature.**ModifyDefinition**(swClosedCornerFeatureData, swModel, Nothing)

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
