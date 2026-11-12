---
title: "Change Dimension Tolerance in a Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Tolerance_in_Configuration_Example_VB.htm"
---

# Change Dimension Tolerance in a Configuration Example (VBA)

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
---------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swConfigurationMgr As SldWorks.ConfigurationManager
Dim swConfiguration As SldWorks.Configuration
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim swDimension As SldWorks.Dimension
Dim swDimensionTolerance As SldWorks.DimensionTolerance
Dim status As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open part document with multiple configurations
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\PDMWorks\speaker_frame.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    ' Get name of active configuration
    Set swConfigurationMgr = swModel.ConfigurationManager
    Set swConfiguration = swConfigurationMgr.ActiveConfiguration
    Debug.Print ("Configuration name: " & swConfiguration.Name)
```

```
    ' Select sketch
    ' Put the sketch in edit mode
    ' Select a dimension in the sketch
    status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -4.30195952926557E-03, 3.21813003735837E-02, -1.55776956607312E-02, False, 0, Nothing, 0)
```

```
    ' Get the selection
    Set swSelMgr = swModel.SelectionManager
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, 0)
```

```
    ' If selection is not a display dimension, then exit
    If swSelMgr.GetSelectedObjectType3(1, -1) <> swSelDIMENSIONS Then Exit Sub
```

```
    ' Selection is a dimension, so get the dimension tolerance
    Set swDimension = swDisplayDimension.GetDimension2(0)
    Set swDimensionTolerance = swDimension.Tolerance
```

```
    ' Set type of tolerance type
    swDimensionTolerance.Type = swTolBASIC
```

```
    ' Set new dimension tolerance values
    status = swDimensionTolerance.SetValues2(0.01, 0.015, swSetValueInConfiguration_e.swSetValue_InThisConfiguration, "")
    Debug.Print ("  Minimum dimension tolerance: " & swDimensionTolerance.GetMinValue)
    Debug.Print ("  Maximum dimension tolerance: " & swDimensionTolerance.GetMaxValue)
```

```
    ' Exit sketch edit mode
    swModel.InsertSketch2 True
```

```
    ' Switch configuration to verify
    ' that dimension tolerance changed
    ' in other configuration only
    status = swModel.ShowConfiguration2("Square Cutout Glueable")
    status = swModelDocExt.SelectByID2("Square Cutout Glueable", "CONFIGURATIONS", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Get name of configuration
    Set swConfiguration = swConfigurationMgr.ActiveConfiguration
    Debug.Print ("Configuration name: " & swConfiguration.Name)
```

```
    ' Select sketch
    ' Select same dimension in sketch as selected
    ' in previously active configuration
    ' Put the sketch in edit mode
    status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -4.71220094479408E-03, 0.032305394835097, -1.53009205936774E-02, False, 0, Nothing, 0)
```

```
    ' Get the selection
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, 0)
```

```
    ' If selection is not a display dimension, then exit
    If swSelMgr.GetSelectedObjectType3(1, -1) <> swSelDIMENSIONS Then Exit Sub
```

```
    ' Selection is a dimension, so get and print the dimension tolerance
    Set swDimension = swDisplayDimension.GetDimension2(0)
    Set swDimensionTolerance = swDimension.Tolerance
    Debug.Print ("  Minimum dimension tolerance: " & swDimensionTolerance.GetMinValue)
    Debug.Print ("  Maximum dimension tolerance: " & swDimensionTolerance.GetMaxValue)
```

```
   ' Exit sketch edit mode
   swModel.InsertSketch2 True
```

```
End Sub
```
