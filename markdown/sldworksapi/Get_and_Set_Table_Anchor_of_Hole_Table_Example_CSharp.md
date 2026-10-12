---
title: "Get and Set Table Anchor of Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm"
---

# Get and Set Table Anchor of Hole Table Example (C#)

This example shows how to get and set the table anchor of a hole table in a drawing.

```vb
  //-----------------------------------------------------------------
 // Preconditions: Verify that the specified drawing to open exists.
 //
 // Postconditions:
 // 1. Opens the drawing.
 // 2. At  System.Diagnostics.Debugger.Break(), examine the position
 //    of the hole table  in the drawing.
 // 3. Click the Continue button in the SOLIDWORKS Visual Studio Tools for
 //    Applications IDE.
 // 4. Sets the position of the hole table's anchor
 //    to the specified location.
 // 5. Examine the hole table in the drawing.
 //
 // NOTE: If prompted, do not save changes when closing the drawing.
 //------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace TableAnchorPositionCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             string filename = null;
             filename =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\SimpleHole.slddrw";

             ModelDoc2 model = default(ModelDoc2);
             int errors = 0;
             int warnings = 0;
             model = (ModelDoc2)swApp.OpenDoc6(filename, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             if (model == null)
                 return;

             System.Diagnostics.Debugger.Break();

             TableAnnotation swTable =  default(TableAnnotation);

             // If document is a drawing, then continue
             switch (model.GetType())
             {
                 case (int)swDocumentTypes_e.swDocDRAWING:
                     DrawingDoc drw = default(DrawingDoc);
                     drw = (DrawingDoc)model;

                     // Get the current sheet
                     Sheet drwSheet =  default(Sheet);
                     drwSheet = (Sheet)drw.GetCurrentSheet();

                     // Select the Sheet2 feature
                     ModelDocExtension modeldocext = default(ModelDocExtension);
                     bool status = false;
                     modeldocext = (ModelDocExtension)model.Extension;
                     status = modeldocext.SelectByID2("Sheet2", "SHEET", 0, 0, 0, false, 0, null, 0);

                     // Get the views on Sheet2
                     object[] views = null;
                     views = (object[])drwSheet.GetViews();

                     foreach (object vView in views)
                     {
                         View drwView =  default(View);
                         drwView = (View)vView;

                         Feature viewFeature =  default(Feature);
                         viewFeature = (Feature)drw.FeatureByName(drwView.Name);

                         // Traverse the features in the view
                         Feature subFeature = default(Feature);
                         subFeature = (Feature)viewFeature.GetFirstSubFeature();

                         // If the feature is HoleTableFeat, then get the table annotations
                         while (!(subFeature == null))
                         {
                             if (subFeature.GetTypeName2() == "HoleTableFeat")
                             {
                                 HoleTable swHoleTable =  default(HoleTable);

                                 swHoleTable = (HoleTable)subFeature.GetSpecificFeature2();
                                 object[] holeTables = null;
                                 holeTables = (object[])swHoleTable.GetTableAnnotations();

                                 // If the annotation is a hole table, then continue
                                 if ((holeTables != null))
                                 {
                                     foreach (object table in holeTables)
                                     {
                                         swTable = (TableAnnotation)table;

                                         // If the hole table is anchored, then continue
                                         if (swTable.Type == (int)swTableAnnotationType_e.swTableAnnotation_HoleChart)
                                         {
                                             if (swTable.Anchored != false)
                                             {
                                                 TableAnchor holeTableAnchor = default(TableAnchor);
                                                 holeTableAnchor = (TableAnchor)drwView.Sheet.get_TableAnchor((int)swTableAnnotationType_e.swTableAnnotation_HoleChart);

                                                 // Get the position of the table anchor
                                                  double[] anchorPosition = null;
                                                 anchorPosition = (double[])holeTableAnchor.Position;

                                                 // Determine type of table anchor
                                                  swBOMConfigurationAnchorType_e newCorner = default(swBOMConfigurationAnchorType_e);

                                                 string corner = null;
                                                 switch (swTable.AnchorType)
                                                 {
                                                     case (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft:
                                                         corner =  "  Bottom-left ";
                                                         newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopRight;
                                                         break;
                                                     case (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomRight:
                                                         corner =  "  Bottom-right ";
                                                         newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft;
                                                         break;
                                                     case (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft:
                                                         corner =  "  Top-left ";
                                                         newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomRight;
                                                         break;
                                                     case (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopRight:
                                                         corner =  "  Top-right ";
                                                         newCorner = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft;
                                                         break;
                                                 }

                                                 swTable.AnchorType = (int)newCorner;

                                                 // Set the new position of the table anchor
                                                  double[] dNewPosition = new double[2];
                                                 dNewPosition[0] = 0.0;
                                                 dNewPosition[1] = 0.0;

                                                 holeTableAnchor.Position = dNewPosition;
                                             }
                                         }
                                     }
                                 }
                             }

                             subFeature = (Feature)subFeature.GetNextSubFeature();
                         }

                     }

                     break;
                 case (int)swDocumentTypes_e.swDocASSEMBLY:
                 case (int)swDocumentTypes_e.swDocPART:

                     break;
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
