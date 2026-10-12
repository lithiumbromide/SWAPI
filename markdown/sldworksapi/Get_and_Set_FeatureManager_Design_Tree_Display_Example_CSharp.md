---
title: "Get and Set FeatureManager Design Tree Display (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_FeatureManager_Design_Tree_Display_Example_CSharp.htm"
---

# Get and Set FeatureManager Design Tree Display (C#)

This example shows how to get and set properties related to displaying the FeatureManager design tree.

```vb
 //----------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the assembly and gets the FeatureManager design tree's display-related property
 //    design tree's display-related property  values.
 // 2. Examine both the Immediate window and the FeatureManager
 //    design tree, then press F5.
 // 3. Re-examine both the Immediate window and the FeatureManager
 //    design tree  to verify the changes.
 //
 // NOTE: Because this assembly document is used
 // elsewhere, do not save changes.
 //----------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace ViewFeatureManagerDesignTreeCSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModelDoc =  default(ModelDoc2);
             FeatureManager swFeatMgr =  default(FeatureManager);
             string document = null;
             int errors = 0;
             int warnings = 0;

             document = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm";

             swModelDoc = (ModelDoc2)swApp.OpenDoc6(document, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swFeatMgr = (FeatureManager)swModelDoc.FeatureManager;

             Debug.Print("----------------- Before changing FeatureManager design tree properties -----------------");
             Debug.Print("View dependencies     = " + swFeatMgr.ViewDependencies);
             Debug.Print("View features         = " + swFeatMgr.ViewFeatures);
             Debug.Print("Show feature details  = " + swFeatMgr.ShowFeatureDetails);
             Debug.Print("Show hierarchy only   = " + swFeatMgr.ShowHierarchyOnly);

             System.Diagnostics.Debugger.Break();
             // Examine the Immediate window and
             // FeatureManager design tree before
             // resuming the macro

             // Change details, dependencies, hierarchy, and
             // features-related properties
             if ((swFeatMgr.ViewDependencies))
             {
                 swFeatMgr.ViewFeatures =  true;
             }
             else
             {
                 swFeatMgr.ViewDependencies =  true;
             }

             if ((swFeatMgr.ShowFeatureDetails))
             {
                 swFeatMgr.ShowHierarchyOnly =  true;
             }
             else
             {
                 swFeatMgr.ShowFeatureDetails =  true;
             }

             Debug.Print("----------------- After changing FeatureManager design tree properties -----------------");
             Debug.Print("View dependencies     = " + swFeatMgr.ViewDependencies);
             Debug.Print("View features         = " + swFeatMgr.ViewFeatures);
             Debug.Print("Show feature details  = " + swFeatMgr.ShowFeatureDetails);
             Debug.Print("Show hierarchy only   = " + swFeatMgr.ShowHierarchyOnly);
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
