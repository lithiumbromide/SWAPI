---
title: "Get Hole Standards Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Wizard_Hole_Standards_Data_Example_CSharp.htm"
---

# Get Hole Standards Data Example (C#)

This example shows how to retrieve hole standards data from the Hole Wizard database.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open SOLIDWORKS Design.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Retrieves row 1 data from all three Binding Head Screw fastener tables
 //    of the ANSI Inch hole standard.
 // 2. Inspect the Immediate window.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetHoleStandards_CSharp
 {

      partial class SolidWorksMacro
     {

         private HoleStandardsData holeStandards;
         private object fastenerData;
         private HoleDataTable fastenerDataObject;
         private bool ret;
         private object indexes;
         private object standards;
         private object[] standardsArray;
         private object fastenerIDs;
         private int[] fastenerIDsArray;
         private object fastenerNames;
         private object[] fastenerNamesArray;
         private object fastenerTableTypeIDs;
         private int[] fastenerTableTypeIDsArray;
         private object columnNames;
         private object[] columnNamesArray;
         private string cellData;
         private int i;
         private int j;

         public void Main()
         {

             holeStandards = (HoleStandardsData)swApp.GetHoleStandardsData((int)swWzdGeneralHoleTypes_e.swWzdCounterBore);
             ret = holeStandards.GetHoleStandards(out indexes, out standards);
             standardsArray = (object[])standards;
             ret = holeStandards.GetFastenerTypes((string)standardsArray[0], out fastenerIDs, out fastenerNames);
             fastenerIDsArray = (int[])fastenerIDs;
             fastenerNamesArray = (object[])fastenerNames;
             ret = holeStandards.GetFastenerTableTypes((string)standardsArray[0], (int)fastenerIDsArray[0], out fastenerTableTypeIDs);
             fastenerTableTypeIDsArray = (int[])fastenerTableTypeIDs;
             for (j = 0; j <= 2; j++)
             {
                 ret = holeStandards.GetFastenerTable((string)standardsArray[0], (int)fastenerIDsArray[0], (int)fastenerTableTypeIDsArray[j], out fastenerData);
                 fastenerDataObject = (HoleDataTable)fastenerData;
                 Debug.Print("");
                 if (j == 0)
                 {
                     Debug.Print("Hole Wizard standard: " + fastenerDataObject.StandardName);
                     Debug.Print("Fastener ID: " + fastenerDataObject.FastenerID);
                     Debug.Print("Fastener: " + fastenerNamesArray[0]);
                 }

                 Debug.Print("Fastener table type ID as defined in swFastenerTableTypes_e: " + fastenerDataObject.TableTypeID);

                 ret = fastenerDataObject.GetColumnNames(out columnNames);
                 columnNamesArray = (object[])columnNames;
                 if (j == 0)
                 {
                     Debug.Print("Size data in Row #1");
                 }
                 else if (j == 1)
                 {
                     Debug.Print("Thread data in Row #1");
                 }
                 else if (j == 2)
                 {
                     Debug.Print("Screw clearances data in Row #1");
                 }

                 for (i = 0; i <= columnNamesArray.GetUpperBound(0); i++)
                 {
                     ret = fastenerDataObject.GetCellData((string)columnNamesArray[i], 0, out cellData);
                     Debug.Print(columnNamesArray[i] + ": " + cellData);
                 }
             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
