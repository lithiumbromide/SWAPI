---
title: "Move Assembly Components to New Folder Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Assembly_Components_to_New_Folder_Example_CSharp.htm"
---

# Move Assembly Components to New Folder Example (C#)

This example shows how to move selected assembly components to a newly created folder in the FeatureManager design tree.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open exists.
// 2. Open an Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Selects the valve<1> and valve_guide<1> components.
// 3. Creates a folder named Folder1 in the FeatureManager design tree.
// 4. Moves the valve<1> and valve_guide<1> components to Folder1,
//    which you can verify by expanding Folder1.
// 5. Examine the Immediate window.
//
// NOTE: Because the assembly document is used by elsewhere,
// do not save any changes.
//---------------------------------------------------------------------------
```

```vb
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace FeatureFolderLocation_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 modelDoc2;
         AssemblyDoc assemblyDoc;
         FeatureManager featureMgr;
         ModelDocExtension modelDocExt;
         SelectionMgr selectionMgr;
         Feature feature;
         object selObj;
         Feature feat;
         Feature folderFeat;
         int errors;
         int warnings;
         int count;
         Component2 componentToMove;
         object[] componentsToMove;
         int i;
         bool retVal;

         public void Main()
         {
             //Open assembly document
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\motionstudies\\valve_cam.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             modelDoc2 = (ModelDoc2)swApp.ActiveDoc;
             assemblyDoc = (AssemblyDoc)modelDoc2;

             //Select and get the two valve-related components to move to the new folder
             modelDocExt = modelDoc2.Extension;
             selectionMgr = (SelectionMgr)modelDoc2.SelectionManager;
             modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             selObj = selectionMgr.GetSelectedObject6(1, -1);
             modelDocExt.SelectByID2("valve_guide-1@valve_cam", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             selectionMgr.GetSelectedObject6(2, -1);
             count = selectionMgr.GetSelectedObjectCount2(0);
             componentsToMove = new object[count];
             for (i = 0; i <= count - 1; i++)
             {
                 componentToMove = (Component2)selectionMgr.GetSelectedObjectsComponent4(i + 1, 0);
                 componentsToMove[i] = componentToMove;
             }

             //Create the folder where to move the selected components
             featureMgr = modelDoc2.FeatureManager;
             feature = featureMgr.InsertFeatureTreeFolder2((int)swFeatureTreeFolderType_e.swFeatureTreeFolder_EmptyBefore);
             feature = (Feature)assemblyDoc.FeatureByName("Folder1");

             //Move the selected components to the new folder
             retVal = assemblyDoc.ReorderComponents(componentsToMove, feature, (int)swReorderComponentsWhere_e.swReorderComponents_LastInFolder);

             modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             feat = (Feature)selectionMgr.GetSelectedObject6(1, -1);

             featureMgr = modelDoc2.FeatureManager;
             folderFeat = featureMgr.FeatureFolderLocation(feat);

             Debug.Print("Component valve-1@valve_cam folder feature: " + folderFeat.Name);

         }

         public SldWorks swApp;

     }

 }
```
