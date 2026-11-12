---
title: "Copy Component With Profile Center Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Component_With_Profile_Center_Mate_Example_CSharp.htm"
---

# Copy Component With Profile Center Mate Example (C#)

This example shows how to:

- create a new assembly.
- add two components to the assembly.
- create a profile center mate between the components.
- copy a component with that mate.

```
//--------------------------------------------------------
// Preconditions:
// 1. Open a new SOLIDWORKS Design session.
// 2. Copy public_documents\samples\tutorial\api\block20.sldprt and
//    cylinder20.sldprt to c:\temp.
// 3. Verify that the specified assembly document template exists.
//
// Postconditions:
// 1. Opens both parts.
// 2. Creates a new assembly.
// 3. Inserts both parts into the new assembly.
// 4. Creates a profile center mate between the two components.
// 5. Copies a component and the profile center mate.
// 6. To verify steps 4 and 5:
//    * Examine the graphics area and FeatureManager design tree.
//    * Expand Mates in the FeatureManager design tree.
//---------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            PartDoc swPart1 = default(PartDoc);
            PartDoc swPart2 = default(PartDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            Component2 swComponent1 = default(Component2);
            Component2 swComponent2 = default(Component2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Mate2 swMate = default(Mate2);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            DispatchWrapper[] dispWrapperComponentArray = new DispatchWrapper[1];
            Component2[] swComponentArray = new Component2[1];
            bool[] repeatArray = new bool[1];
            DispatchWrapper[] dispWrapperMateReferencesArray = new DispatchWrapper[1];
            double[] valueArray = new double[1];
            bool[] flipAlignmentArray = new bool[1];
            bool[] flipDimensionArray = new bool[1];
            bool[] lockRotationArray = new bool[1];
            int[] orientationArray = new int[1];

            // Open parts for new assembly
            swPart1 = (PartDoc)swApp.OpenDoc6("C:\\temp\\block20.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swPart2 = (PartDoc)swApp.OpenDoc6("C:\\temp\\cylinder20.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            // Open new assembly document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Assembly.asmdot", 0, 0, 0);
            swApp.ActivateDoc2("Assem1", false, ref errors);
            swAssemblyDoc = (AssemblyDoc)swModel;

            // Add components to assembly document
            swComponent1 = (Component2)swAssemblyDoc.AddComponent5("C:\\temp\\block20.sldprt", (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", 0.0522792702800426, 0.0658677995643489, 0.102016044707081);
            swComponent2 = (Component2)swAssemblyDoc.AddComponent5("C:\\temp\\cylinder20.sldprt", (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", 0.177061497059185, -0.00151244836160913, 0.0673233033157885);
            swModel.ViewZoomtofit2();

            // Add profile center mate
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0631695178495306, 0.0856797995642182, 0.137370061843797, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.141204290267694, 0.031253551638315, 0.0843440006535161, true, 1, null, 0);
            swMate = (Mate2)swAssemblyDoc.AddMate5((int)swMateType_e.swMatePROFILECENTER, (int)swMateAlign_e.swMateAlignALIGNED, true, 0.0762, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983,
            0.5235987755983, false, true, (int)swMateWidthOptions_e.swMateWidth_Centered, out errors);
            swModel.ClearSelection2(true);

            // Copy component with profile center mate
            swComponentArray[0] = swComponent2;
            dispWrapperComponentArray[0] = new DispatchWrapper(swComponentArray[0]);
            repeatArray[0] = true;
            dispWrapperMateReferencesArray[0] = new DispatchWrapper(null);
            valueArray[0] = 0.05;
            flipAlignmentArray[0] = true;
            flipDimensionArray[0] = true;
            lockRotationArray[0] = false;
            orientationArray[0] = 0;
            status = swAssemblyDoc.CopyWithMates2(dispWrapperComponentArray, repeatArray, dispWrapperMateReferencesArray, valueArray, flipAlignmentArray, flipDimensionArray, lockRotationArray, orientationArray);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
