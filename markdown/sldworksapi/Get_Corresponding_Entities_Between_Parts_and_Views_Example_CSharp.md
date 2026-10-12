---
title: "Get Corresponding Entities Between Parts and Drawing Views Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm"
---

# Get Corresponding Entities Between Parts and Drawing Views Example (C#)

This example shows how to get corresponding entities or objects between a part and its drawing.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Ensure that the specified part and drawing exist.
 // 2. Open the Immediate window.
  // 3. Uncomment the subroutine you want to run in Main().
  // 4. At the pause, select a face, edge, vertex, feature, annotation,
 //    or sketch segment.
 // 5. Press F5.
 //
 // Postconditions:
 // 1. Inspect the Immediate window.
  // 2. If a corresponding face, edge, or vertex is found, it is selected in the
 //    underlying part or drawing.
 //
  // NOTE: Because the models are used elsewhere, do not save changes.
  //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace GetCorresponding_CSharp
 {
     public partial class SolidWorksMacro
     {
         DocumentSpecification docSpec;
         ModelDoc2 swModelPart;
         ModelDoc2 swModelDrawing;
         DrawingDoc swDrawing;
         View swView;
         int lErr = 0;
         SelectionMgr selMgr;
         Entity inputEntity;
         Entity outputEntity;
         bool bSelected;
         object inputObject;
         object outputObject;
         DrawingComponent drComp;

         public void Main()
         {

             //Uncomment the subroutine you want to run; comment the other one
             //ViewToPart()
             PartToView();
         }
         public void ViewToPart()
         {
             docSpec = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.SLDPRT");
             swModelPart = swApp.OpenDoc7(docSpec);

             docSpec = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.SLDDRW");
             swModelDrawing = swApp.OpenDoc7(docSpec);

             swDrawing = (DrawingDoc)swModelDrawing;
             swView = (View)((Feature)(swDrawing.FeatureByName("Drawing View1"))).GetSpecificFeature();

             swApp.ActivateDoc3(swModelPart.GetTitle(), true, (int)swRebuildOnActivation_e.swUserDecision, lErr);

             selMgr = (SelectionMgr)swModelPart.SelectionManager;
             swModelPart.ClearSelection2(true);

             System.Diagnostics.Debugger.Break();
             // Select something in the model and press F5

             switch (selMgr.GetSelectedObjectType3(1, -1))
             {
                 case (int)swSelectType_e.swSelFACES:
                 case (int)swSelectType_e.swSelEDGES:
                 case (int)swSelectType_e.swSelVERTICES:

                     inputEntity = (Entity)selMgr.GetSelectedObject6(1, -1);

                     Debug.Print("Using IView::GetCorrespondingEntity()");

                     outputEntity = (Entity)swView.GetCorrespondingEntity(inputEntity);

                     if (outputEntity == null)
                     {
                         Debug.Print("No corresponding entity found in the drawing view");
                     }
                     else
                     {
                         Debug.Print("Corresponding entity found....selecting in drawing");
                         swApp.ActivateDoc3(swModelDrawing.GetTitle(), false, (int)swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr);
                         bSelected = outputEntity.Select4(false, null);
                     }

                     break;
                 case (int)swSelectType_e.swSelNOTHING:

                     break;
                 default:

                     inputObject = selMgr.GetSelectedObject6(1, -1);

                     Debug.Print("Using IView::GetCorresponding()");

                     outputObject = swView.GetCorresponding(inputObject);

                     if (outputObject == null)
                     {
                         Debug.Print("No corresponding object found in the drawing view");
                     }
                     else
                     {
                         Debug.Print("Corresponding object found in the drawing view");
                     }
                     break;
             }

         }

         public void PartToView()
         {
             docSpec = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.SLDPRT");
             swModelPart = swApp.OpenDoc7(docSpec);

             docSpec = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.SLDDRW");
             swModelDrawing = swApp.OpenDoc7(docSpec);

             swDrawing = (DrawingDoc)swModelDrawing;

             swApp.ActivateDoc3(swModelDrawing.GetTitle(), false, (int)swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr);

             selMgr = (SelectionMgr)swModelDrawing.SelectionManager;
             swModelDrawing.ClearSelection2(true);

             System.Diagnostics.Debugger.Break();
             // Select something in the drawing and press F5

             swView = (View)((Feature)(swDrawing.FeatureByName("Drawing View1"))).GetSpecificFeature();

             switch (selMgr.GetSelectedObjectType3(2, -1))
             {
                 case (int)swSelectType_e.swSelFACES:
                 case (int)swSelectType_e.swSelEDGES:
                 case (int)swSelectType_e.swSelVERTICES:

                     inputEntity = (Entity)selMgr.GetSelectedObject6(2, -1);
                     drComp = (DrawingComponent)selMgr.GetSelectedObjectsComponent4(2, -1);

                     Debug.Print("Using IModelDocExtension::GetCorrespondingEntity2()");

                     outputEntity = (Entity)swModelPart.Extension.GetCorrespondingEntity2(inputEntity);

                     if (outputEntity == null)
                     {
                         Debug.Print("No corresponding entity found in the part");
                     }
                     else
                     {
                         Debug.Print("Corresponding entity found...selecting in part");
                         swApp.ActivateDoc3(swModelPart.GetTitle(), false, (int)swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr);
                         bSelected = outputEntity.Select4(false, null);
                     }

                     break;
                 case (int)swSelectType_e.swSelNOTHING:

                     break;

                 default:

                     inputObject = selMgr.GetSelectedObject6(2, -1);
                     drComp = (DrawingComponent)selMgr.GetSelectedObjectsComponent4(2, -1);

                     Debug.Print("Using IModelDocExtension::GetCorresponding2()");

                     outputObject = swModelPart.Extension.GetCorresponding2(inputObject);

                     if (outputObject == null)
                     {
                         Debug.Print("No corresponding object found in the part");
                     }
                     else
                     {
                         Debug.Print("Corresponding object found in the part");
                     }
                     break;
             }

         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
