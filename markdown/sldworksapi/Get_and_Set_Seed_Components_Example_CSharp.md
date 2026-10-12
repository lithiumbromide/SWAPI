---
title: "Get and Set Seed Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Seed_Components_Example_CSharp.htm"
---

# Get and Set Seed Components Example (C#)

This example shows how to access the seed components of patterns in an assembly. It also shows that seed components can be replaced by either IComponent2 objects or IFeature objects representing those components.

```vb
 //------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly exists.
 // 2. Open the Immediate Window.
 //
 // Postconditions:
 // 1. Gets the names of the seed components.
 // 2. Replaces the seed components either by an IComponent2 object
 //    or an IFeature object representing the component.
 // 3. Examine the Immediate window.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace AssemblyPatterns.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             DispatchWrapper[] dispWrapArr = null;

             string fileName = null;
             int errors = 0;
             int warnings = 0;
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem2.sldasm";

             // Open the model
             ModelDoc2 swModel =  default(ModelDoc2);
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             // Verify that the model is active
             if (swModel == null)
             {
                 Debug.Print("No active model document");
                 return;
             }

             Debug.Print("Model: " + swModel.GetTitle());

             // Get all of the features in the model
             FeatureManager swFeatMgr = default(FeatureManager);
             swFeatMgr = (FeatureManager)swModel.FeatureManager;

             object[] vFeatures = null;
             vFeatures = (object[])swFeatMgr.GetFeatures(true);

             // Iterate over all features
             for (int iFeat = 0; iFeat <= vFeatures.GetUpperBound(0); iFeat++)
             {
                 Feature swFeature = default(Feature);
                 swFeature = (Feature)vFeatures[iFeat];

                 // Is the current feature a patterned feature?
                 string name = "";
                 name = swFeature.GetTypeName2();
                 name = name.ToUpper();

                 switch (name)
                 {
                     case "LOCALLPATTERN":
                         // ILocalLinearPatternFeatureData
                         Debug.Print("    Linear Pattern: " + swFeature.Name);
                         LocalLinearPatternFeatureData llpDefinition =  default(LocalLinearPatternFeatureData);
                         llpDefinition = (LocalLinearPatternFeatureData)swFeature.GetDefinition();
                         object[] llpSeedComps = null;

                         if (llpDefinition.AccessSelections(swModel,  null))
                         {
                             // Get the seed components for this pattern
                             llpSeedComps = (object[])llpDefinition.SeedComponentArray;
                             Array.Resize(ref llpSeedComps, (llpSeedComps.GetUpperBound(0) + 1));
                         }

                         // Arbitrarily decide whether to replace each seed component
                         // with a component or a feature
                         ProcessSeedComponentArray(ref llpSeedComps);

                         dispWrapArr = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(llpSeedComps);
                         llpDefinition.SeedComponentArray = dispWrapArr;

                         // Update the feature defintion
                         swFeature.ModifyDefinition(llpDefinition, swModel, null);

                         break;
                     case "LOCALCIRPATTERN":
                         // ILocalCircularPatternFeatureData
                         Debug.Print("    Circular Pattern: " + swFeature.Name);
                         LocalCircularPatternFeatureData cpDefinition = default(LocalCircularPatternFeatureData);
                         cpDefinition = (LocalCircularPatternFeatureData)swFeature.GetDefinition();
                         object[] cpSeedComps = null;

                         if (cpDefinition.AccessSelections(swModel,  null))
                         {
                             // Get the seed components for this pattern
                             cpSeedComps = (object[])cpDefinition.SeedComponentArray;
                             Array.Resize(ref cpSeedComps, (cpSeedComps.GetUpperBound(0) + 1));
                         }

                         // Arbitrarily decide whether to replace each seed component
                         // with a component or a feature
                         ProcessSeedComponentArray(ref cpSeedComps);

                         dispWrapArr = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(cpSeedComps);
                         cpDefinition.SeedComponentArray = dispWrapArr;

                         // Update the feature definition
                         swFeature.ModifyDefinition(cpDefinition, swModel, null);

                         break;
                     case "DERIVEDLPATTERN":
                         // IDerivedPatternFeatureData
                         Debug.Print("    Derived Linear Pattern: " + swFeature.Name);
                         DerivedPatternFeatureData dpDefinition =  default(DerivedPatternFeatureData);
                         dpDefinition = (DerivedPatternFeatureData)swFeature.GetDefinition();
                         object[] dpSeedComps = null;
                         if (dpDefinition.AccessSelections(swModel,  null))
                         {
                             // Get the seed components for this pattern
                             dpSeedComps = (object[])dpDefinition.SeedComponentArray;
                             Array.Resize(ref dpSeedComps, (dpSeedComps.GetUpperBound(0) + 1));
                         }

                         // Arbitrarily decide whether to replace each seed component
                         // with a component or a feature
                         ProcessSeedComponentArray(ref dpSeedComps);

                         dispWrapArr = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(dpSeedComps);
                         dpDefinition.SeedComponentArray = dispWrapArr;

                         // Update the feature definition
                         swFeature.ModifyDefinition(dpDefinition, swModel, null);

                         break;
                     case "DERIVEDCIRPATTERN":
                         // IDerivedPatternFeatureData
                         Debug.Print("    Derived Circular Pattern: " + swFeature.Name);
                         DerivedPatternFeatureData dcpDefinition =  default(DerivedPatternFeatureData);
                         dcpDefinition = (DerivedPatternFeatureData)swFeature.GetDefinition();
                         object[] dcpSeedComps = null;
                         if (dcpDefinition.AccessSelections(swModel,  null))
                         {
                             // Get the seed components for this pattern
                             dcpSeedComps = (object[])dcpDefinition.SeedComponentArray;
                             Array.Resize(ref dcpSeedComps, (dcpSeedComps.GetUpperBound(0) + 1));
                         }

                         // Arbitrarily decide whether to replace each seed component
                         // with a component or a feature
                         ProcessSeedComponentArray(ref dcpSeedComps);

                         dispWrapArr = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(dcpSeedComps);
                         dcpDefinition.SeedComponentArray = dispWrapArr;

                         // Update the feature definition
                         swFeature.ModifyDefinition(dcpDefinition, swModel, null);

                         break;
                 }
             }

         }

         private void ProcessSeedComponentArray(ref object[] vSeedComps)
         {
             object[] replacementSeeds = null;
             Array.Resize(ref replacementSeeds, (vSeedComps.GetUpperBound(0) + 1));

             // Iterate over each seed component
             int iSeed = 0;
             for (iSeed = 0; iSeed <= vSeedComps.GetUpperBound(0); iSeed++)
             {
                 Feature swCompFeat = default(Feature);
                 swCompFeat = (Feature)vSeedComps[iSeed];
                 Debug.Print("        Seed " + iSeed +  ": " + swCompFeat.Name);

                 // Access the seed component represented by the feature
                 Component2 swComp =  default(Component2);
                 swComp = (Component2)swCompFeat.GetSpecificFeature2();

                 // Arbitrarily decide whether to replace this seed component
                 // with a component or a feature
                 if (iSeed % 2 == 0)
                 {
                     replacementSeeds[iSeed] = swComp;
                 }
                 else
                 {
                     replacementSeeds[iSeed] = swCompFeat;
                 }
             }

             // Replace the seed array
             vSeedComps = (object[])replacementSeeds;

         }

         public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
         {
             int ArraySize = 0;
             ArraySize = Objects.GetUpperBound(0);
             DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
             int ArrayIndex = 0;
             for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
             {
                 d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
             }
             return d;

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
