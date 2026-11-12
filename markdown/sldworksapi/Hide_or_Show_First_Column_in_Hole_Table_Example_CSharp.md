---
title: "Hide or Show First Column in Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Column_in_Hole_Table_Example_CSharp.htm"
---

# Hide or Show First Column in Hole Table Example (C#)

This example shows how to hide the first column in a hole table.

```vb
//-------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\simplehole.slddrw.
 // 2. Select the hole table feature in the FeatureManager
 //    design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Hides the first column.
 // 2. Examine the hole table and Immediate window.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
 //------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace ColumnHiddenTableAnnotation_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
            ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             object[] swHoleTableAnnotation = new object[1];
             TableAnnotation swTableAnnotation = default(TableAnnotation);
             Annotation swAnnotation = default(Annotation);
             HoleTable swHoleTable = default(HoleTable);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             if ((swSelMgr.GetSelectedObjectCount() == 0 | !(swSelMgr.GetSelectedObjectType(1) == (int)swSelectType_e.swSelHOLETABLEFEATS)))
             {
                 System.Windows.Forms.MessageBox.Show("Please select a hole table feature in the FeatureManager design tree.");
                 return;
             }
             swHoleTable = (HoleTable)swSelMgr.GetSelectedObject6(1, -1);
             swHoleTableAnnotation = (object[])swHoleTable.GetTableAnnotations();
             swTableAnnotation = (TableAnnotation)swHoleTableAnnotation[0];
             swAnnotation = (Annotation)swTableAnnotation.GetAnnotation();
             // If column hidden, then show it
             if ((swTableAnnotation.get_ColumnHidden(0)))
             {
                Debug.Print(" First column hidden before API call: " + swTableAnnotation.get_ColumnHidden(0));
                 swTableAnnotation.set_ColumnHidden(0, false);
                 Debug.Print(" First column hidden after API call: " + swTableAnnotation.get_ColumnHidden(0));
             }
             else
             {
                 // If column shown, then hide it
                 Debug.Print(" First column hidden before API call: " + swTableAnnotation.get_ColumnHidden(0));
                 swTableAnnotation.set_ColumnHidden(0, true);
                 Debug.Print(" First column hidden after API call: " + swTableAnnotation.get_ColumnHidden(0));
             }
         }
         public SldWorks swApp;
     }
 }
```
