---
title: "Capture 3D View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Capture_3DView_Example_CSharp.htm"
---

# Capture 3D View Example (C#)

This example shows how to capture the 3D view of a part or assembly and get its properties.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly.
 // 2. Open an Immediate window.
 //
// Postconditions:
 // 1. Captures 3DViewn.
 // 2. Prints out all of the 3D View names.
 // 3. Renames 3DViewn to Aleph.
 // 4. Refreshes the model's 3D Views.
 // 5. Observe Aleph on the 3DViews tab.
 // 6. Inspect the Immediate window.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace Capture3DView_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swDoc;
        ModelDocExtension swModelExt;
        View3D sw3DView;
        String[] viewNames;
        int v_counter;
         string modelBreakViewName = null;

        public void Main()
        {

            swDoc = (ModelDoc2)swApp.ActiveDoc;
            swModelExt = swDoc.Extension;

            sw3DView = swModelExt.Capture3DView();
            viewNames = (string[])swModelExt.Get3DViewNames();
            Debug.Print("3D Views:");
            for (v_counter = 0; v_counter <= viewNames.GetUpperBound(0); v_counter++) {
            Debug.Print("  " + viewNames[v_counter]);
            }

            sw3DView.Activate(true);
            sw3DView.Name = "Aleph";
            swModelExt.Refresh3DViews();
            Debug.Print("Number of 3D Views: " + swModelExt.Get3DViewCount());
            Debug.Print("Name of active 3D View: " + sw3DView.Name);
            Debug.Print("Configuration: " + sw3DView.ConfigurationName);
            Debug.Print("Display state: " + sw3DView.DisplayState);
            Debug.Print("Display mode as defined in swDisplayMode_e: " + sw3DView.DisplayMode);
            Debug.Print("Scale: " + sw3DView.Scale);
             modelBreakViewName = sw3DView.ModelBreakViewName;
              if (modelBreakViewName ==  null)
             {
                  Debug.Print("No model break view");
             }
              else
             {
                  Debug.Print("Model break view name: " + modelBreakViewName);
             }

        }

        public SldWorks swApp;

    }
}
```
