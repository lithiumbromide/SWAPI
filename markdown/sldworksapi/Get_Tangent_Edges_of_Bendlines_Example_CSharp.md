---
title: "Get Tangent Edges of Bendlines Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm"
---

# Get Tangent Edges of Bendlines Example (C#)

This example shows how to get each bendline's visible tangent edges in a flat-pattern view in a drawing of a sheet metal part.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a SOLIDWORKS Design drawing of a sheet metal part
//    that has a flat-pattern view with
//    bend lines with tangent edges.
// 2. Open the Immediate window.
//
// Preconditions: Examine the Immediate window.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetBendlinesTangentEdges_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawing = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);
            long nbrBendlines = 0;
            object[] BendlinesArr = null;
            long nbrRelatedTangentEdges = 0;
            object RelatedTangentEdgesArr = null;
            long i = 0;
            SketchSegment swSketchSegment = default(SketchSegment);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawing = (DrawingDoc)swModel;

            // Get drawing sheet
            swSheet = (Sheet)swDrawing.GetCurrentSheet();

            // Get name of drawing sheet
            Debug.Print("Name of drawing sheet: " + swSheet.GetName());

            // Get number of views on drawing sheet
            Debug.Print(" Number of drawing views on drawing sheet: " + swDrawing.GetViewCount());

            // First view is the current drawing sheet
            swView = (View)swDrawing.GetFirstView();
            Debug.Print(" First drawing view is the current drawing sheet, so...");

            // Get first drawing view on drawing sheet
            swView = (View)swView.GetNextView();
            while ((swView != null))
            {
                Debug.Print(" Get next drawing view on drawing sheet...");

                // Get first true drawing view on current drawing sheet
                Debug.Print(" Is this drawing view a flat-pattern view? " + swView.IsFlatPatternView());

                // If this drawing view is a flat pattern view, then
                // get its bendlines and their related tangent edges
                if (swView.IsFlatPatternView())
                {
                    // Get number of bendlines in the drawing view
                    nbrBendlines = swView.GetBendLineCount();
                    BendlinesArr = new Object[nbrBendlines];
                    Debug.Print(" Number of bendlines in this drawing view: " + nbrBendlines);
                    if ((nbrBendlines > 0))
                    {
                        BendlinesArr = (Object[])swView.GetBendLines();
                        for (i = 0; i <= BendlinesArr.GetUpperBound(0); i++)
                        {
                            swSketchSegment = (SketchSegment)BendlinesArr[i];
                            Debug.Print(" Is bend line " + i + " really a bend line? " + swSketchSegment.IsBendLine());
                            // Get the number of tangent lines related to
                            // the bendline
                            nbrRelatedTangentEdges = swView.GetRelatedTangentEdgeCount(BendlinesArr[i]);
                            Debug.Print(" Number of tangent edges for Bendline " + i + ": " + nbrRelatedTangentEdges);
                            // Get the tangent lines related to the bendline
                            if ((nbrRelatedTangentEdges > 0))
                            {
                                RelatedTangentEdgesArr = swView.GetRelatedTangentEdges(BendlinesArr[i]);
                                nbrRelatedTangentEdges = nbrRelatedTangentEdges - 1;
                            }
                        }
                    }
                }
                // Get next drawing view
                swView = (View)swView.GetNextView();
            }
        }
        public SldWorks swApp;
    }
}
```
