---
title: "Create Model and Sheet Views Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Model_and_Sheet_Views_Example_CSharp.htm"
---

# Create Model and Sheet Views Example (C#)

This example shows how to create:

- model named view with gradient background.
- model named view without a background.
- sheet named view.

```
//--------------------------------------------------------------
//Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this project into the C# IDE.
// 3. Open the Immediate window.
// 4. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 5. Add a reference to System.Windows.Forms.
// 6. Start DraftSight and open
//    disk:\ProgramData\Dassault Systemes\Draftsight\Examples\pump housing.dwg.
// 7. Press F5.
//
//Postconditions:
// 1. A model named view, ModelView, is created with a gradient background
//    and is classified in the A category.
// 2. A model named view, SavedModelView, is created without a background.
// 3. A sheet named view, SheetView, is created and
//    classified in the B category.
// 4. Click View > Named Views and examine both the model and sheet.
// 5. Examine the Immediate window.
//
// NOTE: To change the background to:
// 1. Solid from gradient:
//    a. Uncomment these lines of code:
//       //SolidBackground dsSolidBackground;
//       //dsSolidBackground = dsViewMgr.CreateSolidBackground(dsColor);
//       //dsModelNamedView.SetSolidBackground(dsSolidBackground);
//    b. Comment out these lines of code:
//       GradientBackground dsGradientBackground;
//       dsGradientBackground = dsViewMgr.CreateGradientBackground(dsColor, dsColor2, dsColor3, false, 0);
//       dsModelNamedView.SetGradientBackground(dsGradientBackground);
// 2. Image from gradient:
//    a. Uncomment these lines of code:
//       //ImageBackground dsImageBackground;
//       //dsImageBackground = dsViewMgr.CreateImageBackground(imageFile, dsImageBackgroundPosition_e.dsImageBackgroundPosition_Tile, 0, 0, 0, 0);
//       //dsModelNamedView.SetImageBackground(dsImageBackground);
//    b. Perform step 1b.
//----------------------------------------------------------------

using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using DraftSight.Interop.dsAutomation;

namespace ViewManager_CSharp
{
    static class Program
    {

        public static void Main(string[] args)
        {
            DraftSight.Interop.dsAutomation.Application dsApp;
            Document dsDoc;
            ViewManager dsViewMgr;
            double[] dsCorner1 = new double[] {
            16.12,
            12.23,
            0.0
            };
            double[] dsCorner2 = new double[] {
            25.46,
            20.47,
            0.0
            };
            double[] dsCorner3 = new double[] {
            5.0,
            4.5,
            0.0
            };
            double[] dsCorner4 = new double[] {
            7.36,
            6.38,
            0.0
            };
            ModelNamedView dsModelNamedView;
            SheetNamedView dsSheetNamedView;
            dsCreateObjectResult_e result;
            Object[] dsSheetArray;
            Sheet dsSheet;
            GradientBackground dsGradientBackground;
            //SolidBackground dsSolidBackground;
            //ImageBackground dsImageBackground;
            Color dsColor;
            Color dsColor2;
            Color dsColor3;
            string imageFile;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            //Get active document
            dsDoc = dsApp.GetActiveDocument();

            if ((dsDoc != null))
            {
                //Get the view manager
                dsViewMgr = dsDoc.GetViewManager();

                //In the model space, create a model named view
                result = dsViewMgr.CreateModelNamedView("ModelView", "A", dsCorner1, dsCorner2, out dsModelNamedView);

                dsColor = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Blue);
                dsColor2 = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Cyan);
                dsColor3 = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Green);

                //Create gradient background
                dsGradientBackground = dsViewMgr.CreateGradientBackground(dsColor, dsColor2, dsColor3, false, 0);

                //Create solid background
                //dsSolidBackground = dsViewMgr.CreateSolidBackground(dsColor);

                //Create image background
                imageFile = "C:\\Users\\Public\\Pictures\\Sample Pictures\\Penguins.jpg";
                //dsImageBackground = dsViewMgr.CreateImageBackground(imageFile, dsImageBackgroundPosition_e.dsImageBackgroundPosition_Tile, 0, 0, 0, 0);

                Debug.Print("Result: " + result.ToString());
                Debug.Print("Model named view: " + dsModelNamedView.GetNamedView().GetName());
                dsModelNamedView = dsViewMgr.GetModelNamedView("ModelView");

                //Set background of ModelView and verify
                //by getting its background type
                dsModelNamedView.SetGradientBackground(dsGradientBackground);
                //dsModelNamedView.SetSolidBackground(dsSolidBackground);
                //dsModelNamedView.SetImageBackground(dsImageBackground);
                Debug.Print("Type of background: " + dsModelNamedView.GetBackgroundType());
                dsViewMgr.SaveCurrentViewAsModelView("SavedModelView", "A", out dsModelNamedView);
                dsViewMgr.ActivateModelView("ModelView");
```

```
                Debug.Print("");

                //Switch to sheet space and create a sheet named view
                dsSheetArray = (Object[])dsDoc.GetSheets();
                dsSheet = (Sheet)dsSheetArray[1];
                dsSheet.Activate();
                result = dsViewMgr.CreateSheetNamedView("SheetView", "B", dsCorner3, dsCorner4, out dsSheetNamedView);
                Debug.Print("Result: " + result.ToString());
                Debug.Print("Sheet named view: " + dsSheetNamedView.GetNamedView().GetName());
                dsSheetNamedView = dsViewMgr.GetSheetNamedView("SheetView");
                dsSheet = dsSheetNamedView.GetSheet();
                dsViewMgr.SaveCurrentViewAsSheetView("SavedSheetView", "B", out dsSheetNamedView);
                dsViewMgr.ActivateSheetView("SheetView");

            }
            else
            {
                MessageBox.Show("There are no open documents in DraftSight.");
            }

        }
    }

}
```
