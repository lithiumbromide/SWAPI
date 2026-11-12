---
title: "Constrain Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Constrain_Sketch_Example_CSharp.htm"
---

# Constrain Sketch Example (C#)

This example shows how to fully constrain a sketch.

| Before constraining the sketch | After constraining the sketch |
| --- | --- |
|  |  |

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Before constraining the sketch sketch exists.
 //
 // Postconditions: Fully constrains the sketch, which looks like
 // After constraining the sketch.
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
 using System.Windows.Forms;
 namespace ConstrainSketch_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SketchManager swSketchMgr;
         Sketch swSketch;
         SelectionMgr swSelMgr;
         Feature swFeat;
         long nSketchStatus;
         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Is a model document active?

             if (swModel == null)
             {
                 swApp.SendMsgToUser2("A part document must be open and the active document.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;

             }

             // Is it a part document?
             long modelType = 0;
             modelType = swModel.GetType();

             if (modelType != (int)swDocumentTypes_e.swDocPART)
             {
                 swApp.SendMsgToUser2("A part document must be open and the active document.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;

             }

             swSketchMgr = swModel.SketchManager;
             swSketch = swSketchMgr.ActiveSketch;

             if (swSketch == null)
             {
                 swApp.SendMsgToUser2("No active sketch; thus, a sketch could not be selected.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;

             }

             // Select the lines and make them colinear and vertical
             boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.02116924482339, 0.04904427527406, 0, false, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0.06508556638246, 0.02563976857491, 0, true, 0, null, 0);

             swModel.SketchAddConstraints("sgCOLINEAR");
             swModel.SketchAddConstraints("sgVERTICAL2D");

             MessageBox.Show("The lines have been selected, made colinear, and vertically constrained.");
             swModel.ClearSelection2(true);

             //Select the center of the circles and constrain them to the origin
             boolstatus = swModel.Extension.SelectByID2("Point7", "SKETCHPOINT", 0.1074240560292, 0.006179841656516, 0, false, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Point1@Origin", "EXTSKETCHPOINT", 0, 0, 0, true, 0, null, 0);

             swModel.SketchAddConstraints("sgCOINCIDENT");
             MessageBox.Show("The center of the circles and the origin were selected and made coincident");
             swModel.ClearSelection2(true);

             // Select a line and the circle and make them tangent
             boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.005390925700365, 0.009861449451888, 0,  false, 0,  null, 0);
             boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, true, 0, null, 0);

             swModel.SketchAddConstraints("sgTANGENT");
             MessageBox.Show("One line and a cirle were selected; both lines are now tangent with the circle.");
             swModel.ClearSelection2(true);

             //Select the circles and make them concentric
             boolstatus = swModel.Extension.SelectByID2("Arc2", "SKETCHSEGMENT", -0.0290584043849, 0.03116218026797, 0, false, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, true, 0, null, 0);

             swModel.SketchAddConstraints("sgCONCENTRIC");
             MessageBox.Show("The circles have been selected and made concentric.");
             swModel.ClearSelection2(true);

             //Select all the sketch entities and fix their positions
             MessageBox.Show("All  sketch entities will be selected and made fixed to fully constrain the sketch.");
             boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.02116924482339, 0.04904427527406, 0, false, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0.06508556638246, 0.02563976857491, 0, true, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Arc2", "SKETCHSEGMENT", -0.0290584043849, 0.03116218026797, 0, false, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, true, 0, null, 0);

             swModel.SketchAddConstraints("sgFIXED");
             swModel.ClearSelection2(true);

         }

         public SldWorks swApp;

     }

 }
```
