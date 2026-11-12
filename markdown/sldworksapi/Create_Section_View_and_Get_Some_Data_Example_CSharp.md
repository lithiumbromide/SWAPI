---
title: "Create Section View and Get Some Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Section_View_and_Get_Some_Data_Example_CSharp.htm"
---

# Create Section View and Get Some Data Example (C#)

This example creates a section view and sets and gets some of the section view's data.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.slddrw
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates a section view of Drawing View4.
 // 2. Sets and gets some section view settings.
 // 3. Examine the drawing and the Immediate window.
 //
 // NOTE: Because this drawing is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------
```

using System;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;

```vb
 namespace CreateSectionView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         DrawingDoc swDrawing;
         SketchManager swSketchMgr;
         SketchSegment swSketchSegment;
         object excludedComponents;
         View swView;
         DrSection swSectionView;

         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDrawing = (DrawingDoc)swModel;

             // Activate the view for which you want to create a section view
             boolstatus = swDrawing.ActivateView("Drawing View4");
             swModel.ClearSelection2(true);

             // Create section-view line
             swSketchMgr = swModel.SketchManager;
             swSketchSegment = swSketchMgr.CreateLine(-1.383705, 2.078706, 0.0, 2.747162, 0.0441, 0.0);

             // Create the section view at the specified coordinates
             // and up to the specified distance from the section-view line
             excludedComponents =  null;
             swView = swDrawing.CreateSectionViewAt5(0.1604082711061, 0.2048687170364, 0, "D", 32, (excludedComponents), 0.00835);
             Debug.Print("View data: ");
              Debug.Print(" Emphasize outlines of section views? " + swView.EmphasizeOutline);
             swSectionView = (DrSection)swView.GetSection();    // Set some section-view settings
  swSectionView.SetAutoHatch(true);
  swSectionView.SetLabel2("ABCD");
  swSectionView.SetDisplayOnlySurfaceCut(false);
  swSectionView.SetPartialSection(false);
  swSectionView.SetReversedCutDirection(false);
  swSectionView.SetScaleWithModelChanges(true);
  swSectionView.CutSurfaceBodies = true;
  swSectionView.DisplaySurfaceBodies = true;
  swSectionView.ExcludeSliceSectionBodies = false;

  // Get some section-view settings
  Debug.Print("Section view data: ");
   Debug.Print(" Label: " + swSectionView.GetLabel());
   Debug.Print(" Name of section line: " + swSectionView.GetName());
   Debug.Print(" Depth: " + swSectionView.SectionDepth * 1000.0 + " mm");
   Debug.Print(" Cut direction reversed from default direction? " + swSectionView.GetReversedCutDirection());
   Debug.Print(" Partial section cut? " + swSectionView.GetPartialSection());
   Debug.Print(" Display only the surface cut by the section line? " + swSectionView.GetDisplayOnlySurfaceCut());
   Debug.Print(" Display surface bodies? " + swSectionView.DisplaySurfaceBodies);
  Debug.Print(" Exclude slice section bodies? " + swSectionView.ExcludeSliceSectionBodies);

  swSectionView.SetDisplayOnlySpeedPakBodies(true);

   Debug.Print(" Display only SpeedPak bodies? " + swSectionView.GetDisplayOnlySpeedPakBodies());
  Debug.Print(" Scale with model changes? " + swSectionView.GetScaleWithModelChanges());
  Debug.Print(" Auto-hatch enabled? " + swSectionView.GetAutoHatch());
  Debug.Print(" Hide cut surface bodies? " + swSectionView.CutSurfaceBodies);
```

```vb
  swModel.EditRebuild3();
```

```vb
         }

         public SldWorks swApp;
     }
 }
```
