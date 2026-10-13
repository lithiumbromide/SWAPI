---
title: "Move Annotations to Notes Area Annotation View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Annotations_to_First_Annotation_View_Example_CSharp.htm"
---

# Move Annotations to Notes Area Annotation View Example (C#)

This example shows how to move all annotations to the **Notes Area** annotation view.

```
//----------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\button.sldprt.
// 2. Add a note to the *Top annotation view by double-clicking
//    *Top in the Annotations folder in the FeatureManager design
//    tree and clicking Insert > Annotations > Note. If prompted
//    to turn on feature dimensions display, click No.
// 3. Repeat step 2 to add a note to the *Front annotation view.
// 4. Double-click the Unassigned Items annotation view in the
//    Annotations folder in the FeatureManager design tree.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Examine the Immediate window.
// 2. Double-click each annotation view in the FeatureManager
//    design tree to verify that all annotations were moved
//    from *Front and *Top to Notes Area only. If prompted
//    to turn on feature dimensions display, click No.
//
// NOTE: Because the part is used elsewhere,
// do not save changes when closing the document.
//----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace IAnnotationViewCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelExt = default(ModelDocExtension);
            object[] swAnnViews = null;
            object[] annotations = null;
            Annotation[] annToMove = new Annotation[2];
            AnnotationView swAnnView = default(AnnotationView);
            Annotation swAnn = default(Annotation);
            Feature swFeat = default(Feature);
            MathTransform swMathTransform = default(MathTransform);
            int i = 0;
            int j = 0;
            int k = 0;
            int l = 0;
            double[] planeArray = null;
            int nbrPlaneArray = 0;
            bool status = false;
            double[] transformArray = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelExt = (ModelDocExtension)swModel.Extension;

            //Get the annotation views, number of annotation views,
            //their names, and whether the annotation view is
            //hidden (i.e., not activated)
            swAnnViews = (object[])swModelExt.AnnotationViews;
            Debug.Print("Number of annotation views: " + swModelExt.AnnotationViewCount);
            for (i = 0; i <= swModelExt.AnnotationViewCount - 1; i++)
            {
                swAnnView = (AnnotationView)swAnnViews[i];
                swFeat = (Feature)swAnnView;
                Debug.Print("   " + swFeat.Name);
                status = swAnnView.Hide();
                //status dependent on whether the annotation view is activated
                //Only Unassigned Items is activated
                Debug.Print("        Hide: " + status);
                Debug.Print("        Flat-pattern view: " + swAnnView.FlatPatternView);
            }

            //Iterate through each annotation view and its annotations
            //Print each annotation name, its rotation matrix, whether
            //it is shown in the annotation view, and whether it is assigned
            //to a 3D view
            //Add all annotations to an array to move them
            k = 0;
            l = 0;
            Debug.Print("");
            Debug.Print("  Name and number of annotations in annotation view: ");
            for (i = 0; i <= swModelExt.AnnotationViewCount - 1; i++)
            {
                swAnnView = (AnnotationView)swAnnViews[i];
                swAnnView.Activate();
                annotations = (object[])swAnnView.GetAnnotations2(false, false);
                swFeat = (Feature)swAnnView;
                Debug.Print("");
                Debug.Print("        " + swFeat.Name + " = " + swAnnView.AnnotationCount);
                if ((annotations != null))
                {
                    for (j = 0; j <= swAnnView.AnnotationCount - 1; j++)
                    {
                        swAnn = (Annotation)annotations[j];
                        if (k >= 0)
                        {
                            annToMove[k] = (Annotation)swAnn;
                            k = k + 1;
                        }
                        planeArray = (double[])swAnn.GetPlane();
                        nbrPlaneArray = planeArray.GetLength(0);
                        Debug.Print("          Rotation matrix of the annotation relative to the X-Y plane of the model: ");
                        while (l < nbrPlaneArray)
                        {
                            Debug.Print("            " + planeArray[l] + " " + planeArray[l + 1] + " " + planeArray[l + 2]);
                            l = l + 3;
                        }
                        l = 0;
                        swMathTransform = (MathTransform)swAnn.GetFlipPlaneTransform();
                        transformArray = (double[])swMathTransform.ArrayData;
                        if (transformArray != null)
                        {
                            Debug.Print("          Rotation matrix if annotation plane flipped:");
                            Debug.Print("           " + transformArray[0] + " " + transformArray[1] + " " + transformArray[2]);
                            Debug.Print("           " + transformArray[3] + " " + transformArray[4] + " " + transformArray[5]);
                            Debug.Print("           " + transformArray[6] + " " + transformArray[7] + " " + transformArray[8]);
                            Debug.Print("          Translation component if annotation plane flipped:");
                            Debug.Print("           " + transformArray[9] + " " + transformArray[10] + " " + transformArray[11]);
                            Debug.Print("");
                        }
                        Debug.Print("          Annotation names:");
                        Debug.Print("            " + swAnn.GetName());
                        status = swAnnView.IsShown();
                        Debug.Print("               Shown in this annotation view: " + status);
                        status = swAnnView.UnassignedView;
                        Debug.Print("                  Assigned to a 3D View: " + status);
                    }
                }
            }

            //Move all annotations to the Notes Area annotation view
            Debug.Print("");
            Debug.Print("Move all annotations to Notes Area annotation view:");
            for (i = 0; i <= swModelExt.AnnotationViewCount - 1; i++)
            {
                swAnnView = (AnnotationView)swAnnViews[i];
                swAnnView.Activate();
                swFeat = (Feature)swAnnView;
                if (swFeat.Name == "Notes Area")
                {
                    status = swAnnView.MoveAnnotations(annToMove);
                    Debug.Print("  Annotations moved: " + status);
                    status = swAnnView.Show();
                    //status should be false because annotation was activated
                    Debug.Print("     Show: " + status);

                }
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
