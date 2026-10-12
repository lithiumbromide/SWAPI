---
title: "Get Broken-Out Section Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm"
---

# Get Broken-Out Section Feature Data Example (C#)

This example shows how to get broken-out section feature data from a drawing view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a drawing that contains a view with a broken-out
 // section feature.
 //
 // Postconditions:
 // 1. Inspect the Immediate window.
 // 2. The radius of the broken-out section is increased.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace GetBrokenOutSections_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swDoc;
         DrawingDoc swDDoc;
         View swView;
         object[] varSheet;
         object[] varViews;
         int I;
         int J;
         int K;
         Feature swFeat;
         BrokenOutSectionFeatureData swFeatData;
         Entity swDepthRef;
         object[] varBS;
         bool doRelease;
         object[] varskSeg;
         int segCtr;
         int segType;

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swDDoc = (DrawingDoc)swDoc;
             swDoc.ClearSelection2(true);
             varSheet = (object[])swDDoc.GetViews();
             for (I = varSheet.GetLowerBound(0); I <= varSheet.GetUpperBound(0); I++)
             {
                 varViews = (object[])varSheet[I];
                 // skip the sheet view
                 for (J = 1; J <= varViews.GetUpperBound(0); J++)
                 {
                     View swView = default(View);
                     swView = (View)varViews[J];
                     Debug.Print("View: " + swView.Name);
                     Debug.Print("  Number of broken-out sections in this view: " + swView.GetBreakOutSectionCount());
                     varBS = (object[])swView.GetBreakOutSections();
                     if ((!((varBS == null))))
                     {
                         for (K = varBS.GetLowerBound(0); K <= varBS.GetUpperBound(0); K++)
                         {
                             swFeat = (Feature)varBS[K];
                             EditFeature(swFeat);
                             swFeatData = (BrokenOutSectionFeatureData)swFeat.GetDefinition();
                             swFeatData.AccessSelections(swDoc, null);
                             swDepthRef = swFeatData.DepthReference;
                             // get and select depth reference, if set
                             if ((swDepthRef == null))
                             {
                                 Debug.Print("              Depth of exposure in meters: " + swFeatData.Depth);
                             }
                             else
                             {
                                 swDepthRef.Select(true);
                             }
                             swFeatData.ReleaseSelectionAccess();
                             swFeatData =  null;
                         }
                     }
                 }
             }
         }
         public void GetExistingValue()
         {
             swFeatData.EditSketch =  true;
             varskSeg = (object[])swFeatData.SketchSegment;
             if ((!((varskSeg == null))))
             {
                 Debug.Print("              Number of sketch segments: " + swFeatData.GetSketchSegmentCount());
             }
         }
         public void EditFeature(Feature inFeat)
         {
             Debug.Print("      Iterating on broken-out section: " + inFeat.Name);

             swFeatData = (BrokenOutSectionFeatureData)inFeat.GetDefinition();
             swFeatData.AccessSelections(swDoc,  null);

             GetExistingValue();

             if ((doRelease == false))
             {
                 if ((!((varskSeg == null))))
                 {
                     for (segCtr = varskSeg.GetLowerBound(0); segCtr <= varskSeg.GetUpperBound(0); segCtr++)
                     {
                         SketchSegment swSeg = default(SketchSegment);
                         swSeg = (SketchSegment)varskSeg[segCtr];
                         segType = swSeg.GetType();
                         switch (segType)
                         {
                             case (int)swSketchSegments_e.swSketchLINE:
                                 SketchLine swSegLine = default(SketchLine);
                                 swSegLine = (SketchLine)swSeg;
                                 Debug.Print("                  Segment type: Line");
                                 swSegLine =  null;
                                 break;
                             case (int)swSketchSegments_e.swSketchARC:
                                 SketchArc swSegArc = default(SketchArc);
                                 swSegArc = (SketchArc)swSeg;
                                 Debug.Print("                  Segment type: Arc");
                                 Debug.Print("                      Old radius: " + swSegArc.GetRadius());
                                 double newRad = 0;
                                 newRad = swSegArc.GetRadius() + 0.005;
                                 Debug.Print("                      New radius: " + newRad);
                                 swSegArc.SetRadius(newRad);
                                 swSegArc =  null;
                                 break;
                             default:
                                 Debug.Print("                  Segment type: Unknown");
                                 break;
                         }
                     }
                 }
                 inFeat.ModifyDefinition(swFeatData, swDoc,  null);
                 swDoc.ClearSelection();
             }
             else
             {
                 swFeatData.ReleaseSelectionAccess();
             }
             varskSeg = null;
             swFeatData = null;
         }

         public SldWorks swApp;
     }

 }
```
