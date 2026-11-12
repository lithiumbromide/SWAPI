---
title: "Get Components in Each BOM Table Row Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm"
---

# Get Components in Each BOM Table Row Example (C#)

This example shows how to get the components in each row of a BOM table annotation.

```vb
//-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
 // 2. Make a drawing from the assembly.
 // 3. Click Insert > Tables > Bill of Materials.
 // 4. Ensure that Parts only in Bom Type is selected.
 // 5. Ensure that Display configurations of the same part separate items
 //    in Part Configuration Grouping is selected.
 // 6. Click OK.
 // 7. Click anywhere in the drawing to insert the BOM table.
 //
 // Postconditions:
 // 1. Gets the Bill of Materials1 feature.
 // 2. Gets the Default configuration.
 // 3. Processes the BOM table for the Default configuration.
 // 4. Examine the Immediate window.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //-----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void ProcessTableAnn(SldWorks swApp, ModelDoc2 swModel, TableAnnotation swTableAnn, string ConfigName)
         {
             int nNumRow = 0;
             int J = 0;
             int I = 0;
             string ItemNumber = null;
             string PartNumber = null;
             bool RowLocked;
             double RowHeight;

             Debug.Print("   Table Title: " + swTableAnn.Title);

             nNumRow = swTableAnn.RowCount;

             BomTableAnnotation swBOMTableAnn = default(BomTableAnnotation);
             swBOMTableAnn = (BomTableAnnotation)swTableAnn;

             for (J = 0; J <= nNumRow - 1; J++)
             {
                 RowLocked = swTableAnn.GetLockRowHeight(J);
                 RowHeight = swTableAnn.GetRowHeight(J);
                 Debug.Print("   Row Number " + J + " (height = " + RowHeight + "; height locked = " + RowLocked + ")");
                 Debug.Print("     Component Count: " + swBOMTableAnn.GetComponentsCount2(J, ConfigName, out ItemNumber, out PartNumber));
                 Debug.Print("       Item Number: " + ItemNumber);
                 Debug.Print("       Part Number: " + PartNumber);

                 object[] vPtArr = null;
                 Component2 swComp = null;
                 object pt = null;

                 vPtArr = (object[])swBOMTableAnn.GetComponents2(J, ConfigName);

                 if (((vPtArr != null)))
                 {
                     for (I = 0; I <= vPtArr.GetUpperBound(0); I++)
                     {
                         pt = vPtArr[I];
                         swComp = (Component2)pt;
                         if ((swComp != null))
                         {
                             Debug.Print("           Component Name: " + swComp.Name2);
                             Debug.Print("           Configuration Name: " + swComp.ReferencedConfiguration);
                             Debug.Print("           Component Path: " + swComp.GetPathName());
                         }
                         else
                         {
                             Debug.Print("  Could not get component.");
                         }
                     }
                 }
             }
         }

         public void ProcessBomFeature(SldWorks swApp, ModelDoc2 swModel, BomFeature swBomFeat)
         {
             Feature swFeat = default(Feature);
             object[] vTableArr = null;
             object vTable = null;
             string[] vConfigArray = null;
             object vConfig = null;
             string ConfigName = null;
             TableAnnotation swTable = default(TableAnnotation);
             object visibility = null;

             swFeat = swBomFeat.GetFeature();
             vTableArr = (object[])swBomFeat.GetTableAnnotations();

             foreach (TableAnnotation vTable_loopVariable in vTableArr)
             {
                 vTable = vTable_loopVariable;
                 swTable = (TableAnnotation)vTable;
                 vConfigArray = (string[])swBomFeat.GetConfigurations(true, ref visibility);
                 foreach (object vConfig_loopVariable in vConfigArray)
                 {
                     vConfig = vConfig_loopVariable;
                     ConfigName = (string)vConfig;
                     Debug.Print(" Component for Configuration: " + ConfigName);
                     ProcessTableAnn(swApp, swModel, swTable, ConfigName);
                 }
             }

         }

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             Feature swFeat = default(Feature);
             BomFeature swBomFeat = default(BomFeature);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;
             swFeat = (Feature)swModel.FirstFeature();

             while ((swFeat != null))
             {
                 if ("BomFeat" == swFeat.GetTypeName())
                 {
                     Debug.Print("Feature Name: " + swFeat.Name);
                     swBomFeat = (BomFeature)swFeat.GetSpecificFeature2();
                     ProcessBomFeature(swApp, swModel, swBomFeat);
                 }
                 swFeat = (Feature)swFeat.GetNextFeature();
             }
         }

         public SldWorks swApp;

     }
 }
```
