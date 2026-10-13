---
title: "Delete Blended Faces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Blended_Faces_Example_CSharp.htm"
---

# Delete Blended Faces Example (C#)

This example shows how to delete blended faces.

NOTE: You can only delete blended faces from a temporary body.

```
//--------------------------------------------------
// Preconditions:
// 1. Open a part that contains one solid body
//    and at least one blended (fillet) face.
// 2. Select a blended face.
//
// Postconditions:
// 1. Creates a new part, which has the same body as
//    the original part, but the selected blended
//    face is removed.
// 2. Examine the graphics area.
//
// NOTE: It might not be possible to remove the
// selected blended face. If it's not removed, then
// the new body is the same as the original
// body.
//--------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Collections;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            // 1 = Invisible
            // 0 = Visible
            const int CreateVisible = 0;

            const string sAttDefName = "temp_attrib";
            const string sAttRootName = "temp";

            AttributeDef swAttDef = default(AttributeDef);
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            PartDoc swPart = default(PartDoc);
            int nSelCount = 0;
            Face2 swFace = default(Face2);
            Entity swEnt = default(Entity);
            SolidWorks.Interop.sldworks.Attribute swAtt = null;
            ArrayList vAtt = new ArrayList();
            ArrayList vFaceArr = new ArrayList();
            Feature swFeat = default(Feature);
            object[] vBodies = null;
            Body2 swBody = default(Body2);
            Body2 swCopyBody = default(Body2);
            PartDoc swNewPart = default(PartDoc);
            int i = 0;
            bool bRet = false;

            swAttDef = (AttributeDef)swApp.DefineAttribute(sAttDefName);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swPart = (PartDoc)swModel;
            bRet = swAttDef.Register();

            // Add attribute to selected faces
            nSelCount = swSelMgr.GetSelectedObjectCount2(-1);
            for (i = 1; i <= nSelCount; i++)
            {
                swFace = (Face2)swSelMgr.GetSelectedObject6(i, -1);
                swEnt = (Entity)swFace;
                swAtt = (SolidWorks.Interop.sldworks.Attribute)swAttDef.CreateInstance5(swModel, swEnt, sAttRootName + i, CreateVisible, (int)swInConfigurationOpts_e.swAllConfiguration);
                vAtt.Add(swAtt);
            }
            vBodies = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
            swBody = vBodies[0] as Body2;
            swCopyBody = (Body2)swBody.Copy();

            // Remove attribute from faces
            for (i = 1; i <= nSelCount; i++)
            {
                swAtt = (SolidWorks.Interop.sldworks.Attribute)vAtt[i - 1];
                bRet = swAtt.Delete(true);
            }
            vFaceArr = (ArrayList)GetFacesWithAttribute(swApp, swCopyBody, swAttDef);
            Face2[] aFaceArr = (Face2[])vFaceArr.ToArray(typeof(Face2));

            // Can only delete blends from a temporary body
            Debug.Assert(swCopyBody.IsTemporaryBody());

            bRet = swCopyBody.DeleteBlends3(aFaceArr, true, true);
            swNewPart = (PartDoc)swApp.NewPart();
            swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swCopyBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
        }
        public object GetFacesWithAttribute(SldWorks swApp, Body2 swBody, AttributeDef swAttDef)
        {
            Face2 swFace = default(Face2);
            Entity swEnt = default(Entity);
            SolidWorks.Interop.sldworks.Attribute swAttCopy = default(SolidWorks.Interop.sldworks.Attribute);
            ArrayList swFaceArr = new ArrayList();

            // Search for faces on temporary body based
            // on copied attributes
            swFace = (Face2)swBody.GetFirstFace();
            while ((null != swFace))
            {
                swEnt = (Entity)swFace;
                swAttCopy = null;

                // Only one instance of attribute should exist
                swAttCopy = (SolidWorks.Interop.sldworks.Attribute)swEnt.FindAttribute(swAttDef, 0);
                if ((swAttCopy != null))
                {
                    swFaceArr.Add(swFace);
                }
                swFace = (Face2)swFace.GetNextFace();
            }

            return swFaceArr;
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
