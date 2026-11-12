---
title: "Get Bodies in Body Folders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_in_Body_Folders_Example_CSharp.htm"
---

# Get Bodies in Body Folders Example (C#)

This example shows how to get the bodies in body folder features.

```vb
 //-----------------------------------------------
 // Preconditions: Open a part document that
 // contains a body folder that contains
 // one or more solid, surface, cut-list,
 // or weldment items.
 //
 // Postconditions: Inspect the Immediate window.
 //-----------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace BodyFolderType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swPart;
         Feature swFeat;

         string[] BodyFolderType = new string[6];

         public void Main()
         {
             BodyFolderType[0] = "dummy";
             BodyFolderType[1] = "swSolidBodyFolder";
             BodyFolderType[2] = "swSurfaceBodyFolder";
             BodyFolderType[3] = "swBodySubFolder";
             BodyFolderType[4] = "swWeldmentSubFolder";
             BodyFolderType[5] = "swWeldmentCutListFolder";

             swPart = (ModelDoc2)swApp.ActiveDoc;

             Debug.Print("File = " + swPart.GetPathName());

             swFeat = (Feature)swPart.FirstFeature();
             TraverseFeatures(swFeat, true);

         }

         public void DoTheWork(Feature thisFeat)
         {
             bool IsBodyFolder = false;
             IsBodyFolder = false;

             string FeatType = null;
             FeatType = thisFeat.GetTypeName();

             if (FeatType == "SolidBodyFolder" | FeatType == "SurfaceBodyFolder" | FeatType == "CutListFolder" | FeatType == "SubWeldFolder" | FeatType == "SubAtomFolder")
             {
                 IsBodyFolder = true;
             }

             if (IsBodyFolder)
             {
                 BodyFolder BodyFolder = default(BodyFolder);
                 BodyFolder = (BodyFolder)thisFeat.GetSpecificFeature2();

                 int BodyFolderTypeE = 0;
                 BodyFolderTypeE = BodyFolder.Type;
                 Debug.Print(thisFeat.Name + "," + FeatType + "," + BodyFolderType[BodyFolderTypeE] + " type " + BodyFolderTypeE);

                 int BodyCount = 0;
                 BodyCount = BodyFolder.GetBodyCount();

                 Debug.Print("   Body Count is " + BodyCount);

                 object[] vBodies = null;
                 vBodies = (object[])BodyFolder.GetBodies();

                 int i = 0;

                 if ((vBodies != null))
                 {
                     for (i = vBodies.GetLowerBound(0); i <= vBodies.GetUpperBound(0); i++)
                     {
                         Body2 Body = default(Body2);
                         Body = (Body2)vBodies[i];
                         Debug.Print("   " + Body.Name);
                     }
                 }

                 Feature FeatureFromBodyFolder = default(Feature);
                 FeatureFromBodyFolder = BodyFolder.GetFeature();

                 if ((!object.ReferenceEquals(FeatureFromBodyFolder, thisFeat)))
                 {
                     MessageBox.Show("Features don't match!");
                 }

             }
             else
             {
             }

         }

         public void TraverseFeatures(Feature thisFeat, bool isTopLevel)
         {
             Feature curFeat = default(Feature);
             curFeat = thisFeat;

             while ((curFeat != null))
             {
                 DoTheWork(curFeat); //Do the thing that we are doing this feature traversal for

                 Feature subfeat = default(Feature);
                 subfeat = (Feature)curFeat.GetFirstSubFeature();

                 while ((subfeat != null))
                 {
                     TraverseFeatures(subfeat,  false);
                     Feature nextSubFeat = default(Feature);
                     nextSubFeat = (Feature)subfeat.GetNextSubFeature();
                     subfeat = nextSubFeat;
                     nextSubFeat = null;
                 }

                 subfeat = null;

                 Feature nextFeat = default(Feature);

                 if (isTopLevel)
                 {
                     nextFeat = (Feature)curFeat.GetNextFeature();
                 }
                 else
                 {
                     nextFeat = null;
                 }

                 curFeat = nextFeat;
                 nextFeat = null;

             }

         }

         public SldWorks swApp;

     }

 }
```
