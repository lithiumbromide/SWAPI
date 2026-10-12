---
title: "Copy Components With Mates to Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Components_With_Mates_To_Assembly_Example_CSharp.htm"
---

# Copy Components With Mates to Assembly Example (C#)

This example shows how to copy components with mates in an assembly.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.SLDASM.
 // 2. Inspect Leg<1> and Leg<2> in the assembly.
 //
 // Postconditions:
 // 1. Replaces Leg<1> with a copy of Leg<2>.
 // 2. Inspect Leg<2> and leg<3> in the assembly.
 //
 // NOTE: Because this assembly is used elsewhere, do not save any changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using System.Runtime.InteropServices;
namespace CopyComponentsWithMatesToAssembly_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            bool[] blRepeat = new bool[3];
            bool[] blFlip = new bool[3];
            object SelectedComps = null;
            object RepeatOptions = null;
            object[] MateRefs = new object[3];
            object InpValues = null;
            object FlipValues = null;
            AssemblyDoc swAssy = default(AssemblyDoc);
            Component2 swItem = default(Component2);
            Feature swFeature = default(Feature);
            RefPlane refPlane = default(RefPlane);
            object[] arrMateEntities = new object[3];
            object[] arrCompsToCopy = new object[1];
            bool boolstatus = false;
            double[] dValues = new double[3];

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("Leg-1@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swModel.EditDelete();

            swModel.ClearSelection2(true);

            boolstatus = swModelDocExt.SelectByID2("Leg-2@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swItem = (Component2)swSelMgr.GetSelectedObject6(1, -1);
            arrCompsToCopy[0] = swItem;
            arrMateEntities[0] = null;
            arrMateEntities[1] = null;
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Left End@Universal Beam-1@mobile gantry", "PLANE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            refPlane = (RefPlane)swFeature.GetSpecificFeature2();
            arrMateEntities[2] = refPlane;

            swModel.ClearSelection2(true);

            blRepeat[0] = true;
            blRepeat[1] = true;
            blRepeat[2] = false;
            SelectedComps = arrCompsToCopy;
            RepeatOptions = blRepeat;
            MateRefs = arrMateEntities;
            dValues[0] = 0.0;
            dValues[1] = 0.0;
            dValues[2] = 0.0;
            InpValues = dValues;
            blFlip[0] = false;
            blFlip[1] = false;
            blFlip[2] = false;
            FlipValues = blFlip;
            DispatchWrapper[] disparrCompsToCopy = new DispatchWrapper[1];
            disparrCompsToCopy[0] = new DispatchWrapper(arrCompsToCopy[0]);
            DispatchWrapper[] dispMateRefs = new DispatchWrapper[3];
            dispMateRefs[0] = new DispatchWrapper(MateRefs[0]);
            dispMateRefs[1] = new DispatchWrapper(MateRefs[1]);
            dispMateRefs[2] = new DispatchWrapper(MateRefs[2]);

            //Repeat all mates except the coincident mate with "Right End@Universal Beam-1"
            swAssy.CopyWithMates((disparrCompsToCopy), RepeatOptions, (dispMateRefs), InpValues, FlipValues);
            swAssy.EditRebuild();
        }
        public SldWorks swApp;
    }
}
```
