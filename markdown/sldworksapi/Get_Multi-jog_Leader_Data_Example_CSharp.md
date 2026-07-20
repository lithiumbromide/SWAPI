---
title: "Get Multi-jog Leader Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Multi-jog_Leader_Data_Example_CSharp.htm"
---

# Get Multi-jog Leader Data Example (C#)

This example shows how to get data for a multi-jog leader.

```
//-----------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing document with at least one multi-jog leader.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects a multi-jog leader.
// 2. Gets data for the multi-jog leader.
// 3. Examine the Immediate window.
//-----------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MultiJogLeaderCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);
            object obj = null;
            Annotation swAnnotation = default(Annotation);
            MultiJogLeader swMultiJogLeader = default(MultiJogLeader);
            int nbrLines = 0;
            double[] lineData = null;
            int lineType = 0;
            double startPointX = 0;
            double startPointY = 0;
            double startPointZ = 0;
            double endPointX = 0;
            double endPointY = 0;
            double endPointZ = 0;
            int i = 0;

            //Get multi-jog leader
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawingDoc = (DrawingDoc)swModel;
            swSheet = (Sheet)swDrawingDoc.GetCurrentSheet();
            Debug.Print("Sheet name: " + swSheet.GetName());
            //First view is Sheet, so get next view
            swView = (View)swDrawingDoc.GetFirstView();
            swView = (View)swView.GetNextView();
            Debug.Print("View name: " + swView.GetName2());
            obj = (object)swView.GetFirstMultiJogLeader2();
            swMultiJogLeader = (MultiJogLeader)obj;

            //Get multi-jog leader data
            swAnnotation = (Annotation)swMultiJogLeader.GetAnnotation();
            Debug.Print("Annotation name: " + swAnnotation.GetName());
            Debug.Print("Type of annotation (11 = multi-jog leader): " + swAnnotation.GetType());
            nbrLines = swMultiJogLeader.GetLineCount();
            Debug.Print("Number of lines in multi-jog leader: " + nbrLines);
            lineData = (double[])swMultiJogLeader.GetLineAtIndex(1);
            for (i = 0; i <= nbrLines - 1; i++)
            {
                if ((lineData != null))
                {
                    Debug.Print(" Line " + (i + 1) + ":");
                    lineType = (int)lineData[0];
                    startPointX = lineData[1];
                    startPointY = lineData[2];
                    startPointZ = lineData[3];
                    endPointX = lineData[4];
                    endPointY = lineData[5];
                    endPointZ = lineData[6];
                    Debug.Print("  Line type as defined by swLineTypes_e: " + lineType);
                    Debug.Print("  Line x, y, and z start points: " + startPointX + ", " + startPointY + ", and " + startPointZ);
                    Debug.Print("  Line x, y, and z end points: " + endPointX + ", " + endPointY + ", and " + endPointZ);
                }
            }
            Debug.Print("Number of arrow heads in multi-jog leader: " + swMultiJogLeader.GetArrowHeadCount());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
