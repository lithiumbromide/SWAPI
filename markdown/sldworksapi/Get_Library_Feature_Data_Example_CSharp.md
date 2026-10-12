---
title: "Get Library Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Library_Feature_Data_Example_CSharp.htm"
---

# Get Library Feature Data Example (C#)

This example shows how to get data about library features in model documents.

```vb
 //-------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that contains at least one
 //    library feature.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Traverses the FeatureManager design tree searching for
 //    library features.
 // 2. Gets each library feature's data.
 // 3. Inspect the Immediate window.
 //-------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetReferences3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         bool boolstatus;
         ModelDoc2 ModelDoc2;
         Feature Feature;
         Feature NextFeature;
         LibraryFeatureData LibraryFeatureData;
         int placementPlaneType;
         Object placementPlane;
         string ConfigurationName;
         String[] vConfigs;
         int x;
         bool LinkToLibraryPart;
         int LocatingDimensionsCount;
         Object vLocDimName;
         double[] vLocDimVal;
         int i;
         bool bOverrideDimVal;
         int SizeDimensionsCount;
         Object vSizDimName;
         double[] vSizDimVal;
         int ReferencesCount;
         Object vRefType;
         Object vRefName;
         Object[] vRefs;

         public void Main()
         {
             ModelDoc2 = (ModelDoc2)swApp.ActiveDoc;

             // Traverse the FeatureManager design tree searching for library features
             Feature = (Feature)ModelDoc2.FirstFeature();

             while ((Feature != null))
             {
                 // Debug.Print(Feature.Name, Feature.GetTypeName());

                 // If feature is library feature, then get its data; otherwise,
                 // move onto the next feature in the FeatureManager design tree
                 if (Feature.GetTypeName() == "LibraryFeature")
                 {
                     Debug.Print("");
                     Debug.Print(Feature.Name + ",  " + Feature.GetTypeName());
                     LibraryFeatureData = (LibraryFeatureData)Feature.GetDefinition();
                     boolstatus = LibraryFeatureData.AccessSelections(ModelDoc2, null);

                     // Access the selections of the library feature that define it
                     Debug.Print("LibraryFeatureData.AccessSelections = " + boolstatus.ToString());

                     // Get its placement type
                     placementPlane = LibraryFeatureData.GetPlacementPlane2((int)swLibFeatureData_e.swLibFeatureData_PartRespect, out placementPlaneType);
                     Debug.Print("PlacementPlaneType = " + placementPlaneType.ToString());

                     // Get the name of the active library feature configuration
                     ConfigurationName = LibraryFeatureData.ConfigurationName;

                     Debug.Print("ConfigurationName = " + ConfigurationName);

                     // Determine if the library feature is linked to
                     // the library feature part
                     LinkToLibraryPart = LibraryFeatureData.LinkToLibraryPart;
                     Debug.Print("LinkToLibraryPart = " + LinkToLibraryPart.ToString());

                     // If the library feature part document is open, or
                     // if the library feature is linked to the library feature
                     // part document, then get the names of all of the
                     // library feature configurations; if it's not open,
                     // then only the name of the active library configuration
                     // is returned
                     vConfigs = (String[])LibraryFeatureData.GetAllConfigurationNames();
                     Debug.Print("Configuration names :");

                     if ((vConfigs != null))
                     {
                         for (x = vConfigs.GetLowerBound(0); x <= vConfigs.GetUpperBound(0); x++)
                         {
                             Debug.Print(" " + vConfigs[x]);
                         }
                     }

                     // Get the number of locating dimensions
                     LocatingDimensionsCount = LibraryFeatureData.GetDimensionsCount(0);
                     Debug.Print("LocatingDimensionsCount = " + LocatingDimensionsCount.ToString());

                     // Get the locating dimensions
                     vLocDimVal = (double[])LibraryFeatureData.GetDimensions(0, out vLocDimName);
                     Debug.Print("Locating dimensions :");

                     if ((vLocDimName != null))
                     {
                         String[] dimNames = (String[])vLocDimName;
                         for (i = dimNames.GetLowerBound(0); i <= dimNames.GetUpperBound(0); i++)
                         {
                             Debug.Print(" " + dimNames[i], vLocDimVal[i]);
                         }
                     }

                     // Determine if existing dimension values of the library
                     // feature can be overridden
                     bOverrideDimVal = LibraryFeatureData.OverrideDimension;
                     Debug.Print("OverrideDimension = " + bOverrideDimVal.ToString());

                     // Get the number of feature dimensions
                     SizeDimensionsCount = LibraryFeatureData.GetDimensionsCount(1);
                     Debug.Print("SizeDimensionsCount = " + SizeDimensionsCount.ToString());

                     // Get the feature dimensions
                     vSizDimVal = (double[])LibraryFeatureData.GetDimensions(1, out vSizDimName);
                     Debug.Print("Size dimensions :");

                     if ((vSizDimName != null))
                     {
                         String[] sizDimNames = (String[])vSizDimName;
                         for (i = sizDimNames.GetLowerBound(0); i <= sizDimNames.GetUpperBound(0); i++)
                         {
                             Debug.Print(" " + sizDimNames[i], vSizDimVal[i]);
                         }
                     }

                     // Get the number of references
                     ReferencesCount = LibraryFeatureData.GetReferencesCount();
                     Debug.Print("GetReferencesCount = " + ReferencesCount.ToString());

                     // Get the references
                     vRefs = (object[])LibraryFeatureData.GetReferences3((int)swLibFeatureData_e.swLibFeatureData_PartRespect, out vRefType, out vRefName);
                     if ((vRefType != null))
                     {
                         int[] refTypes = (int[])vRefType;
                         string[] refNames = (string[])vRefName;
                         Debug.Print("Reference types and names: ");
                         for (i = refTypes.GetLowerBound(0); i <= refTypes.GetUpperBound(0); i++)
                         {
                             Debug.Print(" " + refTypes[i].ToString() +  ", " + (string)refNames[i]);
                         }
                     }

                     //Release the selections that define the library feature
                     LibraryFeatureData.ReleaseSelectionAccess();
                 }

                 // Get the next feature until there are no more
                 NextFeature = (Feature)Feature.GetNextFeature();
                 Feature = null;
                 Feature = NextFeature;
                 NextFeature = null;
             }
         }

         public SldWorks swApp;
     }
 }
```
