---
title: "Change Colors of User-interface Elements Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Colors_of_User-interface_Elements_Example_CSharp.htm"
---

# Change Colors of User-interface Elements Example (C#)

This example shows how to change the colors of user-interface elements.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions:
// 1. Message boxes pop up before and after the colors of
//    the user-interface elements change.
// 2. Click OK to close each message box.
// 3. Examine and experiment with the user-interface
//    elements whose colors changed:
//    * Text in command window
//    * Crosshair
//    * Background of model
// 4. Run the macro again to reset the colors of the user-interface
//    elements to their former colors.
//----------------------------------------------------------------

using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using DraftSight.Interop.dsAutomation;

namespace ApplicationOptionsCSharp
{

    static class Program
    {
        public static void Main(string[] args)
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            // Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            if (null == dsApp)
            {
                return;
            }

            ApplicationOptions dsApplicationOptions = dsApp.GetApplicationOptions();

            //Change colors of user-interface elements

            //Set color of text of command window to blue or black, dependent on current color
            Color dsColor = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_CommandWindowText);
            MessageBox.Show("Color of text command window before changing its color: " + dsColor.GetNamedColor());
            if (dsColor.GetNamedColor() == dsNamedColor_e.dsNamedColor_Blue)
                dsColor.SetRGBColor(0, 0, 0);
            else
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue);
            dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_CommandWindowText, dsColor);
            MessageBox.Show("Color of text of command window after changing its color: " + dsColor.GetNamedColor());

            //Set color of model crosshair to red or white, dependent on current color
            dsColor = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_ModelCrosshair);
            MessageBox.Show("Color of crosshair before changing its color: " + dsColor.GetNamedColor());
            if (dsColor.GetNamedColor() == dsNamedColor_e.dsNamedColor_Red)
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_White);
            else
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Red);
            dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_ModelCrosshair, dsColor);
            MessageBox.Show("Color of crosshair after changing its color: " + dsColor.GetNamedColor());

            //Set color of background of model to white or black, dependent on current color
            dsColor = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_ModelBackground);
            MessageBox.Show("Color of model background before changing its color: " + dsColor.GetNamedColor());
            if (dsColor.GetNamedColor() == dsNamedColor_e.dsNamedColor_White)
                dsColor.SetRGBColor(0, 0, 0);
            else
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_White);
            dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_ModelBackground, dsColor);
            MessageBox.Show("Color of model background after changing its color: " + dsColor.GetNamedColor());

        }
    }
}
```
