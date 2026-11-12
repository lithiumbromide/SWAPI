---
title: "Specify IGES Levels and Values, Then Import IGES File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm"
---

# Specify IGES Levels and Values, Then Import IGES File Example (C#)

This example shows how to:

- specify levels and values for importing IGES data.
- import an IGES file.

```
//------------------------------------------------
// Preconditions: Substitute the path and name
// of your IGES file where noted in the code.
//
// Postconditions:
// 1. Creates a folder named Layer 25.
// 2. Imports the specified IGES file into SOLIDWORKS Design
//    and moves the imported IGES features to Layer 25.
// 3. To verify, examine the graphics area and
//    FeatureManager design tree.
//--------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ImportIGESFilesCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

            ModelDoc2 model = default(ModelDoc2);
            bool boolstatus = false;
            string fileName = null;
            string argString = null;
            ImportIgesData importData = default(ImportIgesData);
            int Err = 0;
            bool orgSetting = false;
            bool allLevels = false;
            object vOnlyLev = null;
            int[] onlyLev = new int[2];
            int oneLev = 0;
            Feature lastFeature = default(Feature);
            Feature newFolder = default(Feature);
            string newFolderName = "";
            string lastFeatureName = null;

            model = (ModelDoc2)swApp.ActiveDoc;
            // Substitute the path and name of your IGES file
            fileName = "C:\\beam_with_holes.igs";
            // "r" means open new document
            // "i" means insert into existing document
            if (model == null)
            {
                argString = "r";
                // There is an existing part, so use it
            }
            else
            {
                argString = "i";
            }
            // Fill in the import data
            importData = (ImportIgesData)swApp.GetImportFileData(fileName);
            if ((importData != null))
            {
                // Test the various flags
                importData.IncludeSurfaces = true;
                importData.IncludeCurves = true;
                importData.CurvesAsSketches = true;
                // False = Curves as Curves
                importData.ProcessByLevel = false;
                // Test all levels
                //        allLevels = True
                // False = levels specified in vOnlyLev
                //        newFolderName = "All levels"
                // or, test multiple levels
                //        onlyLev(0) = 0
                //        onlyLev(1) = 6
                //        vOnlyLev = onlyLev
                //        newFolderName = "Layer 0 and 6"
                // Or, test individual levels
                oneLev = 25;
                vOnlyLev = oneLev;
                newFolderName = "Layer " + oneLev.ToString();
                boolstatus = importData.SetLevels(allLevels, (vOnlyLev));
            }

            // Keep the last feature to determine what's been added
            //   If this is a new document, that cannot be done, so
            //   just hard code the name of the Origin feature,
            //   which is currently the last feature in a new part document
            //   It is better to always create a new
            //   document first, and then call SldWorks::LoadFile4
            //   with "i" argString to avoid this potential problem
            if ((model != null))
            {
                lastFeature = (Feature)model.FeatureByPositionReverse(0);
                lastFeatureName = lastFeature.Name;
            }
            else
            {
                lastFeatureName = "Origin";
            }
            // Setting this user preference to true means that the IGES
            //   dialog is displayed
            // Setting this user preference to false means that the
            //   IGES dialog is not displayed, and the import IGES data
            //   is used if it is passed in, or, if it is not,
            //   then the default values for the dialog are used
            orgSetting = swApp.GetUserPreferenceToggle((int)swUserPreferenceToggle_e.swIGESImportShowLevel);
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swIGESImportShowLevel, false);
            model = (ModelDoc2)swApp.LoadFile4(fileName, argString, importData, ref Err);

            // swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swIGESImportShowLevel, orgSetting
            // If the SldWorks::LoadFile4 failed, do not continue
            if (model == null)
            {
                Debug.Print("Problem loading file.");
                return;
            }
            // Retrieve all of the features that were created
            // and move them into their own new folder
            model.ClearSelection2(true);
            // Select features that are then used by FeatureManager::InsertFeatureTreeFolder2
            // Either method of selection seems to take the same amount of time
            boolstatus = select_new_features_individually(model, lastFeatureName);
            // boolstatus = multiselect_new_features(model, lastFeatureName);
            if ((boolstatus))
            {
                newFolder = model.FeatureManager.InsertFeatureTreeFolder2((int)swFeatureTreeFolderType_e.swFeatureTreeFolder_Containing);
                if ((newFolder != null))
                {
                    newFolder.Name = newFolderName;
                }
                model.ClearSelection2(true);
            }
        }

        private bool select_new_features_individually(ModelDoc2 model, string lastFeatureName)
        {
            bool functionReturnValue = false;
            Feature testFeature = default(Feature);
            int loopCount = 0;
            bool boolstatus = false;
            functionReturnValue = false;
            loopCount = 0;
            testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            while (((testFeature != null)) && (!(testFeature.Name == lastFeatureName)))
            {
                loopCount = loopCount + 1;
                boolstatus = testFeature.Select2(true, 0);
                if (!(boolstatus = false))
                {
                    functionReturnValue = true;
                }
                testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            }
            return functionReturnValue;
        }

        private bool multiselect_new_features(ModelDoc2 model, string lastFeatureName)
        {
            bool functionReturnValue = false;
            Feature testFeature = default(Feature);
            int loopCount = 0;
            Feature[] featureList = null;
            object vFeatureList = null;
            int longstatus = 0;
            SelectData selData = default(SelectData);
            SelectionMgr selMgr = default(SelectionMgr);
            functionReturnValue = false;
            loopCount = 0;
            testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            while (((testFeature != null)) && (!(testFeature.Name == lastFeatureName)))
            {
                loopCount = loopCount + 1;
                testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            }
            Array.Resize(ref featureList, (loopCount + 1));

            loopCount = 0;
            testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            while (((testFeature != null)) && (!(testFeature.Name == lastFeatureName)))
            {
                featureList[loopCount] = testFeature;
                loopCount = loopCount + 1;
                testFeature = (Feature)model.FeatureByPositionReverse(loopCount);
            }

            vFeatureList = featureList;
            selMgr = (SelectionMgr)model.SelectionManager;
            selData = (SelectData)selMgr.CreateSelectData();
            longstatus = model.Extension.MultiSelect2((vFeatureList), true, selData);
            if (longstatus > 0)
            {
                functionReturnValue = true;
            }
            return functionReturnValue;
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
