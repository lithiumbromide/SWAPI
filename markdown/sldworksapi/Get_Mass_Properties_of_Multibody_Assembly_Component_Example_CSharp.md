---
title: "Get Mass Properties of Multibody Assembly Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm"
---

# Get Mass Properties of Multibody Assembly Component Example (C#)

This example shows how to get the mass properties of a multibody assembly component in which an assembly cut-extrude feature is created.

**NOTES:**

-

  ```vb
  An assembly component, i.e., a part or subassembly, can contain  one or more assembly-level features. Some types of assembly features, e.g., cut extrude, can affect the mass properties. Assembly features are not present in the part or subassembly.
  ```
-

  ```vb
  Mass property values returned are relative to the component origin, not the assembly origin.
  ```

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified multibody part document
//    and assembly document template exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified multibody part document.
// 2. Creates an assembly using the specified multibody
//    part document.
// 3. Creates an assembly cut-extrude feature.
// 4. Selects the multibody component.
// 5. Gets the mass property values of the multibody
//    component.
// 6. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------

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
            ModelDocExtension swDocExt = default(ModelDocExtension);
            MassProperty swMass = default(MassProperty);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swComp = default(Component2);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            object vBodyInfo = null;
            double[] vCoM = null;
            double[] vMoI = null;
            double[] vPrinAoIx = null;
            double[] vPrinAoIy = null;
            double[] vPrinAoIz = null;
            double[] vPrinMoI = null;
            bool bRet = false;
            int errors = 0;
            int warnings = 0;

            //Open multibody part document and create an assembly
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2017\\templates\\Assembly.asmdot", 0, 0, 0);
            swAssembly = (AssemblyDoc)swModel;
            swComp = (Component2)swAssembly.AddComponent5("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt", (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", -9.26777909171506E-05, 0, 4.8904806817518E-05);

            //Create an assembly cut-extrude feature
            swDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            bRet = swDocExt.SelectByID2("", "FACE", -0.0195381300573558, 0.0449999999998454, -0.00303401890568011, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.002956, -0.004701, 0.0);
            swModel.ClearSelection2(true);
            bRet = swDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swFeat = (Feature)swFeatMgr.FeatureCut3(true, false, false, 0, 0, 0.5, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            true, true, false, 0, 0, false);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelMgr.EnableContourSelection = false;

            //Select multibody component
            bRet = swDocExt.SelectByID2("multi_inter-1@Assem1", "COMPONENT", 0, 0, 0, false, 0, null, 0);

            swMass = (MassProperty)swDocExt.CreateMassProperty();
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent4(1, -1);
            object[] vBodies = new object[1];
            vBodies = (object[])swComp.GetBodies3((int)swBodyType_e.swSolidBody, out vBodyInfo);
            DispatchWrapper[] dispArray = ObjectArrayToDispatchWrapperArray(vBodies);
            bRet = swMass.AddBodies((dispArray));

            //Get mass properties of selected component's bodies
            vCoM = (double[])swMass.CenterOfMass;
            vMoI = (double[])swMass.GetMomentOfInertia((int)swMassPropertyMoment_e.swMassPropertyMomentAboutCenterOfMass);
            vPrinAoIx = (double[])swMass.get_PrincipleAxesOfInertia(0);
            vPrinAoIy = (double[])swMass.get_PrincipleAxesOfInertia(1);
            vPrinAoIz = (double[])swMass.get_PrincipleAxesOfInertia(2);
            vPrinMoI = (double[])swMass.PrincipleMomentsOfInertia;
            Debug.Print("Component = " + swComp.Name2);
            Debug.Print("Configuration = " + swComp.ReferencedConfiguration);
            Debug.Print("Density = " + swMass.Density + " kg/m^3");
            Debug.Print("");
            Debug.Print("Center of mass = (" + vCoM[0] * 1000.0 + ", " + vCoM[1] * 1000.0 + ", " + vCoM[2] * 1000.0 + ") mm");
            Debug.Print("Volume = " + swMass.Volume * 1000000000.0 + " mm^3");
            Debug.Print("Area = " + swMass.SurfaceArea * 1000000.0 + " mm^2");
            Debug.Print("Mass = " + swMass.Mass + " kg");
            Debug.Print("Principle axes of inertia ");
            Debug.Print("  Ix = (" + vPrinAoIx[0] + ", " + vPrinAoIx[1] + ", " + vPrinAoIx[2] + ")");
            Debug.Print("  Iy = (" + vPrinAoIy[0] + ", " + vPrinAoIy[1] + ", " + vPrinAoIy[2] + ")");
            Debug.Print("  Iz = (" + vPrinAoIz[0] + ", " + vPrinAoIz[1] + ", " + vPrinAoIz[2] + ")");
            Debug.Print("Principle moments of inertia");
            Debug.Print("  Px = " + vPrinMoI[0] + " kg*m^2");
            Debug.Print("  Py = " + vPrinMoI[1] + " kg*m^2");
            Debug.Print("  Pz = " + vPrinMoI[2] + " kg*m^2");
            Debug.Print("Products of inerita");
            Debug.Print("  Lxx = " + vMoI[0] + " kg*m^2");
            Debug.Print("  Lxy = " + vMoI[1] + " kg*m^2");
            Debug.Print("  Lxz = " + vMoI[2] + " kg*m^2");
            Debug.Print("  Lyx = " + vMoI[3] + " kg*m^2");
            Debug.Print("  Lyy = " + vMoI[4] + " kg*m^2");
            Debug.Print("  Lyz = " + vMoI[5] + " kg*m^2");
            Debug.Print("  Lzx = " + vMoI[6] + " kg*m^2");
            Debug.Print("  Lzy = " + vMoI[7] + " kg*m^2");
            Debug.Print("  Lzz = " + vMoI[8] + " kg*m^2");

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
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
