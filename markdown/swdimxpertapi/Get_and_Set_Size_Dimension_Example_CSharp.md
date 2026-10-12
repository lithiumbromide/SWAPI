---
title: "Get and Set Size Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Size_Dimension_Example_CSharp.htm"
---

# Get and Set Size Dimension Example (C#)

This example shows how to get and set DimXpert compound width features.

```vb
 //------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\dimxpert\bracket_ads_plusminus.sldprt.
 // 2. Select an edge.
 // 3. Open the Immediate window.
 // 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 //    a. Right-click the project in Project Explorer.
 //    b. Select Add Reference.
 //    c. Click the Browse tab.
 //    d. Find and select install_dir\api\redist\swdimxpert.dll.
 //
 // Postconditions:
 // 1. Inspect the Immediate Window.
 // 2. Observe the Width1 feature and the Width2 size dimension on the
 //     DimXpertManager tab.
 //
 // NOTE: Because this part is elsewhere,  do not save changes.
 //--------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System;
 using System.Diagnostics;
 namespace InsertSize_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         DimXpertPart dimXpertPart;

         public void Main()
         {

             ModelDoc2 swModelDoc = default(ModelDoc2);
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;
             Feature swFeature = default(Feature);
             swDimXpertFeatureType_e featureType = default(swDimXpertFeatureType_e);
             object[] features = null;
             object[] appliedFeatures = null;
             object[] appliedAnnotations = null;
             DimXpertAnnotation appliedAnnotation = default(DimXpertAnnotation);
             DimXpertFeature feature = default(DimXpertFeature);
             DimXpertFeature appliedFeature = default(DimXpertFeature);
             string msgStr = null;
             string msgStr2 = null;
             string msgStr3 = null;
             string msgStr4 = null;
             int n = 0;
             int o = 0;
             int p = 0;
             bool boolstatus = false;

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

             DimXpertDimensionOption dimOption = default(DimXpertDimensionOption);
             dimOption = dimXpertPart.GetDimOption();

             // Specify the position of the dimension annotation
             double[] textPos = new double[3];
             textPos[0] = 0.05;
             textPos[1] = -0.03;
             textPos[2] = -0.03;
             object posvar = null;
             posvar = textPos;
             dimOption.TextPosition = posvar;

             int[] dimarray = new int[1];
             dimarray[0] = -1;
             // default feature
             object dimvar = null;
             dimvar = dimarray;
             dimOption.FeatureSelectorOptions = dimvar;

             // Insert the size dimension
             dimXpertPart.InsertSizeDimension(dimOption);

             int featCount = 0;
             featCount = dimXpertPart.GetFeatureCount();

             msgStr = "Total of ";
             msgStr2 = featCount.ToString();
             msgStr = msgStr + msgStr2 + " DimXpert features";
             Debug.Print("");
             Debug.Print(msgStr);

             // Get IDimXpert features through IDimXpertPart

             features = (object[])dimXpertPart.GetFeatures();
             if ((features != null))
             {
                 msgStr = " Features: ";
                 Debug.Print("");
                 Debug.Print(msgStr);

                 for (n = 0; n <= features.GetUpperBound(0); n++)
                 {
                     feature = (DimXpertFeature)features[n];
                     Debug.Print(" " +  "Feature name: " + (feature.Name));
                     featureType = feature.Type;
                     GetPatternType(ref featureType, ref msgStr2);

                     msgStr = " Feature type ";
                     msgStr3 = " is suppressed on the DimXpertManager tab? ";
                     msgStr4 = feature.IsSuppressed().ToString();
                     Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4);

                     msgStr = " " + "Model feature: ";

                     swFeature = (Feature)feature.GetModelFeature();

                     if ((swFeature != null))
                     {
                         msgStr2 = swFeature.GetTypeName2();
                         Debug.Print(msgStr + msgStr2);
                     }

                     msgStr = " " + "Number of SOLIDWORKS face entities in this feature: ";
                     msgStr2 = feature.GetFaceCount().ToString();
                     Debug.Print(msgStr + msgStr2);

                     msgStr = " " + "Number of applied features: ";
                     msgStr2 = feature.GetAppliedFeatureCount().ToString();
                     Debug.Print(msgStr + msgStr2);

                     appliedFeatures = (object[])feature.GetAppliedFeatures();

                     if ((appliedFeatures != null))
                     {
                         for (o = 0; o <= appliedFeatures.GetUpperBound(0); o++)
                         {
                             appliedFeature = (DimXpertFeature)appliedFeatures[o];
                             Debug.Print(" " +  "Applied feature name: " + (appliedFeature.Name));
                         }
                     }

                     msgStr = " " + "Number of applied annotations: ";
                     msgStr2 = feature.GetAppliedAnnotationCount().ToString();
                     Debug.Print(msgStr + msgStr2);

                     appliedAnnotations = (object[])feature.GetAppliedAnnotations();

                     if ((appliedAnnotations != null))
                     {
                         for (p = 0; p <= appliedAnnotations.GetUpperBound(0); p++)
                         {
                             appliedAnnotation = (DimXpertAnnotation)appliedAnnotations[p];
                             Debug.Print(" " +  "Applied annotation name: " + (appliedAnnotation.Name));
                         }
                     }
                     Debug.Print(" ");
                 }

                 // Get specific information about the Width1 feature

                 IDimXpertCompoundWidthFeature widthFeature = default(IDimXpertCompoundWidthFeature);
                 widthFeature = (IDimXpertCompoundWidthFeature)dimXpertPart.GetFeature("Width1");
                 msgStr = ((IDimXpertFeature)widthFeature).Name + " is a DimXpert compound width feature.";
                 Debug.Print("");
                 Debug.Print(msgStr);
                 Debug.Print("");

                 // Get the nominal width coordinates

                 double width = 0;
                 double x = 0;
                 double y = 0;
                 double z = 0;
                 double i = 0;
                 double j = 0;
                 double k = 0;

                 Debug.Print("Nominal width of Width1");
                 Debug.Print("");
                 boolstatus = widthFeature.GetNominalCompoundWidth(ref width, ref x, ref y, ref z, ref i, ref j, ref k);

                 msgStr = "Width is ";
                 msgStr2 = width.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "X-coordinate is ";
                 msgStr2 = x.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "Y-coordinate is ";
                 msgStr2 = y.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "Z-coordinate is ";
                 msgStr2 = z.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "I-component of pierce vector is ";
                 msgStr2 = i.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "J-component of pierce vector is ";
                 msgStr2 = j.ToString();
                 Debug.Print(msgStr + msgStr2);

                 msgStr = "K-component of pierce vector is ";
                 msgStr2 = k.ToString();
                 Debug.Print(msgStr + msgStr2);
                 Debug.Print("");

                 // Get whether the width is a hole or a pin

                 boolstatus = widthFeature.Inner;
                 msgStr = "This width is for a hole: ";
                 msgStr2 = boolstatus.ToString();
                 Debug.Print(msgStr + msgStr2);
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
                 msgStr2 = "Bestfit Plane";
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
