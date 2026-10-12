---
title: "Get Virtual Sharp Witness Line Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Virtual_Sharp_Witness_Line_Data_Example_CSharp.htm"
---

# Get Virtual Sharp Witness Line Data Example (C#)

This example shows how to get the geometry data of all of the virtual sharp witness lines in a drawing.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open the drawing of a part that contains one or more
 // virtual sharps with witness lines.
 //
 // Postconditions: Inspect the Immediate Window for virtual sharp witness line
 // geometry data.
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
 namespace GetWitnessGeomInfo_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swModel;
         DrawingDoc pDrawing;
         View swView;
         int Count;
         int size;
         Double[] entitiesData;
         int index;
         int entityCounts;
         int entType;
         int linesCount;
         int arcsCount;
         int VirtualSharpNum;
         int j;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             pDrawing = (DrawingDoc)swModel;

             swView = (View)pDrawing.GetFirstView();

             while ((swView != null))
             {
                 Debug.Print("Drawing view: " + swView.Name);

                 Count = swView.GetWitnessEntitiesCount(out size);

                 Debug.Print("  Number of virtual sharp witness lines: " + Count);
                 Debug.Print("  Size of virtual sharp witness line geometry data array: " + size);

                 if ((Count > 0))
                 {
                     entitiesData = (double[])swView.GetWitnessGeomInfo();

                     if ((entitiesData != null))
                     {
                         VirtualSharpNum = 0;
                         index = 0;
                         entityCounts = 0;
                         while (entityCounts < Count - 1)
                         {
                             Debug.Print("    Virtual sharp " + VirtualSharpNum);
                             Debug.Print("      Color: " + entitiesData[index]);
                             index = index + 1;
                             Debug.Print("      Line style (swLineStyles_e): " + entitiesData[index]);
                             index = index + 1;
                             Debug.Print("      Line weight: (swLineWeights_e): " + entitiesData[index]);
                             index = index + 1;
                             Debug.Print("      Layer ID: " + entitiesData[index]);
                             index = index + 1;
                             Debug.Print("      Layer override (swLayerOverride_e):" + entitiesData[index]);
                             index = index + 1;

                             entType = (int)entitiesData[index];
                             Debug.Print("      Entity type: " + entType);
                             if ((entType == 0))
                             {
                                 index = index + 1;
                                 linesCount = (int)entitiesData[index];
                                 Debug.Print("      Line count: " + linesCount);
                                 index = index + 1;

                                 for (j = 0; j <= linesCount - 1; j++)
                                 {
                                     Debug.Print("        Start: x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                     Debug.Print("        End:   x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                 }
                                 entityCounts = entityCounts + linesCount;
                             }

                             entType = (int)entitiesData[index];
                             Debug.Print("      Entity type: " + entType);
                             if ((entType == 1))
                             {
                                 index = index + 1;
                                 arcsCount = (int)entitiesData[index];
                                 Debug.Print("      Arc count: " + arcsCount);
                                 index = index + 1;

                                 for (j = 0; j <= arcsCount - 1; j++)
                                 {
                                     Debug.Print("        Start:  x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                     Debug.Print("        End:    x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                     Debug.Print("        Center: x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                     Debug.Print("        Normal: x =" + entitiesData[index] +  " y =" + entitiesData[index + 1] + " z =" + entitiesData[index + 2]);
                                     index = index + 3;
                                 }

                                 entityCounts = entityCounts + arcsCount;

                             }

                             VirtualSharpNum = VirtualSharpNum + 1;

                         }

                     }
                 }

                 swView = (View)swView.GetNextView();

             }

         }

         public SldWorks swApp;

     }
 }
```
