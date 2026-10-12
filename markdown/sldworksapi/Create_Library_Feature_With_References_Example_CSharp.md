---
title: "Create Library Feature Data Object and Library Feature With References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Library_Feature_With_References_Example_CSharp.htm"
---

# Create Library Feature Data Object and Library Feature With References Example (C#)

This example shows how to create a library feature with references in order to position the library feature on a model.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template and library feature
//    exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part containing a boss extrude.
// 2. Creates a library feature data object.
//    a. Initializes the newly created library feature using
//       the specified library feature.
//    b. Gets the type of references required for the library
//       feature.
//    c. Sets the name of the active library feature configuration.
//    d. Selects the face where to create the library feature.
//    e. Creates the library feature.
//    f. Accesses the library feature and selects the edges where to
//       position the it.
//    g. Sets the references for positioning the library feature.
//    h. Updates the definition of the library feature.
//    i. Unsuppresses the library feature.
// 3. Examine the Immediate window, FeatureManager design tree, and
//    graphics area.
//-------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            Feature swFeature = default(Feature);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            FeatureManager swFeatureManager = default(FeatureManager);
            LibraryFeatureData swLibFeat = default(LibraryFeatureData);
            bool status = false;
            object[] sketchLines = null;
            object Refs = null;
            object RefTypes = null;
            int RefCount = 0;
            int k = 0;
            int i = 0;
            DispatchWrapper[] LibRefs = null;

            // Create part
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchManager = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(0, 0, 0, 1, 0.5, 0);
            swModel.ShowNamedView2("*Trimetric", 8);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.01, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swSelectionManager.EnableContourSelection = false;

            // Create library feature
            swLibFeat = (LibraryFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmLibraryFeature);

            // Initialize newly created library feature using the specified library part
            status = swLibFeat.Initialize("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\design library\\features\\metric\\slots\\straight slot.sldlfp");

            // Get the type of references required for the library feature
            RefCount = swLibFeat.GetReferencesCount();
            Refs = (object[])swLibFeat.GetReferences2((int)swLibFeatureData_e.swLibFeatureData_FeatureRespect, out RefTypes);

            if ((RefTypes != null))
            {
                Debug.Print("Types of references required (edge = 1): ");
                int[] RefType = (int[])RefTypes;
                for (k = RefType.GetLowerBound(0); k <= RefType.GetUpperBound(0); k++)
                {
                    Debug.Print("    " + RefType[k].ToString());
                }
            }

            // Set the name of the active library feature configuration
            swLibFeat.ConfigurationName = "Default";

            // Select the face where to create the library feature
            status = swModelDocExt.SelectByID2("", "FACE", 0.522458766456054, 0.288038964184011, 0.00999999999987722, false, 0, null, 0);

            // Create the library feature
            swFeature = (Feature)swFeatureManager.CreateFeature(swLibFeat);

            // Access the library feature to position it on the part
            swLibFeat = null;
            swLibFeat = (LibraryFeatureData)swFeature.GetDefinition();
            status = swLibFeat.AccessSelections(swModel, null);

            // Select the edges where to position the library feature
            status = swModelDocExt.SelectByID2("", "EDGE", 0.960865149149924, 0.497807163546383, 0.0131011390528215, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.99866860703213, 0.481385806014544, 0.0113313929676906, true, 0, null, 0);

            int selCount = 0;
            selCount = swSelectionManager.GetSelectedObjectCount2(-1);

            object[] selectedObjects = new object[selCount];

            for (i = 0; i < selCount; i++)
            {
                object selectedObject = null;
                selectedObject = (object)swSelectionManager.GetSelectedObject6(i + 1, -1);
                selectedObjects[i] = selectedObject;
            }

            // Convert the .NET array to IDispatch
            LibRefs = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray((selectedObjects));

            // Set the references for positioning the library feature on the part
            swLibFeat.SetReferences(LibRefs);

            // Update the definition of the library feature
            status = swFeature.ModifyDefinition(swLibFeat, swModel, null);

            // Unsuppress the library feature
            status = swModelDocExt.SelectByID2("straight slot<1>", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModel.EditUnsuppress2();

            swModel.ClearSelection2(true);
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
        public DispatchWrapper[] LibRefs;

    }
}
```
