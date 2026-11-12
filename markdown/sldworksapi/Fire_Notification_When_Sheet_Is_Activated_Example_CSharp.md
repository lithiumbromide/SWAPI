---
title: "Fire Notification When Activating a Sheet Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Sheet_Is_Activated_Example_CSharp.htm"
---

# Fire Notification When Activating a Sheet Example (C#)

This example shows how to fire a notification when a sheet is activated in a drawing document.

```
//-------------------------------------------------------------------------------
//Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
//
// Postconditions:
// 1. Displays a message box informing you that a sheet is about to be
//    activated.
// 2. Click OK to close the message box.
//
// NOTES:
// * The IDrawingDoc ActivateSheetPostNotify event only fires
//   when a sheet is interactively activated in SOLIDWORKS; this event
//   does not fire when a sheet is activated through the API.
// * Because the drawing is used elsewhere, do not save changes.
//------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace ActivateSheetEventsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public DrawingDoc swDrawingDoc;

        public void Main()
        {

            ModelDoc2 swModel;
            Boolean status;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Set up events
            swDrawingDoc = (DrawingDoc)swModel;
            AttachEventHandlers();

            // Activate Sheet4
            status = swDrawingDoc.ActivateSheet("Sheet4");
        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swDrawingDoc.ActivateSheetPreNotify += this.swDraw_ActivateSheetPreNotify;
        }

        private int swDraw_ActivateSheetPreNotify(string SheetName)
        {
            MessageBox.Show("A sheet is about to be activated.");
            return 1;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
