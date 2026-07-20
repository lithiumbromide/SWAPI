---
title: "Change Color of Component in Specific Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm"
---

# Change Color of Component in Specific Display State Example (C#)

This example shows how to change the color of a:

- selected component in a
  specific display state at the assembly and part levels.
- component in its part document.

```
//----------------------------------------------
// Preconditions: Verify that the specified assembly and part exist.
//
// Postconditions:
//  1. Opens the specified assembly document.
//  2. Examine the graphics area, then press F5.
//  3. Changes the selected component's, USB_cover1,
//     assembly-level color from the default red
//     to gray in the specified display state. This
//     is the overriding color level.
//  4. Examine the component in the graphics area, then press F5.
//  5. Changes the selected component's, USB_cover1, part-level
//     color from red to green in the specified display state of
//     the component part. This is not the overriding color level.
//  6. Closes, but does not save, the assembly document.
//  7. Opens the component's part document, USB_cover1.sldprt.
//  8. Examine the graphics area, then press F5.
//  9. Changes part's color from red to green in the specified
//     display state of the part. This is the overriding color
//     level.
// 10. Examine the graphics area, then press F5.
// 11. Closes, but does not save, the part document.
//-----------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace AppearancesCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModelDoc = null;
            ModelDocExtension swModelDocExt = null;
            SelectionMgr swSelMgr = null;
            DisplayStateSetting swDisplayStateSetting = null;
            Component2 swComponent = null;
            Component2[] swComponents = new Component2[1];
            string[] displayStateNames = new string[1];
            object appearances = null;
            object[] appearancesArray = null;
            AppearanceSetting swAppearanceSetting = default(AppearanceSetting);
            AppearanceSetting[] newAppearanceSetting = new AppearanceSetting[1];
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = "";
            int red_rgb = 0;
            int green_rgb = 0;
            int blue_rgb = 0;
            int newColor = 0;

            //Open assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\appearances\\usb_flash_drive1.sldasm";
            swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area
            //Press F5 to continue

            //Select component, USB_cover1
            swModelDocExt = (ModelDocExtension)swModelDoc.Extension;
            swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
            status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swComponent = (Component2)swSelMgr.GetSelectedObject6(1, -1);
            swComponents[0] = swComponent;

            swModelDoc.ClearSelection2(true);

            //Get display state
            swDisplayStateSetting = (DisplayStateSetting)swModelDocExt.GetDisplayStateSetting((int)swDisplayStateOpts_e.swAllDisplayState);
            swDisplayStateSetting.Entities = swComponents;
            swDisplayStateSetting.Option = (int)swDisplayStateOpts_e.swSpecifyDisplayState;
            displayStateNames[0] = "Display State-1";
            swDisplayStateSetting.Names = displayStateNames;
            //Assembly level is default
            swDisplayStateSetting.PartLevel = false;

            //Change the selected component's, USB_cover1,
            //assembly-level color from the default red
            //to gray in the specified display state; this
            //is the overriding color level
            appearances = (object)swModelDocExt.get_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting);
            appearancesArray = (object[])appearances;
            swAppearanceSetting = (AppearanceSetting)appearancesArray[0];
            red_rgb = 50;
            green_rgb = 50;
            blue_rgb = 50;
            newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16;
            swAppearanceSetting.Color = newColor;
```

swAppearanceSetting. Diffuse = 0.8d;

swAppearanceSetting. Specular = 0.5d;

swAppearanceSetting. SpecularColor = newColor;

swAppearanceSetting. Luminous = 0.1d;

swAppearanceSetting. Transparent = 0d;

```
            newAppearanceSetting[0] = (AppearanceSetting)swAppearanceSetting;
            swModelDocExt.set_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting, newAppearanceSetting);

            System.Diagnostics.Debugger.Break();
            //Examine the component in the graphics area
            //Press F5 to continue

            swModelDoc.ClearSelection2(true);

            status = swModelDocExt.SelectByID2("USB_cover1-1@usb_flash_drive1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swComponent = (Component2)swSelMgr.GetSelectedObject6(1, -1);
            swComponents[0] = (Component2)swComponent;

            swModelDoc.ClearSelection2(true);

            //Get display state
            swDisplayStateSetting = swModelDocExt.GetDisplayStateSetting((int)swDisplayStateOpts_e.swAllDisplayState);
            swDisplayStateSetting.Entities = swComponents;
            swDisplayStateSetting.Option = (int)swDisplayStateOpts_e.swSpecifyDisplayState;
            displayStateNames[0] = "<Default>_Display State 1";
            swDisplayStateSetting.Names = displayStateNames;
            //Set to part level
            swDisplayStateSetting.PartLevel = true;

            //Change the selected component's, USB_cover1, part-level
            //color from red to green in the specified display state of
            //the component part; this is not the overriding color level
            appearances = (object)swModelDocExt.get_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting);
            appearancesArray = (object[])appearances;
            swAppearanceSetting = (AppearanceSetting)appearancesArray[0];
            red_rgb = 0;
            green_rgb = 255;
            blue_rgb = 0;
            newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16;
            swAppearanceSetting.Color = newColor;
```

swAppearanceSetting. Diffuse = 0.8d;

swAppearanceSetting. Specular = 0.5d;

swAppearanceSetting. SpecularColor = newColor;

swAppearanceSetting. Luminous = 0.1d;

swAppearanceSetting. Transparent = 0.0d;

```
            newAppearanceSetting[0] = swAppearanceSetting;
            swModelDocExt.set_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting, newAppearanceSetting);

            //Close the assembly document without saving
            //changes
            swApp.CloseDoc("usb_flash_drive1");

            //Open the assembly component USB_cover1 as a part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\appearances\\usb_cover1.sldprt";
            swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModelDoc.Extension;
            swConfigMgr = (ConfigurationManager)swModelDoc.ConfigurationManager;
            swConfig = (Configuration)swConfigMgr.ActiveConfiguration;

            swComponents[0] = null;
            swComponents[0] = swConfig.GetRootComponent3(true);

            swModelDoc.ClearSelection2(true);

            //Get display state
            swDisplayStateSetting = null;
            swDisplayStateSetting = (DisplayStateSetting)swModelDocExt.GetDisplayStateSetting((int)swDisplayStateOpts_e.swAllDisplayState);
            swDisplayStateSetting.Entities = swComponents;
            swDisplayStateSetting.Option = (int)swDisplayStateOpts_e.swSpecifyDisplayState;
            displayStateNames[0] = "<Default>_Display State 1";
            swDisplayStateSetting.Names = displayStateNames;

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area
            //Press F5 to continue

            //Change color of selected component in specified display state
            //from default red to green; this is the overriding color
            appearances = (object)swModelDocExt.get_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting);
            appearancesArray = (object[])appearances;
            swAppearanceSetting = (AppearanceSetting)appearancesArray[0];
            red_rgb = 0;
            green_rgb = 255;
            blue_rgb = 0;
            newColor = Math.Max(Math.Min(red_rgb, 255), 0) + Math.Max(Math.Min(green_rgb, 255), 0) * 16 * 16 + Math.Max(Math.Min(blue_rgb, 255), 0) * 16 * 16 * 16 * 16;
            swAppearanceSetting.Color = newColor;
```

swAppearanceSetting. Diffuse = 0.8d;

swAppearanceSetting. Specular = 0.5d;

swAppearanceSetting. SpecularColor = newColor;

swAppearanceSetting. Luminous = 0.1d;

swAppearanceSetting. Transparent = 0.0d;

```
            newAppearanceSetting[0] = swAppearanceSetting;
            swModelDocExt.set_DisplayStateSpecMaterialPropertyValues(swDisplayStateSetting, newAppearanceSetting);

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area
            //Press F5 to continue

            //Close the part document without saving
            //changes
            swApp.CloseDoc("usb_cover1");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
