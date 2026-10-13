---
title: "Get Patterned Cosmetic Thread Annotations Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm"
---

# Get Patterned Cosmetic Thread Annotations Data Example (C#)

This example shows how to get data for patterned cosmetic thread annotations in a drawing.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing that contains at least one
//    drawing view with patterned cosmetic thread annotations.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Iterates through the drawing views and prints
//    to the Immediate window the patterned cosmetic
//    thread annotations data in each drawing view.
// 2. Examine the Immediate window.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CThreadCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            MathUtility swMathUtility = default(MathUtility);
            ModelDoc2 myModel = default(ModelDoc2);
            DrawingDoc myDrawing = default(DrawingDoc);
            View thisView = default(View);
            CThread thisCThread = default(CThread);

            swMathUtility = (MathUtility)swApp.GetMathUtility();
            myModel = (ModelDoc2)swApp.ActiveDoc;
            myDrawing = (DrawingDoc)myModel;
            myModel.ClearSelection2(true);

            //Traverse annotations of the drawing views in this drawing and look for cosmetic threads
            thisView = (View)myDrawing.GetFirstView();
            while ((thisView != null))
            {
                if (thisView.Name == "Sheet1")
                {
                    Debug.Print("");
                }
                else
                {
                    Debug.Print("View name = " + thisView.Name);
                    thisCThread = (CThread)thisView.GetFirstCThread();
                    while ((thisCThread != null))
                    {
                        processCosmeticThread(myModel, thisCThread);
                        thisCThread = (CThread)thisCThread.GetNext();
                    }
                }
                thisView = (View)thisView.GetNextView();
            }
        }
        private void processCosmeticThread(ModelDoc2 myModel, CThread aCThread)
        {
            Annotation cthreadAnno = default(Annotation);
            string annoName = null;
            string annoVis = null;
            int patternedCount = 0;
            object[] vPatternedXform = null;
            int i = 0;
            MathTransform transform = default(MathTransform);
            double[] vTransform = null;
            cthreadAnno = (Annotation)aCThread.GetAnnotation();
            annoName = cthreadAnno.GetName();
            if ((cthreadAnno.Visible == (int)swAnnotationVisibilityState_e.swAnnotationHidden))
            {
                annoVis = "Hidden";
            }
            else
            {
                annoVis = "Visible";
            }
            Debug.Print("  Processing CThread " + annoName + "(" + annoVis + ")");

            //Retrieve information about any patterns made from this cosmetic thread
            patternedCount = aCThread.GetPatternedTransformsCount();
            Debug.Print("   Pattern count = " + patternedCount);
            vPatternedXform = (object[])aCThread.PatternedTransforms;
            if ((vPatternedXform != null))
            {
                for (i = 0; i < vPatternedXform.Length; i++)
                {
                    transform = (MathTransform)vPatternedXform[i];
                    vTransform = (double[])transform.ArrayData;
                    if ((vTransform != null))
                    {
                        Debug.Print("    Rotate (" + vTransform[0].ToString("###0.0#####") + " " + vTransform[1].ToString("###0.0#####") + " " + vTransform[2].ToString("###0.0#####"));
                        Debug.Print("            " + vTransform[3].ToString("###0.0#####") + " " + vTransform[4].ToString("###0.0#####") + " " + vTransform[5].ToString("###0.0#####"));
                        Debug.Print("            " + vTransform[6].ToString("###0.0#####") + " " + vTransform[7].ToString("###0.0#####") + " " + vTransform[8].ToString("###0.0#####") + ")");
                        Debug.Print("    Translate " + vTransform[9].ToString("###0.0#####") + " " + vTransform[10].ToString("###0.0#####") + " " + vTransform[11].ToString("###0.0#####"));
                        Debug.Print("");
                    }
                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
