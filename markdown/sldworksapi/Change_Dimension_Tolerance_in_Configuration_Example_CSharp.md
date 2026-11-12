---
title: "Change Dimension Tolerance in a Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Tolerance_in_Configuration_Example_CSharp.htm"
---

# Change Dimension Tolerance in a Configuration Example (C#)

This example shows how to change the dimension tolerance in one configuration in a multi-configuration part.

```
//--------------------------------------------
// Preconditions:
// 1. Ensure that the specified part document exists.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Opens specified document.
// 2. Selects a sketch and a dimension
//    in that sketch.
// 3. Changes the tolerance values of the selected
//    dimension in the sketch and prints the values
//    to the Immediate window.
// 4. Changes configuration.
// 5. Selects the same sketch and dimension
//    in the sketch in this configuration.
// 6. Prints the tolerance values of the dimension
//    to the Immediate window.
// 7. Examine the Immediate window to verify that
//    the tolerance values of the sketch in the
//    different configurations are different.
//
// NOTE: Because this part document is used elsewhere,
// do not save any changes when closing it.
//---------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace SetValues2CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ConfigurationManager swConfigurationMgr = default(ConfigurationManager);
            Configuration swConfiguration = default(Configuration);
            SelectionMgr swSelMgr = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            Dimension swDimension = default(Dimension);
            DimensionTolerance swDimensionTolerance = default(DimensionTolerance);
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            // Open part document with multiple configurations
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\PDMWorks\\speaker_frame.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Get name of active configuration
            swConfigurationMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfiguration = (Configuration)swConfigurationMgr.ActiveConfiguration;
            Debug.Print("Configuration name: " + swConfiguration.Name);

            // Select sketch
            // Put the sketch in edit mode
            // Select a dimension in the sketch
            status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -0.00430195952926557, 0.0321813003735837, -0.0155776956607312, false, 0, null, 0);

            // Get the selection
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, 0);

            // If selection is not a display dimension, then exit
            if (swSelMgr.GetSelectedObjectType3(1, -1) != (int)swSelectType_e.swSelDIMENSIONS)
                return;

            // Selection is a dimension, so get the dimension tolerance
            swDimension = (Dimension)swDisplayDimension.GetDimension2(0);
            swDimensionTolerance = (DimensionTolerance)swDimension.Tolerance;

            // Set type of tolerance type
            swDimensionTolerance.Type = (int)swTolType_e.swTolBASIC;

            // Set new dimension tolerance values
            status = swDimensionTolerance.SetValues2(0.01, 0.015, (int)swSetValueInConfiguration_e.swSetValue_InThisConfiguration, "");
            Debug.Print("  Minimum dimension tolerance: " + swDimensionTolerance.GetMinValue());
            Debug.Print("  Maximum dimension tolerance: " + swDimensionTolerance.GetMaxValue());

            // Exit sketch edit mode
            swModel.InsertSketch2(true);

            // Switch configuration to verify
            // that dimension tolerance changed
            // in other configuration only
            status = swModel.ShowConfiguration2("Square Cutout Glueable");
            status = swModelDocExt.SelectByID2("Square Cutout Glueable", "CONFIGURATIONS", 0, 0, 0, false, 0, null, 0);

            // Get name of configuration
            swConfiguration = (Configuration)swConfigurationMgr.ActiveConfiguration;
            Debug.Print("Configuration name: " + swConfiguration.Name);

            // Select sketch
            // Select same dimension in sketch as selected
            // in previously active configuration
            // Put the sketch in edit mode
            status = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("D4@Sketch8@speaker_frame.SLDPRT", "DIMENSION", -0.00471220094479408, 0.032305394835097, -0.0153009205936774, false, 0, null, 0);

            // Get the selection
            swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, 0);

            // If selection is not a display dimension, then exit
            if (swSelMgr.GetSelectedObjectType3(1, -1) != (int)swSelectType_e.swSelDIMENSIONS)
                return;

            // Selection is a dimension, so get and print the dimension tolerance
            swDimension = (Dimension)swDisplayDimension.GetDimension2(0);
            swDimensionTolerance = (DimensionTolerance)swDimension.Tolerance;
            Debug.Print("  Minimum dimension tolerance: " + swDimensionTolerance.GetMinValue());
            Debug.Print("  Maximum dimension tolerance: " + swDimensionTolerance.GetMaxValue());

            // Exit sketch edit mode
            swModel.InsertSketch2(true);
         }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
