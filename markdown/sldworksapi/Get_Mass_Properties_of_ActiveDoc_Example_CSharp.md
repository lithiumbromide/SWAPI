---
title: "Get Mass Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_ActiveDoc_Example_CSharp.htm"
---

# Get Mass Properties Example (C#)

This example shows how to retrieve the mass properties of selected components in an assembly.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly with one or more components.
  // 2. Multi-select the components for which to get mass properties.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. Gets the mass properties for the selected components in
 //    the assembly.
 // 2. Inspect the Immediate window for the mass properties of
 //    the selected components.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetMassProperties2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelExt = default(ModelDocExtension);

             SelectionMgr swSelMgr = default(SelectionMgr);
             Component2 swComp = default(Component2);

             int nStatus = 0;
             double[] vMassProp = null;
             int i = 0;
             int nbrSelections = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             nbrSelections = swSelMgr.GetSelectedObjectCount2(-1);

             if (nbrSelections == 0)
             {
                 Debug.Print("Please select one or more components and rerun the macro.");
                 return;
             }

             nbrSelections = nbrSelections - 1;

             Debug.Print("Getting mass properties for components: ");
             for (i = 0; i <= nbrSelections; i++)
             {
                 swComp = (Component2)swSelMgr.GetSelectedObject6(i + 1, -1);
                 Debug.Print("  " + swComp.Name2);
             }

             vMassProp = (double[])swModelExt.GetMassProperties2(1, out nStatus, true);

             Debug.Print("Status as defined in swMassPropertiesStatus_e (0 = Mass properties calculation successful) = " + nStatus);

             if ((vMassProp != null))
             {
                 Debug.Print("Center of mass:");
                 Debug.Print("  X-coordinate = " + vMassProp[0]);
                 Debug.Print("  Y-coordinate = " + vMassProp[1]);
                 Debug.Print("  Z-coordinate = " + vMassProp[2]);
                 Debug.Print("Volume = " + vMassProp[3]);
                 Debug.Print("Surface area = " + vMassProp[4]);
                 Debug.Print("Mass = " + vMassProp[5]);
                 Debug.Print("Density = " + vMassProp[5] / vMassProp[3]);
                 Debug.Print("Moments of inertia taken at the center of mass and aligned with the output coordinate system:");
                 Debug.Print("  Lxx = " + vMassProp[6]);
                 Debug.Print("  Lyy = " + vMassProp[7]);
                 Debug.Print("  Lzz = " + vMassProp[8]);
                 Debug.Print("  Lxy = " + vMassProp[9]);
                 Debug.Print("  Lzx = " + vMassProp[10]);
                 Debug.Print("  Lyz = " + vMassProp[11]);

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
