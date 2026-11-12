---
title: "Get and Set Drawing Properites Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Drawing_Properties_Example_CSharp.htm"
---

# Get and Set Drawing Properites Example (C#)

## Get and Set Drawing Properties Example (C#)

This example shows how to get and set standard and custom drawing properties.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets the active document.
// 3. Gets and sets standard and custom drawing properties.
// 4. Displays a message box showing the total number of
//    drawing custom properties. Click OK to close the message
//    box.
// 5. Displays a message box showing the first custom property
//    in the list of custom properties. Click OK to close the
//    message box.
// 6. Displays a message box instructing you to
//    type DRAWINGPROPERTIES at the prompt in the
//    command window to open the drawing properties dialog.
//    Click OK to close the message box.
// 7. Examine the properties on both tabs of the drawing
//    properties dialog.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace DrawingPropertiesCSharp
{
    class Program
    {
        public static void Main()
        {

            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }
```

```
            //Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get drawing properties
            DrawingProperties dsDrawingProperties = dsDoc.GetDrawingProperties();

            if (null == dsDrawingProperties)
            {
                MessageBox.Show("There are no valid drawing properties.");
                return;
            }

            //Set drawing properties
            dsDrawingProperties.Author = "Me";
            dsDrawingProperties.Keywords = "test,sample";
            dsDrawingProperties.Comments = "Properties created by this DraftSight API application";
            dsDrawingProperties.Title = "Title";
            dsDrawingProperties.Subject = "Test";

            //Add key and value to the drawing custom properties
            string key = "0123";
            string value = "Test Value";
            dsDrawingProperties.AddCustomProperty(key, value);

            //Set another drawing custom property
            dsDrawingProperties.SetCustomProperty("9234", "234");

            //Remove previously added drawing custom property
            dsDrawingProperties.RemoveCustomProperty("234");

            //Set drawing custom property with an index number
            dsDrawingProperties.SetCustomPropertyAt(1, "testvalue");

            //Get number of custom properties
            MessageBox.Show("Number of custom properties: " + dsDrawingProperties.GetCustomPropertyCount());

            string keyValue;
            if (dsDrawingProperties.GetCustomPropertyCount() >= 0)
            {
                //Get first drawing custom property and key value in the list of drawing custom properties
                string customProperty = dsDrawingProperties.GetCustomPropertyAt(0, out keyValue);
                MessageBox.Show("Custom property: " + customProperty + ", Key: " + keyValue);
            }

            //Type DRAWINGPROPERTIES at the prompt in the command window
            //to see the drawing properties
            MessageBox.Show("Type DRAWINGPROPERTIES at the prompt in the command window to open the drawing properties dialog. Examine the information on both tabs.");
        }
    }
}
```
