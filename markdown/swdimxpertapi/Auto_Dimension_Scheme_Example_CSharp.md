---
title: "Auto Dimension Scheme Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Auto_Dimension_Scheme_Example_CSharp.htm"
---

# Auto Dimension Scheme Example (C#)

This example shows how to create a DimXpert Auto Dimension Scheme, turn tolerance status on and off, and delete tolerances.

```vb
 //---------------------------------------------------------------------------
 //
 // Preconditions:
 //  1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_plusminus.sldprt.
 //  2. (Optional) Multi-select three faces to specify primary, secondary,  and tertiary datum.
 //  3. Open the Immediate window.
 //  4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 //     a. Right-click the project in Project Explorer.
 //     b. Select Add Reference.
 //     c. Click the Browse tab.
 //     d. Find and select install_dir\api\redist\swdimxpert.dll.
 //  5. Set two breakpoints:
 //     * swDXPart.ShowToleranceStatus = false;
 //     * retval = swDXPart.DeleteAllTolerances();
 //  6. Press F5.
 //  7. Observe on the DimXpertManager tab: Hole Pattern1, Hole Pattern2, Fillet1,
 //       Fillet Pattern1. Also observe that tolerance status is turned on in
 //     the SOLIDWORKS viewer.
 //  8. Press F5 and observe that tolerance status is turned off.
 //  9. Compare the output in the Immediate window with the features displayed
 //      on the DimXpertManager tab.
 // 10. Press F5 and observe that all tolerance annotations have been removed from the part.
 //
 // Postconditions: None
 //
 // NOTE: Because this part is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------
```

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System;
 using System.Diagnostics;
 namespace AutoDimScheme_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         Feature swFeature;
         DimXpertManager swSchema;
         DimXpertPart swDXPart;
         DimXpertAutoDimSchemeOption schemeOption;
         swDimXpertFeatureType_e featureType;
         object[] features;
         object[] appliedFeatures;
         object[] appliedAnnotations;
         DimXpertAnnotation appliedAnnotation;
         DimXpertFeature feature;
         DimXpertFeature appliedFeature;
         string msgStr;
         string msgStr2;
         string msgStr3;
         string msgStr4;
         int n;
         int o;
         int p;

         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Get the default DimXpert schema using IModelDocExtension.DimXpertManager()
             swSchema = swModelDocExt.get_DimXpertManager("Default", true);

             // Get IDimXpertPart from the IDimXpertManager
             swDXPart = (DimXpertPart)swSchema.DimXpertPart;

             // Set Auto Dimension Scheme using default options
             schemeOption = swDXPart.GetAutoDimSchemeOption();
             Debug.Print("Default for ScopeAllFeature is: ");
             Debug.Print(schemeOption.ScopeAllFeature.ToString());
             Debug.Print("Default for FeatureFilters is: ");
             Debug.Print(schemeOption.FeatureFilters.ToString());
             Debug.Print("Default for PartType is: ");
             Debug.Print(schemeOption.PartType.ToString());
             Debug.Print("Default for PatternType is: ");
             Debug.Print(schemeOption.PatternType.ToString());
             Debug.Print("Default for PolarPatternHoleCount is: ");
             Debug.Print(schemeOption.PolarPatternHoleCount.ToString());
             Debug.Print("Default for ToleranceType is: ");
             Debug.Print(schemeOption.ToleranceType.ToString());

             bool retval = false;
             retval = swDXPart.AutoDimensionScheme(schemeOption);

             // Turn tolerance status off
             swDXPart.ShowToleranceStatus = false;

             long featCount = 0;
             featCount = swDXPart.GetFeatureCount();

             msgStr = "Total of ";
             msgStr2 = featCount.ToString();
             msgStr = msgStr + msgStr2 + " features in " + (swSchema.SchemaName);

             Debug.Print("");
             Debug.Print(msgStr);

             // Get IDimXpert features through IDimXpertPart
             features = (object[])swDXPart.GetFeatures();
             msgStr = (swSchema.SchemaName) +  " has the following features: ";

             Debug.Print("");
             Debug.Print(msgStr);

             for (n = 0; n <= features.GetUpperBound(0); n++)
             {
                 //Use IDimXpertFeature to get feature data
                 feature = (DimXpertFeature)features[n];

                 Debug.Print(" " +  "Feature name: " + (feature.Name));

                 featureType = feature.Type;
                 GetPatternType(ref featureType, ref msgStr2);

                 msgStr = " Feature type ";
                 msgStr3 = " is suppressed on the DimXpertManager tab? ";
                 msgStr4 = feature.IsSuppressed().ToString();

                 Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4);

                 msgStr = " " + "Swift model: ";

                 //Use IFeature to get the Swift model corresponding to this geometric dimensioning and tolerancing data
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

                 if (!((appliedFeatures == null)))
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

                 if (!((appliedAnnotations == null)))
                 {
                     for (p = 0; p <= appliedAnnotations.GetUpperBound(0); p++)
                     {
                         appliedAnnotation = (DimXpertAnnotation)appliedAnnotations[p];
                         Debug.Print(" " +  "Applied annotation name: " + (appliedAnnotation.Name));
                     }
                 }
                 Debug.Print(" ");
             }

             // Delete all tolerances
             retval = swDXPart.DeleteAllTolerances();
         }

         public void GetPatternType(ref swDimXpertFeatureType_e featureType, ref String msgStr2)
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
