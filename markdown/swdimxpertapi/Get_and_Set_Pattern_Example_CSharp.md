---
title: "Get and Set Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Pattern_Example_CSharp.htm"
---

# Get and Set Pattern Example (C#)

This example shows how to get and set DimXpert pattern features.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_manual.sldprt.
 // 2. Select one of the CBORE hole faces in the SOLIDWORKS viewer.
 // 3. Open an Immediate window.
 // 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 //    a. Right-click the project in Project Explorer.
 //    b. Select Add Reference.
 //    c. Click the Browse tab.
 //    d. Find and select install_dir\api\redist\swdimxpert.dll.
 //
 // Postconditions: Inspect the Immediate Window and the DimXpertManager tab.
 //
 // NOTE: Because this part is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System;
 using System.Diagnostics;

 namespace InsertPattern_CSharp.csproj
 {

     partial class SolidWorksMacro
     {
         DimXpertPart dimXpertPart;
         ModelDoc2 swModelDoc;
         swDimXpertFeatureType_e featureType;
         string msgStr;
         string msgStr2;
         string msgStr3;
         bool retval;
         int n;

         public void Main()
         {

             swModelDoc = (ModelDoc2)swApp.ActiveDoc;

             if (swModelDoc == null)
             {
                 return;
             }

             DimXpertManager dimXpertMgr = default(DimXpertManager);
             dimXpertMgr = swApp.IActiveDoc2.Extension.get_DimXpertManager(swApp.IActiveDoc2.IGetActiveConfiguration().Name, true);
             Debug.Print("Model: " + swApp.IActiveDoc2.GetPathName());

             DimXpertPart dimXpertPartObj = default(DimXpertPart);
             dimXpertPartObj = (DimXpertPart)dimXpertMgr.DimXpertPart;
             dimXpertPart = dimXpertPartObj;

             SelectionMgr selectMgr = default(SelectionMgr);
             selectMgr = (SelectionMgr)swApp.IActiveDoc2.SelectionManager;

             DimXpertDimensionOption dimOption = default(DimXpertDimensionOption);
             dimOption = dimXpertPart.GetDimOption();

             int patternType = 0;
             patternType = 2;
             // collection pattern

             bool findall = false;
             findall = true;
             // find all similar features on this face

             int[] dimarray = new int[1];
             dimarray[0] = -1;
             // default
             object dimvar = null;
             dimvar = dimarray;
             dimOption.FeatureSelectorOptions = dimvar;

             retval = selectMgr.SetSelectedObjectMark(1, 51, (int)swSelectionMarkAction_e.swSelectionMarkSet);

             // Insert the collection pattern feature
             retval = dimXpertPart.InsertPattern(dimOption, patternType, findall);

             int featCount = 0;
             featCount = dimXpertPart.GetFeatureCount();

             if (!(featCount == 0))
             {

                 IDimXpertFeature patternFeature = default(IDimXpertFeature);
                 patternFeature = (DimXpertFeature)dimXpertPart.GetFeature("Collection1");

                 msgStr = patternFeature.Name +  " is a DimXpert collection pattern feature.";
                 Debug.Print("");
                 Debug.Print(msgStr);

                 featureType = ((IDimXpertPatternFeature)patternFeature).PatternType;

                 GetPatternType(ref featureType, ref msgStr2);

                 int featureCount = 0;

                 featureCount = ((IDimXpertPatternFeature)patternFeature).GetSubFeatureCount();
                 msgStr = " Number of ";
                 msgStr3 = featureCount.ToString();
                 Debug.Print(msgStr + msgStr2 + " sub-features in this pattern is " + msgStr3);

                 object[] subfeatures = null;
                 subfeatures = (object[])((IDimXpertPatternFeature)patternFeature).GetSubFeatures();

                 Debug.Print(" Sub-features of Collection1:");
                 DimXpertFeature subFeature = default(DimXpertFeature);

                 for (n = 0; n <= subfeatures.GetUpperBound(0); n++)
                 {
                     subFeature = (DimXpertFeature)subfeatures[n];
                     Debug.Print(" " + subFeature.Name);

                 }
             }
             else
             {

                 Debug.Print("Please select a CBORE hole face in the viewer and run this macro again.");

             }
         }

         public void GetPatternType(ref swDimXpertFeatureType_e featureType, ref string msgStr2)
         {

             if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Plane))
             {
                 msgStr2 = "Plane";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Cylinder))
             {
                 msgStr2 = "Cylinder";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Cone))
             {
                 msgStr2 = "Cone";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Extrude))
             {
                 msgStr2 = "Extrude";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Fillet))
             {
                 msgStr2 = "Fillet";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Chamfer))
             {
                 msgStr2 = "Chamfer";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole))
             {
                 msgStr2 = "CompoundHole";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth))
             {
                 msgStr2 = "CompoundWidth";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch))
             {
                 msgStr2 = "CompoundNotch";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D))
             {
                 msgStr2 =  "CompoundClosedSlot3D";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint))
             {
                 msgStr2 = "IntersectPoint";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine))
             {
                 msgStr2 = "IntersectLine";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle))
             {
                 msgStr2 = "IntersectCircle";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane))
             {
                 msgStr2 = "IntersectPlane";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Pattern))
             {
                 msgStr2 = "Pattern";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Sphere))
             {
                 msgStr2 = "Sphere";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane))
             {
                 msgStr2 = "Bestfit plane";
             }
             else if ((featureType == swDimXpertFeatureType_e.swDimXpertFeature_Surface))
             {
                 msgStr2 = "Surface";
             }

         }

         public SldWorks swApp;

     }
 }
```
