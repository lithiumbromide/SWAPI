---
title: "Fill Holes in Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fill_Holes_in_Part_Example_CSharp.htm"
---

# Fill Holes in Part Example (C#)

In CAM drilling operations, it might be useful to deduce the appearance of an item before machining begins. This is slightly different than calculating the minimum amount of raw material required, i.e., the stock size. This example shows how to use some of the geometry- and topology-related methods and properties to fill all holes in a part.

```
//--------------------------------------------------------------------------
// Preconditions:  Open public_documents\samples\tutorial\api\cover_datum.sldrpt.
//
// Postconditions:
// 1. Creates a new part.
// 2. Fills the holes in the new part.
// 3. Click the surface-imported and thicken features, which were created
//    by filling the holes, in the FeatureManager design tree and examine
//    the part after each click.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            Body2 swBody = default(Body2);
            Face2 swFace = default(Face2);
            Loop2 swLoop = default(Loop2);
            object[] vEdgeArr = null;
            Curve[] swCurve = new Curve[1];
            object[] vCurveArr = null;
            Edge swEdge = default(Edge);
            Body2 swTempBody = default(Body2);
            Surface swSurf = default(Surface);
            Surface swSurfCopy = default(Surface);
            string sPartTemplateName = null;
            ModelDoc2 swNewModel = default(ModelDoc2);
            PartDoc swNewPart = default(PartDoc);
            Feature[] swFeats = new Feature[1];
            Feature swFeat = default(Feature);
            Feature swKnitFeat = default(Feature);
            Feature swThickFeat = default(Feature);
            FeatureManager swNewFeatMgr = default(FeatureManager);
            int i = 0;
            bool bRet = false;
            object[] vBodies = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;

            vBodies = (object[])swPart.GetBodies2((int)swBodyType_e.swSolidBody, false);
            swBody = (Body2)vBodies[0];

            // Create new part
            sPartTemplateName = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            swNewModel = (ModelDoc2)swApp.NewDocument(sPartTemplateName, (int)swDwgPaperSizes_e.swDwgPaperAsize, 0.0, 0.0);
            swNewFeatMgr = (FeatureManager)swNewModel.FeatureManager;
            swNewPart = (PartDoc)swNewModel;

            swFace = (Face2)swBody.GetFirstFace();
            while ((swFace != null))
            {
                swLoop = (Loop2)swFace.GetFirstLoop();
                while ((swLoop != null))
                {
                    if (swLoop.IsOuter())
                    {
                        vEdgeArr = (object[])swLoop.GetEdges();
                        if ((vEdgeArr.GetUpperBound(0)) >= 0)
                        {
                            Array.Resize(ref swCurve, (vEdgeArr.GetUpperBound(0) + 1));

                            for (i = 0; i <= (vEdgeArr.GetUpperBound(0)); i++)
                            {
                                swEdge = (Edge)vEdgeArr[i];
                                swCurve[i] = (Curve)swEdge.GetCurve();
                            }
                            vCurveArr = (Curve[])swCurve;
                            swSurf = (Surface)swFace.GetSurface();
                            swSurfCopy = (Surface)swSurf.Copy();
                            swTempBody = (Body2)swSurfCopy.CreateTrimmedSheet4((vCurveArr), false);

                            // Typically nothing is returned if the loop is
                            // perpendicular to the surface, as in the
                            // end loops of a cylinder

                            if ((swTempBody != null))
                            {
                                // Sheet body only has one face
                                swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swTempBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
                                swFeats[swFeats.GetUpperBound(0)] = swFeat;
                                Debug.Assert((swFeats[swFeats.GetUpperBound(0)] != null));
                                Array.Resize(ref swFeats, (swFeats.GetUpperBound(0)) + 2);
                            }
                        }
                    }
                    swLoop = (Loop2)swLoop.GetNext();
                }
                swFace = (Face2)swFace.GetNextFace();
            }

            Array.Resize(ref swFeats, (swFeats.GetUpperBound(0)));

            swNewModel.ClearSelection2(true);
            for (i = 0; i <= (swFeats.GetUpperBound(0)); i++)
            {
                bRet = swFeats[i].Select2(true, 1);
            }

            swNewFeatMgr.InsertSewRefSurface(true, false, false, 3.001639406912E-05, 0.0001);

            // Make sure surfaces are successfully sewn together
            swKnitFeat = (Feature)swNewModel.FeatureByPositionReverse(0);
            bRet = swKnitFeat.Select2(false, 1);
            swThickFeat = (Feature)swNewFeatMgr.FeatureBossThicken(0.00254, 0, 7471215, false, true, true, true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
