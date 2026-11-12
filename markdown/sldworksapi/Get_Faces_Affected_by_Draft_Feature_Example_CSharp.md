---
title: "Get Faces Affected by Draft Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Draft_Feature_Example_CSharp.htm"
---

# Get Faces Affected by Draft Feature Example (C#)

This example shows how to get the faces affected by a draft feature.

**NOTE:** In SOLIDWORKS Design, a feature is comprised of faces. The faces created by a feature can be retrieved using IFeature::GetFaces. However, certain types of features only affect existing faces and do not create any new faces. Examples of these types of features are draft and scale features. For these features, IFeature::GetFaces returns an empty array (no faces). This sample code shows how to use IDraftFeatureData2::GetDraftedEntities to get the faces affected by a draft feature.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly with a draft feature.
 // 2. If you opened an assembly, then fully resolve the assembly if necessary.
 // 3. Select a draft feature.
 //
 // Postconditions:
 // 1. Deselects the draft feature.
 // 2. Selects the faces affected by the draft feature.
 // 3. Gets the type of draft feature as defined in swDraftType_e.
 // 4. Examine the Immediate window and graphics area.
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
 namespace GetFacesForDraftFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             SelectData swSelData = default(SelectData);
             Feature swFeat = default(Feature);
             DraftFeatureData2 swDraftFeat = default(DraftFeatureData2);
             object vEnt = null;
             object[] vEntArr = null;
             Entity swEnt = default(Entity);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = (SelectData)swSelMgr.CreateSelectData();
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swDraftFeat = (DraftFeatureData2)swFeat.GetDefinition();

             // Type as defined in swDraftType_e
             Debug.Print(swDraftFeat.Type.ToString());

             swModel.ClearSelection2(true);

             // No need to roll back to get affected faces
             vEntArr = (object[])swDraftFeat.GetDraftedEntities();
             foreach (object vEnt_loopVariable in vEntArr)
             {
                 vEnt = vEnt_loopVariable;
                 swEnt = (Entity)vEnt;
                 bRet = swEnt.Select4(true, swSelData);
             }
         }

         public SldWorks swApp;

     }
 }
```
