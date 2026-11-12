---
title: "Link Projected View to Parent Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Projected_View_to_Parent_Configuration_Example_CSharp.htm"
---

# Link Projected View to Parent Configuration Example (C#)

This example shows how to link a projected drawing view to the parent configuration.

```
//-------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified file exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Links the projected view to the parent configuration.
// 2. Examine the Immediate window.
//
// NOTE: Because this drawing document is used elsewhere, do not save
// changes.
//-------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace LinkParentConfigurationCSharp.csproj

{

    partial class SolidWorksMacro

    {

        public ModelDoc2 swModel;

        public View swView;

        public bool status;

        public void Main()

        {

            ModelDocExtension swModelDocExt = default(ModelDocExtension);

            DrawingDoc swDrawing = default(DrawingDoc);

            string fileName = null;

            int errors = 0;

            int warnings =
0;

            // Open drawing document that has a
projected view

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";

            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING,
(int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            swDrawing = (DrawingDoc)swModel;

            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Make the projected view the active
view

            status = swDrawing.ActivateView("Drawing View2");

            status = swModelDocExt.SelectByID2("Drawing
View2", "DRAWINGVIEW",
0.4426278247583, 0.3837831481976, 0, false,
0, null, 0);

            swView = (View)swDrawing.ActiveDrawingView;

            // Determine whether the projected view
is linked to the

            // parent
configuration

            LinkConfiguration();

            // Link the projected view to the parent

            //
configuration

            swView.LinkParentConfiguration = true;

            // Determine whether the projected view
is linked to the

            // parent
configuration

            LinkConfiguration();

        }

        public void LinkConfiguration()

        {

            // Print to the Immediate window whether

            // the
projected view is linked to the parent

            //
configuration

            status = swView.LinkParentConfiguration;

            if (status)

            {

                Debug.Print("Projected view now linked to parent configuration.");

                swModel.EditRebuild3();

            }

            else

            {

                Debug.Print("Projected view not linked to parent configuration.");

            }

        }

        /// <summary>

        /// The SldWorks swApp variable is pre-assigned for you.

        /// </summary>

        public SldWorks swApp;

    }

}
```
