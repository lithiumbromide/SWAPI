---
title: "Set Table Anchors in Sheet Formats Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Table_Anchors_Example_CSharp.htm"
---

# Set Table Anchors in Sheet Formats Example (C#)

This example shows how to set a hole table anchor in a sheet format of a drawing.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified drawing to open exists.
 // 2. Open and Immediate window.
 //
 // Postconditions:
 // 1. Opens the drawing.
 // 2. At Stop, examine the position of the hole table in the drawing.
 // 3. Press F5.
 // 4. Edits the sheet format.
 // 5. Creates a point.
 // 6. Sets the position of the hole table's anchor at the new point.
 // 7. Examine the new position of the hole table
 //    and the Immediate window.
 //
 // NOTE: If prompted, do not save changes when closing the drawing.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace SetTableAnchor_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             DrawingDoc swDrw = default(DrawingDoc);
             Sheet swSheet = default(Sheet);
             ModelDoc2 swModel = default(ModelDoc2);
             SketchPoint swSkPoint = default(SketchPoint);
             TableAnchor oldTableAnchor = default(TableAnchor);
             TableAnchor newTableAnchor = default(TableAnchor);
             double[] vPosition = null;
             string filename = null;
             int errors = 0;
             int warnings = 0;

             filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\SimpleHole.slddrw";
             swDrw = (DrawingDoc)swApp.OpenDoc6(filename, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             if (swDrw == null)
                 return;

             System.Diagnostics.Debugger.Break();

             swSheet = (Sheet)swDrw.GetCurrentSheet();
             swModel = (ModelDoc2)swDrw;

             swModel.Extension.SelectByID2(swSheet.GetName(), "SHEET", 0, 0, 0, false, 0, null, 0);

             swDrw.EditTemplate();
             swModel.EditSketch();

             swSkPoint = swModel.SketchManager.CreatePoint(0.2, 0.07, 0);
             swSkPoint.Select4(false, null);

             // If an anchor for the hole table already exists, move it to the selected sketch point
             oldTableAnchor = swSheet.get_TableAnchor((int)swTableAnnotationType_e.swTableAnnotation_HoleChart);
             newTableAnchor = (TableAnchor)swSheet.SetAsTableAnchor((int)swTableAnnotationType_e.swTableAnnotation_HoleChart);

             if ((newTableAnchor != null))
             {
                 vPosition = (double[])newTableAnchor.Position;
                 Debug.Print("Table Anchor at (" + vPosition[0] + ", " + vPosition[1] + ")");
             }

             swDrw.EditSheet();
             swModel.EditSketch();
             swModel.ForceRebuild3(true);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
