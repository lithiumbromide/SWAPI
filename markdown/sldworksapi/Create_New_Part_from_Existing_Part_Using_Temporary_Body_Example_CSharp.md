---
title: "Create New Part from Existing Part Using Temporary Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_CSharp.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (C#)

This example shows how to delete faces from a temporary body and how to create a new part using that temporary body.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\toolbox\braceright.sldprt.
// 2. Verify that the specified part template exists..
//
// Postconditions:
// 1. Creates a new part; the new part has same body as original part
//    but with selected faces deleted.
// 2. Close the new part without saving it.
// 3. Close braceright.sldprt without saving it.
//----------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace DeleteFaces5Body2_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public object GetFacesWithAttribute(SldWorks swApp, Body2 swBody, AttributeDef swAttDef)
        {
            Face2 swFace = default(Face2);
            Entity swEnt = default(Entity);
            SolidWorks.Interop.sldworks.Attribute swAttCopy = default(SolidWorks.Interop.sldworks.Attribute);
            // Search for faces on temporary body based on copied attributes
            Face2[] swFaceArr = new Face2[1];
            swFace = (Face2)swBody.GetFirstFace();
            while ((null != swFace))
            {
                swEnt = (Entity)swFace;
                swAttCopy = null;
                // Only one instance of attribute on a face should exist
                swAttCopy = (SolidWorks.Interop.sldworks.Attribute)swEnt.FindAttribute(swAttDef, 0);
                if ((swAttCopy != null))
                {
                    swFaceArr[swFaceArr.GetUpperBound(0)] = swFace;
                    Array.Resize(ref swFaceArr, swFaceArr.GetUpperBound(0) + 2);
                }
                swFace = (Face2)swFace.GetNextFace();
            }
            Array.Resize(ref swFaceArr, swFaceArr.GetUpperBound(0));
            return swFaceArr;
        }
        public void Main()
        {
            const int CreateVisible = 0;
            const string sAttDefName = "temp_attrib";
            const string sAttRootName = "root_attrib";
            AttributeDef swAttDef = default(AttributeDef);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PartDoc swPart = default(PartDoc);
            Body2 swBody = default(Body2);
            Body2 swCopyBody = default(Body2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            long nSelCount = 0;
            Face2 swFace = default(Face2);
            Entity swEnt = default(Entity);
            SolidWorks.Interop.sldworks.Attribute[] swAtt = new SolidWorks.Interop.sldworks.Attribute[6];
            object[] vFaceArr = null;
            PartDoc swNewPart = default(PartDoc);
            ModelDoc2 swNewModel = default(ModelDoc2);
            Feature swFeat = default(Feature);
            object[] vBodies = null;
            bool boolstatus = false;
            int i = 0;
            bool bLocChk = false;
            bool bRet = false;

            swAttDef = (AttributeDef)swApp.DefineAttribute(sAttDefName);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swPart = (PartDoc)swModel;
            bRet = swAttDef.Register();
            //Debug.Assert(bRet);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02203398034251, 0.2107859236428, 0.005471558832284, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03651723484872, 0.1911276369938, 0.007226351471076, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01524, 0.1384548315647, 0.004444480215071, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1306826750488, 0.0172129316129, 0.006448917397336, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1068570742154, 0.01524000000001, 0.00670683128584, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01652926606039, 0.01775444632528, 0.004157527166058, true, 0, null, 0);
            // Add attribute to selected faces
            nSelCount = swSelMgr.GetSelectedObjectCount2(-1);

            for (i = 1; i <= nSelCount; i++)
            {
                swFace = (Face2)swSelMgr.GetSelectedObject6(i, -1);
                swEnt = (Entity)swFace;
                swAtt[i - 1] = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName + i, CreateVisible, (int)swInConfigurationOpts_e.swAllConfiguration);

            }
            Object varBodies;
            vBodies = (Object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
            varBodies = vBodies;
            swBody = (Body2)vBodies[0];
            swCopyBody = (Body2)swBody.Copy();
            // Remove attribute from faces
            for (i = 1; i <= nSelCount; i++)
            {
                bRet = swAtt[i - 1].Delete(true);

            }
            vFaceArr = (Object[])GetFacesWithAttribute(swApp, swCopyBody, swAttDef);
            Object varFaceArr = vFaceArr;
            bRet = swCopyBody.DeleteFaces5(varFaceArr, (int)swHealActionType_e.swHealAction_Shrink, (int)swLoopProcessOption_e.swLoopProcess_Auto, true, out varBodies, out bLocChk);

            swNewPart = (PartDoc)swApp.NewDocument("C:\\Documents and Settings\\All Users\\Application Data\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\part.prtdot", 0, 0, 0);
            swNewModel = (ModelDoc2)swNewPart;
            swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swCopyBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
        }
        public SldWorks swApp;
    }
}
```
