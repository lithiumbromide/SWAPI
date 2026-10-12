---
title: "Delete Instances and Dimensions in Variable Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm"
---

# Delete Instances and Dimensions in Variable Pattern Feature Example (VB.NET)

This example shows how to:

- delete instances in a variable pattern feature.
- add and delete dimensions in the pattern table of a variable pattern feature.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part and selects the variable pattern feature.
' 2. Accesses the variable pattern feature.
' 3. Deletes the last and fourth instance from the pattern table
'    and pattern.
' 4. Gets the number and names of the controlling dimensions.
' 5. Selects and adds two dimensions to the pattern table and
'    deletes the second dimension from the pattern table.
' 6. Rolls forward the modified variable pattern feature.
' 7. Examine the graphics area and Immediate window.
'
' NOTE: Because the part used is elsewhere, do not save changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swDimensionDrivenTablePatternFeat As DimPatternFeatureData
	Dim swDisplayDimension As DisplayDimension
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim dimNbr As Integer
        Dim i As Integer
        Dim controllingDimNames() As String
        Dim controllingDimName As String

        'Open part and select the variable pattern feature
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\bottle.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swDimensionDrivenTablePatternFeat = swFeature.GetDefinition

        'Roll back and access the variable pattern feature
        status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, Nothing)

        'Delete the last instance of the variable pattern in the pattern table and pattern
        status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(-1)
        Debug.Print("Last instance of variable pattern deleted from pattern table? " & status)

        'Delete another instance of the variable pattern in the pattern table and pattern
        status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(3)
        Debug.Print("Fourth instance of variable pattern deleted from pattern table? " & status)

        'Get the number and names of the controlling dimensions
        dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount
        Debug.Print("Number of controlling dimensions: " & dimNbr)
        Debug.Print("  Controlling dimension names: ")
        ReDim Preserve controllingDimNames(dimNbr)
        For i = 0 To dimNbr - 1
            controllingDimNames(i) = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i)
            controllingDimName = controllingDimNames(i)
            Debug.Print("     " & controllingDimName)
        Next i
```

```
	'Select two display dimensions and add them to the pattern table
	status = swModelDocExt.SelectByID2("D1@Sketch2@bottle.SLDPRT", "DIMENSION", 0.0176517231321772, 0.0149650532369545, -0.0243235746513165, False, 0, Nothing, 0)
	swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
	status = swDimensionDrivenTablePatternFeat.AddDimension
	If status Then
    		Debug.Print("Added " & swDisplayDimension.GetNameForSelection & " to pattern table")
	End If

	swModel.ClearSelection2(True)

	status = swModelDocExt.SelectByID2("D2@Sketch2@bottle.SLDPRT", "DIMENSION", 0.019517663324148, 0.0297942417761803, -0.0237034236540374, False, 0, Nothing, 0)
	swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
	status = swDimensionDrivenTablePatternFeat.AddDimension
	If status Then
    		Debug.Print("Added " & swDisplayDimension.GetNameForSelection & " to pattern table")
	End If

	'Delete the just-added display dimension from the pattern table
	status = swDimensionDrivenTablePatternFeat.DeleteDimension(swDisplayDimension.GetNameForSelection)
	If status Then
    		Debug.Print("  Deleted " & swDisplayDimension.GetNameForSelection & " from pattern table")
	End If

        swDimensionDrivenTablePatternFeat.PropagateVisualProperties = True

        'Roll forward the variable pattern feature
        swFeature.ModifyDefinition(swDimensionDrivenTablePatternFeat, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
