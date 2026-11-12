---
title: "Set Components and Transforms for Interference Detection Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm"
---

# Set Components and Transforms for Interference Detection Example (C#)

This example shows how to:

- move an assembly component to an interfering position by replacing its transform.
- detect interference.

This example also shows how to apply absolute transforms to all components in order to multiply by identity transforms, which results in the components remaining in their current positions during interference detection.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly exists.
// 2. Copy and paste Main into SolidWorksMacro.cs of your macro.
// 3. Click Project > Add Class and copy and paste Class into Class1.cs.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly.
// 2. Gets the components of the assembly and their transforms.
// 3. Creates a new transform for Part1^AssemInterferenceDetection-2.
// 4. Sets the components and their transforms, using the existing
//    rotation and the translation from the assembly origin.
//    a. Gets the number of interferences.
//    b. Examine the graphics area at the System.Diagnostics.Debugger.Break()
//       statement to visually verify the interferences, then press F5.
//    c. Programmatically verifies that the number of interferences
//       is as expected.
//    d. Gets whether:
//       * each returned interference is correct.
//       * the components remained in their starting positions during
//         interference detection.
//       * the components are at their starting positions.
// 5. Examine the Immediate window and graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-------------------------------------------------------------------------
//Main
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ArrayList colStartingPositions = new ArrayList();

        public void Main()
        {
            Class1 Class1 = new Class1();
            Class1 = new Class1();

            int expectedNumberofInterferences = 0;
            expectedNumberofInterferences = 2;

            ArrayList expectedInterferenceVolumes = default(ArrayList);
            expectedInterferenceVolumes = new ArrayList();
            expectedInterferenceVolumes.Add(0.09);
            expectedInterferenceVolumes.Add(0.01);

            ArrayList expectedNumberOfInterferenceComps = default(ArrayList);
            expectedNumberOfInterferenceComps = new ArrayList();
            expectedNumberOfInterferenceComps.Add(2);
            expectedNumberOfInterferenceComps.Add(2);

            bool bResult = false;
            bResult = true;
            AssemblyDoc swAssem = default(AssemblyDoc);
            swAssem = (AssemblyDoc)OpenAssembly();

            RecordStartingPositions(swAssem);

            SelectAllComponents(swAssem);

            InterferenceDetectionMgr swInfrMgr = default(InterferenceDetectionMgr);
            swInfrMgr = (InterferenceDetectionMgr)swAssem.InterferenceDetectionManager;

            swInfrMgr.UseTransform = true;

            Component2[] swComps = new Component2[3];
            swComps[0] = (Component2)swAssem.GetComponentByName("Part1^AssemInterferenceDetection-1");
            swComps[1] = (Component2)swAssem.GetComponentByName("Part1^AssemInterferenceDetection-2");
            swComps[2] = (Component2)swAssem.GetComponentByName("Part1^AssemInterferenceDetection-3");
            MathTransform[] swXfms = new MathTransform[3];
            swXfms[0] = (MathTransform)swComps[0].Transform2;
            swXfms[1] = (MathTransform)swComps[1].Transform2;
            swXfms[2] = (MathTransform)swComps[2].Transform2;

            // Replacement transform for Part1^AssemInterferenceDetection-2
            double[] dXfm = new double[16];

            // Use existing rotation
            double[] vXfmCurrent = null;
            vXfmCurrent = (double[])swXfms[1].ArrayData;
            dXfm[0] = (double)vXfmCurrent[0];
            dXfm[1] = (double)vXfmCurrent[1];
            dXfm[2] = (double)vXfmCurrent[2];
            dXfm[3] = (double)vXfmCurrent[3];
            dXfm[4] = (double)vXfmCurrent[4];
            dXfm[5] = (double)vXfmCurrent[5];
            dXfm[6] = (double)vXfmCurrent[6];
            dXfm[7] = (double)vXfmCurrent[7];
            dXfm[8] = (double)vXfmCurrent[8];
            // Translation from assembly origin
            dXfm[9] = (double)0.9;
            dXfm[10] = (double)0.1;
            dXfm[11] = (double)0;
            dXfm[12] = (double)1;
            dXfm[13] = (double)0;
            dXfm[14] = (double)0;
            dXfm[15] = (double)0;
            dXfm[1] = (double)0;
            dXfm[2] = (double)0;

            MathUtility swMath = default(MathUtility);
            swMath = (MathUtility)swApp.GetMathUtility();
            swXfms[1] = (MathTransform)swMath.CreateTransform(dXfm);

            int lResult = 0;
            lResult = swInfrMgr.SetComponentsAndTransforms(swComps, swXfms);

            Debug.Print("Transforms applied:");
            if (lResult == (int)swSetComponentsAndTransformsStatus_e.swSetComponentsAndTransforms_Succeeded)
            {
                Debug.Print("  True");
            }
            else
            {
                Debug.Print("  False: " + lResult + " vs. " + (int)swSetComponentsAndTransformsStatus_e.swSetComponentsAndTransforms_Succeeded);
                bResult = false;
            }
            int actualNumberOfInterferences = 0;
            actualNumberOfInterferences = swInfrMgr.GetInterferenceCount();
            Debug.Print("Number of interferences: ");
            Debug.Print("  " + actualNumberOfInterferences);

            System.Diagnostics.Debugger.Break();
            // Examine the graphics area to verify
            // the interferences, then press F5

            bool bCorrectNumberofInterferences = false;
            bCorrectNumberofInterferences = expectedNumberofInterferences == actualNumberOfInterferences;
            Debug.Print("Correct number of interferences:");
            if (bCorrectNumberofInterferences)
            {
                Debug.Print("  True");
            }
            else
            {
                Debug.Print("  False: " + actualNumberOfInterferences + " vs. " + expectedNumberofInterferences);
                bResult = false;
            }
            bool bCorrectInterferences = false;
            object[] interferences;
            interferences = (object[])swInfrMgr.GetInterferences();
            bCorrectInterferences = VerifyInterferencesAgainstExpectation(interferences, expectedInterferenceVolumes, expectedNumberOfInterferenceComps);
            Debug.Print("Correct interferences:");
            if (bCorrectInterferences)
            {
                Debug.Print("  True");
            }
            else
            {
                Debug.Print("  False");
                bResult = false;
            }
            swInfrMgr.Done();

            bool bBackToStartingPositions = false;
            bBackToStartingPositions = VerifyFinishingPositions();
            Debug.Print("Components back at starting positions:");
            if (bBackToStartingPositions)
            {
                Debug.Print("  True");
            }
            else
            {
                Debug.Print("  False");
                bResult = false;
            }

        }
        public AssemblyDoc OpenAssembly()
        {
            swApp.CloseAllDocuments(true);
            DocumentSpecification docspec = default(DocumentSpecification);
            string assemblyFile = null;
            assemblyFile = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\AssemInterferenceDetection.sldasm";
            docspec = (DocumentSpecification)swApp.GetOpenDocSpec(assemblyFile);
            ModelDoc2 swModel = default(ModelDoc2);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModel = (ModelDoc2)swApp.OpenDoc7(docspec);
            AssemblyDoc swAssem = default(AssemblyDoc);
            swAssem = (AssemblyDoc)swModel;
            return swAssem;
        }

        public void RecordStartingPositions(AssemblyDoc swAssem)
        {
            colStartingPositions = new ArrayList();
            object[] vComponents = null;
            vComponents = (object[])swAssem.GetComponents(true);
            if ((vComponents != null))
            {
                foreach (object oneComp in vComponents)
                {
                    Component2 swComp = default(Component2);
                    swComp = (Component2)oneComp;
                    Class1 position = default(Class1);
                    position = new Class1();
                    position.RecordReferencePosition(swComp);
                    colStartingPositions.Add(position);
                }
            }
        }
        public bool VerifyFinishingPositions()
        {
            bool bResult = false;
            bResult = true;

            Debug.Print("Position of: ");
            foreach (Class1 position in colStartingPositions)
            {
                if (position.IsAtReferencePosition())
                {
                    Debug.Print("  " + position.Name + " has not moved");
                }
                else
                {
                    Debug.Print("  " + position.Name + " has moved");
                    bResult = false;
                }
            }
            return bResult;
        }
        public bool VerifyInterferencesAgainstExpectation(object[] vInterferences, System.Collections.ArrayList expectedVolumes, System.Collections.ArrayList expectedCompCounts)
        {
            bool bResult = false;
            bResult = true;
            if ((vInterferences == null))
            {
                Debug.Print("IInterferenceDetectionMgr::GetInterferences returned:");
                if (expectedVolumes.Count == 0)
                {
                    Debug.Print("  Null as expected");
                }
                else
                {
                    Debug.Print("  Null unexpectedly");
                    bResult = false;
                }
            }
            else
            {
                int numInterferences = 0;
                numInterferences = vInterferences.GetUpperBound(0) - vInterferences.GetLowerBound(0) + 1;
                if (numInterferences != expectedVolumes.Count)
                {
                    Debug.Print("IInterferenceDetectionMgr::GetInterferences returned unexpected number of interferences: " + numInterferences + " vs. " + expectedVolumes.Count);
                    bResult = false;
                }
                // Cannot assume the same order
                // Try to find matches for each returned interference
                int i = 0;

                Debug.Print("Match found for calculated interference:");
                for (i = vInterferences.GetLowerBound(0); i <= vInterferences.GetUpperBound(0); i++)
                {
                    Interference swInterference = default(Interference);
                    swInterference = (Interference)vInterferences[i];
                    double volume = 0;
                    volume = swInterference.Volume;
                    int compCount = 0;
                    compCount = swInterference.GetComponentCount();
                    bool bFoundMatch = false;
                    bFoundMatch = false;
                    int j;
                    for (j = 0; j < (expectedVolumes.Count); j++)
                    {
                        double expVol;
                        expVol = (double)expectedVolumes[j];
                        double expCompCounts;
                        expCompCounts = (int)expectedCompCounts[j];
                        if (Class1.EqualWithinTolerance(expVol, volume) & (expCompCounts == compCount))
                        {
                            bFoundMatch = true;
                            expectedVolumes.RemoveAt(j);
                            expectedCompCounts.RemoveAt(j);
                            break;
                        }
                    }
                    if (bFoundMatch)
                    {
                        Debug.Print("  " + i + ": Volume = " + volume.ToString("0.000000") + " & Component count = " + compCount);

                    }
                    else
                    {
                        Debug.Print("  " + i + ": Volume = " + volume.ToString("0.000000") + " & Component count = " + compCount);

                        bResult = false;
                    }
                }
                int k;
                if (expectedVolumes.Count > 0)
                {
                    for (k = 0; k < (expectedVolumes.Count); k++)
                    {
                        double expVolumes;
                        expVolumes = (double)expectedVolumes[k];
                        Debug.Print("No match found for expected interference: " + k + ": Volume = " + (expVolumes.ToString("0.000000") + " & Component count = " + expectedCompCounts[k]));
                    }
                }
            }
            return bResult;
        }
        public void SelectAllComponents(AssemblyDoc swAssem)
        {
            ModelDoc2 swModel = default(ModelDoc2);
            swModel = (ModelDoc2)swAssem;
            swModel.ClearSelection2(true);

            object[] vComponents = null;
            vComponents = (object[])swAssem.GetComponents(true);
            if ((vComponents != null))
            {
                foreach (object vComp in vComponents)
                {
                    Component2 swComp = default(Component2);
                    swComp = (Component2)vComp;
                    swComp.Select4(true, null, false);
                }
            }
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

```
Back to top
```

```
//Class

using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using Macro1CSharp;

public class Class1
{

    private Component2 swComp;
    private MathTransform swReferenceTransform;
    public void RecordReferencePosition(Component2 swComponent)
    {
        swComp = (Component2)swComponent;
        swReferenceTransform = (MathTransform)swComp.Transform2;
    }
    public bool IsAtReferencePosition()
    {

        MathTransform swCurrentTransform = default(MathTransform);
        swCurrentTransform = (MathTransform)swComp.Transform2;

        MathTransform swProduct = default(MathTransform);
        swProduct = (MathTransform)swReferenceTransform.Multiply(swCurrentTransform.Inverse());

        double[] vProduct = null;
        vProduct = (double[])swProduct.ArrayData;
        double product0 = (double)vProduct[0];
        double product1 = (double)vProduct[1];
        double product2 = (double)vProduct[2];
        double product3 = (double)vProduct[3];
        double product4 = (double)vProduct[4];
        double product5 = (double)vProduct[5];
        double product6 = (double)vProduct[6];
        double product7 = (double)vProduct[7];
        double product8 = (double)vProduct[8];
        double product9 = (double)vProduct[9];
        double product10 = (double)vProduct[10];
        double product11 = (double)vProduct[11];
        double product12 = (double)vProduct[12];

        // Require identity transform
        bool bResult = false;
        bResult = EqualWithinTolerance(product0, 1);
        bResult = EqualWithinTolerance(product1, 0) & bResult;
        bResult = EqualWithinTolerance(product2, 0) & bResult;

        bResult = EqualWithinTolerance(product3, 0) & bResult;
        bResult = EqualWithinTolerance(product4, 1) & bResult;
        bResult = EqualWithinTolerance(product5, 0) & bResult;

        bResult = EqualWithinTolerance(product6, 0) & bResult;
        bResult = EqualWithinTolerance(product7, 0) & bResult;
        bResult = EqualWithinTolerance(product8, 1) & bResult;

        bResult = EqualWithinTolerance(product9, 0) & bResult;
        bResult = EqualWithinTolerance(product10, 0) & bResult;
        bResult = EqualWithinTolerance(product11, 0) & bResult;

        bResult = EqualWithinTolerance(product12, 1) & bResult;

        if (!bResult)
        {
            Debug.Print(Name + ":");
            Debug.Print(product0.ToString("0.000000") + "\t" + product1.ToString("0.000000") + "\t" + product2.ToString("0.000000"));
            Debug.Print(product3.ToString("0.000000") + "\t" + product4.ToString("0.000000") + "\t" + product5.ToString("0.000000"));
            Debug.Print(product6.ToString("0.000000") + "\t" + product7.ToString("0.000000") + "\t" + product8.ToString("0.000000"));
            Debug.Print(product9.ToString("0.000000") + "\t" + product10.ToString("0.000000") + "\t" + product11.ToString("0.000000"));
            Debug.Print(product12.ToString("0.000000"));
        }

        return bResult;
    }
    public string Name
    {
        get { return swComp.Name2; }
    }

    public static bool EqualWithinTolerance(double A, double B)
    {
        const double tolerance = 1E-05;
        double difference = 0;
        difference = Math.Abs(A - B);
        return difference < tolerance;
    }

}
```

[Back to top](#Top)
