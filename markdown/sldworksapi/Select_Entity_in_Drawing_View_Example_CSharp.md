---
title: "Select Entity in Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Entity_in_Drawing_View_Example_CSharp.htm"
---

# Select Entity in Drawing View Example (C#)

This example shows how to select a model face, edge, or vertex in a drawing view and dimension it.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or fully resolved assembly.
 // 2. Verify that the specified template exists.
 // 3. Select a face, edge, or vertex.
 //
 // Postconditions:
 // 1. Creates a new drawing with three views.
 // 2. Dimensions the selected face, edge, or vertex
 //    in the first drawing view.
 // 3. Examine the drawing.
 //
 // NOTE: The dimension is not guaranteed to be created if a face is selected.
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
 namespace AddDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             const string sPathToTemplate = "C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\data\\templates\\drawing.drwdot";
             const double nYoffset = 0.01;

             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Entity swEnt = default(Entity);

             DrawingDoc swDraw = default(DrawingDoc);
             ModelDoc2 swDrawModel = default(ModelDoc2);
             View swView = default(View);
             double[] vOutline = null;
             DisplayDimension swDispDim = default(DisplayDimension);

             double nXpos = 0;
             double nYpos = 0;

             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swEnt = (Entity)swSelMgr.GetSelectedObject6(1, -1);

             if ((swEnt != null))
             {
                 swDraw = (DrawingDoc)swApp.NewDrawing2((int)swDwgTemplates_e.swDwgTemplateCustom, sPathToTemplate, (int)swDwgPaperSizes_e.swDwgPaperA1size, 0.0, 0.0);
                 swDrawModel = (ModelDoc2)swDraw;

                 bRet = swDraw.Create3rdAngleViews2(swModel.GetPathName());

                 swView = (View)swDraw.GetFirstView();
                 swView = (View)swView.GetNextView();

                 bRet = swView.SelectEntity(swEnt, false);

                 // Work out where to place dimension -
                 // midway across view and slightly above
                 vOutline = (double[])swView.GetOutline();
                 nXpos = (vOutline[0] + vOutline[2]) / 2.0;
                 nYpos = vOutline[3] + nYoffset;

                 // Create the dimension, even if the entity is not
                 // visible in the drawing view
                 swDispDim = (DisplayDimension)swDrawModel.Extension.AddDimension(nXpos, nYpos, 0.0, (int)swSmartDimensionDirection_e.swSmartDimensionDirection_Left);

             }

         }

         public SldWorks swApp;
     }

 }
```
