---
title: "Get Transform for Each Circular Pattern Instance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm"
---

# Get Transform for Each Circular Pattern Instance Example (VB.NET)

This example shows how to get the transform for each instance in a circular pattern feature.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the circular-pattern feature.
' 3. Get the number of instances in the circular-pattern
'    feature.
' 4. Gets the transform for each instance
'    in the circular-pattern feature.
' 5. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swCircularPatternFeatureData As CircularPatternFeatureData
        Dim swMathTransform As MathTransform
        Dim boolstatus As Boolean
        Dim nErrors As Integer
        Dim nWarnings As Integer
        Dim NbrInstances As Integer
        Dim i As Integer

        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\introtosw\pressure_plate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", nErrors, nWarnings)
        swModelDocExtension = swModel.Extension

        ' Select the circular-pattern feature
        boolstatus = swModelDocExtension.SelectByID2("CirPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swCircularPatternFeatureData = swFeature.GetDefinition

        ' Get the number of instances in the circular-pattern feature
        NbrInstances = swCircularPatternFeatureData.TotalInstances
        Debug.Print("Number of instances: " & NbrInstances)

        ' Get the transform for each instance
        ' in the circular-pattern feature
        For i = 0 To (NbrInstances - 1)
            Debug.Print("  Processing instance " & (i + 1) & "...")
            swMathTransform = swCircularPatternFeatureData.GetTransform(i)
            ' TODO: Do something with the transform
        Next
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
