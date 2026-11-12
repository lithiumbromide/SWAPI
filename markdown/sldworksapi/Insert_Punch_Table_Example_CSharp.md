---
title: "Insert Punch Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Punch_Table_Example_CSharp.htm"
---

# Insert Punch Table Example (C#)

This example shows how to insert a punch table in the flat pattern view of a sheet metal part that contains one or more forming tool features.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing that contains a flat pattern view of a sheet
//    metal part with one or more forming tool features.
// 2. Modify the x- and y-coordinates in the IModelDocExtension::SelectByID2
//    methods for the specified VERTEX and FACE.
// 3. Verify that the punch table template exists.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a punch table in the drawing.
// 2. Inspect the Immediate window for punch table feature details.
// ---------------------------------------------------------------------------
```

```vb
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace InsertPunchTable_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         DrawingDoc Draw;
         bool boolstatus;
         View myView;
         PunchTableAnnotation myTableAnn;
         PunchTable MyTable;
         Feature featRet;

         object rVar;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             Draw = (DrawingDoc)Part;
             boolstatus = Draw.ActivateView("Drawing View1");
             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);

             //Select a vertex in the drawing view to be the origin of all datums in the table
             //All X LOCATION and Y LOCATION table column values will be relative to this datum origin
             boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.1344949308616, 0.0948467785893, 0, false, 1, null, 0);

             //Select a face that contains the punches that will be annotated in the table
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.1562337360869, 0.1059474450873, 0, true, 2, null, 0);

             myView = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObjectsDrawingView(1);

             myTableAnn = myView.InsertPunchTable(false, 0.2178779310824, 0.2022819591903, 1, "A", "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\punchtable-standard.sldpuntbt");

             MyTable = myTableAnn.PunchTable;
             Debug.Print("Default punch table properties:");
             Debug.Print("");
             Debug.Print("Tag style (swPunchTableTagStyle_e): " + MyTable.TagStyle);
             Debug.Print("Starting tag: " + MyTable.StartingValue);
             Debug.Print("Merge cells with the punch ID for a given tag? " + MyTable.CombineSameSize);
             Debug.Print("Combine rows with the same punch ID? " + MyTable.CombineTags);
             Debug.Print("Display dual dimensions? " + MyTable.DualDimensions);
             Debug.Print("Display units for dual dimensions? " + MyTable.ShowUnits);
             Debug.Print("Punch table annotation count: " + MyTable.GetTableAnnotationCount());

             rVar = MyTable.GetTableAnnotations();

             featRet = (Feature)MyTable.GetFeature();
             Debug.Print("Feature name: " + featRet.Name);

             Part.ClearSelection2(true);
             boolstatus = Draw.ActivateSheet("Sheet1");
         }

         public SldWorks swApp;

     }
 }
```
