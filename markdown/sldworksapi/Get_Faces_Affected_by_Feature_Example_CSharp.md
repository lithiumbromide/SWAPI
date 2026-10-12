---
title: "Get Faces Affected by Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Feature_Example_CSharp.htm"
---

# Get Faces Affected by Feature Example (C#)

This example shows how to get the faces affected by a feature. This example also highlights the edges on each affected face in blue.

```vb
 //-----------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document.
 // 2. Select a feature, such as a draft, that affects faces.
 //
 // Postconditions:
 // 1. Highlights the edges of the faces in blue that are affected
 //    by the selected feature.
 // 2. Examine the graphics area.
 //-----------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace GetFaceEdgeCount_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         ModelDocExtension swModelExt;
         Feature swFeature;
         object[] vAffectedFaces;
         object[] vEdges;
         int nFaceCount;
         int nEdgeCount;
         int i;
         int j;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swModel.ClearSelection2(true);

             nFaceCount = swFeature.GetAffectedFaceCount();
             Debug.Print("Number of faces affected by selected feature = " + nFaceCount);
             vAffectedFaces = (object[])swFeature.GetAffectedFaces();

             for (i = 0; i <= (nFaceCount - 1); i++)
             {
                 nEdgeCount = ((Face)vAffectedFaces[i]).GetEdgeCount();
                 Debug.Print("   Number of edges on Face " + i +  " = " + nEdgeCount);
                 vEdges = (object[])((Face)vAffectedFaces[i]).GetEdges();

                 for (j = 0; j <= (nEdgeCount - 1); j++)
                 {
                     ((Edge)vEdges[j]).Display(2, 0, 0, 1, true);
                 }
             }

         }

         public SldWorks swApp;

     }

 }
```
