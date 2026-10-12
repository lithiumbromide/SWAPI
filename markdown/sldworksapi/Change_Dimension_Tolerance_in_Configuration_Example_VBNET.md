---
title: "Change Dimension Tolerance in a Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Tolerance_in_Configuration_Example_VBNET.htm"
---

# Change Dimension Tolerance in a Configuration Example (VB.NET)

This example shows how to change the dimension tolerance in one configuration in a multi-configuration part.

```
'--------------------------------------------
' Preconditions:
' 1. Ensure that the specified part document exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens specified document.
' 2. Selects a sketch and a dimension
'    in that sketch.
' 3. Changes the tolerance values of the selected
'    dimension in the sketch and prints the values
'    to the Immediate window.
' 4. Changes configuration.
' 5. Selects the same sketch and dimension
'    in the sketch in this configuration.
' 6. Prints the tolerance values of the dimension
'    to the Immediate window.
' 7. Examine the Immediate window to verify that
'    the tolerance values of the sketch in the
'    different configurations are different.
'
' NOTE: Because this part document is used elsewhere,
' do not save any changes when closing it.
'---------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swConfigurationMgr As ConfigurationManager
        Dim swConfiguration As Configuration
        Dim swSelMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim swDimension As Dimension
        Dim swDimensionTolerance As DimensionTolerance
        Dim status As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        ' Open part document with multiple configurations
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\PDMWorks\speaker_frame.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Get name of active configuration
        swConfigurationMgr = swModel.ConfigurationManager
        swConfiguration = swConfigurationMgr.ActiveConfiguration
        Debug.Print("Configuration name: " & swConfiguration.Name)

        ' Select sketch
        ' Put the sketch in edit mode
        ' Select a dimension in the sketch
        status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -0.00430195952926557, 0.0321813003735837, -0.0155776956607312, False, 0, Nothing, 0)

        ' Get the selection
        swSelMgr = swModel.SelectionManager
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, 0)

        ' If selection is not a display dimension, then exit
        If swSelMgr.GetSelectedObjectType3(1, -1) <> swSelectType_e.swSelDIMENSIONS Then Exit Sub

        ' Selection is a dimension, so get the dimension tolerance
        swDimension = swDisplayDimension.GetDimension2(0)
        swDimensionTolerance = swDimension.Tolerance

        ' Set type of tolerance type
        swDimensionTolerance.Type = swTolType_e.swTolBASIC

        ' Set new dimension tolerance values
        status = swDimensionTolerance.SetValues2(0.01, 0.015, swSetValueInConfiguration_e.swSetValue_InThisConfiguration, "")
        Debug.Print("  Minimum dimension tolerance: " & swDimensionTolerance.GetMinValue)
        Debug.Print("  Maximum dimension tolerance: " & swDimensionTolerance.GetMaxValue)

        ' Exit sketch edit mode
        swModel.InsertSketch2(True)

        ' Switch configuration to verify
        ' that dimension tolerance changed
        ' in other configuration only
        status = swModel.ShowConfiguration2("Square Cutout Glueable")
        status = swModelDocExt.SelectByID2("Square Cutout Glueable", "CONFIGURATIONS", 0, 0, 0, False, 0, Nothing, 0)

        ' Get name of configuration
        swConfiguration = swConfigurationMgr.ActiveConfiguration
        Debug.Print("Configuration name: " & swConfiguration.Name)

        ' Select sketch
        ' Select same dimension in sketch as selected
        ' in previously active configuration
        ' Put the sketch in edit mode
        status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -0.00471220094479408, 0.032305394835097, -0.0153009205936774, False, 0, Nothing, 0)

        ' Get the selection
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, 0)

        ' If selection is not a display dimension, then exit
        If swSelMgr.GetSelectedObjectType3(1, -1) <> swSelectType_e.swSelDIMENSIONS Then Exit Sub

        ' Selection is a dimension, so get and print the dimension tolerance
        swDimension = swDisplayDimension.GetDimension2(0)
        swDimensionTolerance = swDimension.Tolerance
        Debug.Print("  Minimum dimension tolerance: " & swDimensionTolerance.GetMinValue)
        Debug.Print("  Maximum dimension tolerance: " & swDimensionTolerance.GetMaxValue)

        ' Exit sketch edit mode
        swModel.InsertSketch2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
