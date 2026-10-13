---
title: "Add and Edit Misaligned Symmetric Concentric Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_CSharp.htm"
---

# Add and Edit Misaligned Symmetric Concentric Mate Example (C#)

This example shows how to add and edit a misaligned symmetric concentric mate between components.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the parts to open and assembly template exist.
// 2. Open a new session of SOLIDWORKS Design to ensure that the assembly
//    document's title is Assem1.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Opens wheel_hub.sldprt.
// 2. Opens a new assembly document titled Assem1 and adds
//    wheel_hub.sldprt as a component.
// 3. Opens and adds beam with holes.sldprt as another component.
// 4. Adds a concentric mate between the components.
// 5. Adds a misaligned symmetric concentric mate
//    between the components.
// 6. Edits the misaligned symmetric concentric mate.
// 7. Examine the Immediate window, graphics area, and the mates
//    in the Mates folder in the FeatureManager design tree.
//
// NOTE: Because the parts are used elsewhere, do not save changes.
//-----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            Component2 swInsertedComponent = default(Component2);
            MathUtility swMathUtil = default(MathUtility);
            MathTransform swTransform = default(MathTransform);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Mate2 swMate = default(Mate2);
	    Mate2 swLinkedMate = default(Mate2);
            Component2 swComp = default(Component2);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            Feature swFeature = default(Feature);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            double swSheetWidth = 0;
            double swSheetHeight = 0;
            string AssemblyTitle = null;
            double[] TransformData = new double[16];
            object TransformDataObj = null;

            //Open the part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\wheel_hub.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swApp.ActivateDoc2("wheel_hub.sldprt", false, ref errors);

            //Create an assembly
            swSheetWidth = 0;
            swSheetHeight = 0;
            swAssembly = (AssemblyDoc)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2018\\templates\\Assembly.asmdot", 0, swSheetWidth, swSheetHeight);
            swModel = (ModelDoc2)swAssembly;
            AssemblyTitle = swModel.GetTitle();

            //Add the part to the assembly
            swInsertedComponent = (Component2)swAssembly.AddComponent5(fileName, (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", -0.000181145833835217, 0.000107469465717713, 2.25750183631135E-05);
            swApp.CloseDoc(fileName);
            TransformData[0] = 1;
            TransformData[1] = 0;
            TransformData[2] = 0;
            TransformData[3] = 0;
            TransformData[4] = 1;
            TransformData[5] = 0;
            TransformData[6] = 0;
            TransformData[7] = 0;
            TransformData[8] = 1;
            TransformData[9] = 0;
            TransformData[10] = 0;
            TransformData[11] = 0;
            TransformData[12] = 1;
            TransformData[13] = 0;
            TransformData[14] = 0;
            TransformData[15] = 0;
            TransformDataObj = (object)TransformData;
            swMathUtil = (MathUtility)swApp.GetMathUtility();
            swTransform = (MathTransform)swMathUtil.CreateTransform((TransformDataObj));
            status = swInsertedComponent.SetTransformAndSolve2(swTransform);

            //Open and add another part to the assembly
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\beam with holes.sldprt";
            swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_AutoMissingConfig, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swApp.ActivateDoc3(AssemblyTitle, true, 0, ref errors);
            swAssembly = (AssemblyDoc)swModel;
            swInsertedComponent = (Component2)swAssembly.AddComponent5(fileName, (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", -0.0543800538871437, -0.10948954091873, 0.0944189997389913);
            swApp.CloseDoc(fileName);
            TransformData[0] = 1;
            TransformData[1] = 0;
            TransformData[2] = 0;
            TransformData[3] = 0;
            TransformData[4] = 1;
            TransformData[5] = 0;
            TransformData[6] = 0;
            TransformData[7] = 0;
            TransformData[8] = 1;
            TransformData[9] = -0.179380053887144;
            TransformData[10] = -0.0894895409187302;
            TransformData[11] = 0.0744189997389913;
            TransformData[12] = 1;
            TransformData[13] = 0;
            TransformData[14] = 0;
            TransformData[15] = 0;
            TransformDataObj = (object)TransformData;
            swMathUtil = (MathUtility)swApp.GetMathUtility();
            swTransform = (MathTransform)swMathUtil.CreateTransform((TransformDataObj));

            //Add a concentric mate
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByRay(-0.158811046822791, -0.11180606883903, 0.110029416510201, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, true, 1,
            0);
            status = swModelDocExt.SelectByRay(-0.0595820179927387, -0.0282041473137156, 0.0120989536100637, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, true, 1,
            0);
            swMate = (Mate2)swAssembly.AddMate5((int)swMateType_e.swMateCONCENTRIC, (int)swMateAlign_e.swMateAlignALIGNED, false, 0.128546596088087, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983,
            0.5235987755983, false, false, 0, out errors);
            swModel.ClearSelection2(true);
            swModel.EditRebuild3();

            //Move a component in order to add another mate
            status = swModelDocExt.SelectByID2("beam with holes-1@Assem1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            TransformData[0] = 0.999268594246539;
            TransformData[1] = -0.0382397247969312;
            TransformData[2] = 0;
            TransformData[3] = 0.0382397247969312;
            TransformData[4] = 0.999268594246539;
            TransformData[5] = 0;
            TransformData[6] = 0;
            TransformData[7] = 0;
            TransformData[8] = 1;
            TransformData[9] = -0.0817169203602251;
            TransformData[10] = -0.00405863499514564;
            TransformData[11] = 0.158954897029145;
            TransformData[12] = 1;
            TransformData[13] = 0;
            TransformData[14] = 0;
            TransformData[15] = 0;
            TransformDataObj = (object)TransformData;
            swMathUtil = (MathUtility)swApp.GetMathUtility();
            swTransform = (MathTransform)swMathUtil.CreateTransform((TransformDataObj));
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swComp = (Component2)swSelectionManager.GetSelectedObjectsComponent4(1, -1);
            status = swComp.SetTransformAndSolve2(swTransform);

            //Add a misaligned symmetric concentric mate
            status = swModelDocExt.SelectByRay(-0.0362917984178921, -0.0292363280984205, 0.194521666713399, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(0.054967212945769, -0.0278611795938559, 0.0112380964281442, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, true, 1, 0);
            Debug.Print("Misaligned concentric mate:");
            swMate = (Mate2)swAssembly.AddConcentricMateWithTolerance((int)swMateAlign_e.swMateAlignALIGNED, (int)swConcentricAlignmentType_e.swConcentricAlignSymmetric, false, 0, out errors);
            if (errors == 1)
            {
                Debug.Print("  Added");

            }
            else
            {
                Debug.Print("  Not added");
            }

            swModel.ClearSelection2(true);

            //Edit the misaligned symmetric concentric mate
            //and change its position from symmetric to aligned
            status = swModelDocExt.SelectByRay(0.0548392523382404, -0.0277425865184, 0.00906375356890976, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00107347349835279, 2, false, 0, 0);
            status = swModelDocExt.SelectByRay(0.00980255664001106, -0.0292099642897483, 0.193646683964346, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00107347349835279, 2, true, 0, 0);
            status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, true, 0, null, 0);
            swAssembly.EditConcentricMate((int)swMateAlign_e.swMateAlignALIGNED, (int)swConcentricAlignmentType_e.swConcentricAlignThisMate, true, 0.095, out errors);

            swModel.ClearSelection2(true);

            if (errors == 1)
            {
                Debug.Print("  Edited");
                status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, true, 0, null, 0);
                swFeature = (Feature)swSelectionManager.GetSelectedObject6(1, -1);
                swMate = (Mate2)swFeature.GetSpecificFeature2();
```

```vb
                 //Get the linked concentric mate
                 swLinkedMate = (Mate2)swMate.GetLinkedMate();
                 //Get current misaligned deviation
                 Debug.Print("    Current misalignment deviation: " + swLinkedMate.GetCurrentMisalignedDeviation());
                 //Do not use document property value for misalignment deviation
                 swMate.SetUseMisalignedDeviationDocumentProperty(false);
                 Debug.Print("    Use document property? " + swMate.GetUseMisalignedDeviationDocumentProperty());
                 //Change mate alignment type to symmetric
                 swLinkedMate.SetConcentricAlignmentType((int)swConcentricAlignmentType_e.swConcentricAlignSymmetric);
                 Debug.Print("    Concentric alignment type as defined in swConcentricAlignmentType_e: " + swLinkedMate.GetConcentricAlignmentType());
                 //Set maximum misalignment deviation
                 swMate.SetMaximumMisalignedDeviation(0.102);
                 Debug.Print("    Maximum misalignment deviation: " + swMate.GetMaximumMisalignedDeviation());
```

```
            }
            else
            {
                Debug.Print("  Not edited");
            }

            swModel.ClearSelection2(true);
            swModel.EditRebuild3();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
