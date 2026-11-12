---
title: "Create Cut-sweep Feature Using Circular Profile Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Circular_Profile_Example_VBNET.htm"
---

# Create Cut-sweep Feature Using Circular Profile Example (VB.NET)

This example shows how to create a cut-sweep feature using a circular profile.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects an edge on the part.
' 3. Creates a cut-sweep feature using a circular
'    profile.
' 4. Accesses the cut-sweep feature.
' 5. Changes the diameter of the circular profile.
' 6. Examine the Immediate window, FeatureManager
'    design tree, and graphics area.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'------------------------------------------------
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
        Dim swFeatureManager As FeatureManager
        Dim swSweepFeatureData As SweepFeatureData
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Select the edge for the cut-sweep feature
        status = swModelDocExt.SelectByID2("", "EDGE", -0.0372983839416747, 0.0393904284381961, 0.0495042874504179, True, 4, Nothing, 0)
        swFeatureManager = swModel.FeatureManager

        'Create the cut-sweep feature using a circular profile
        swFeature = swFeatureManager.InsertCutSwept5(False, True, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, True, 0, True, True, True, False, True, 0.0254, swSweepDirection_e.swSweepDirection1)

        'Roll back the cut-sweep feature to access and change the diameter of circular profile
        swSweepFeatureData = swFeature.GetDefinition
        status = swSweepFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Using a circular profile? " & swSweepFeatureData.CircularProfile)
        Debug.Print("Original size of circular profile = " & swSweepFeatureData.CircularProfileDiameter)
        swSweepFeatureData.CircularProfileDiameter = 0.003
        Debug.Print("Modified size of circular profile = " & swSweepFeatureData.CircularProfileDiameter)
        Debug.Print("Direction of cut-sweep = " & swSweepFeatureData.Direction)

        'Roll forward the cut-sweep feature
        swFeature.ModifyDefinition(swSweepFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
