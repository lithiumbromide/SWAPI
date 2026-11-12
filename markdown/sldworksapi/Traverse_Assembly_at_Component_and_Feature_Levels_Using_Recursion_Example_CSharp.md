---
title: "Traverse Assembly at Component and Feature Levels Using Recursion Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm"
---

# Traverse Assembly at Component and Feature Levels Using Recursion Example (C#)

This example shows how to traverse an assembly at the component and feature levels using recursion.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly document containing nested subassemblies.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Traverses the assembly.
 // 2. Examine the Immediate Window.
 //---------------------------------------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RecursiveTraverseAssemblyCSharp.csproj
{

    public partial class SolidWorksMacro
    {

        public void TraverseFeatureFeatures(Feature swFeat, long nLevel)
        {
            Feature swSubFeat;
            Feature swSubSubFeat;
            Feature swSubSubSubFeat;
            string sPadStr = " ";
            long i = 0;

            for (i = 0; i <= nLevel; i++)
            {
                sPadStr = sPadStr + " ";
            }
            while ((swFeat != null))
            {
                Debug.Print(sPadStr + swFeat.Name + " [" + swFeat.GetTypeName2() + "]");
                swSubFeat = (Feature)swFeat.GetFirstSubFeature();

                while ((swSubFeat != null))
                {
                    Debug.Print(sPadStr + "  " + swSubFeat.Name + " [" + swSubFeat.GetTypeName() + "]");
                    swSubSubFeat = (Feature)swSubFeat.GetFirstSubFeature();

                    while ((swSubSubFeat != null))
                    {
                        Debug.Print(sPadStr + "    " + swSubSubFeat.Name + " [" + swSubSubFeat.GetTypeName() + "]");
                        swSubSubSubFeat = (Feature)swSubSubFeat.GetFirstSubFeature();

                        while ((swSubSubSubFeat != null))
                        {
                            Debug.Print(sPadStr + "      " + swSubSubSubFeat.Name + " [" + swSubSubSubFeat.GetTypeName() + "]");
                            swSubSubSubFeat = (Feature)swSubSubSubFeat.GetNextSubFeature();

                        }

                        swSubSubFeat = (Feature)swSubSubFeat.GetNextSubFeature();

                    }

                    swSubFeat = (Feature)swSubFeat.GetNextSubFeature();

                }

                swFeat = (Feature)swFeat.GetNextFeature();

            }

        }

        public void TraverseComponentFeatures(Component2 swComp, long nLevel)
        {
            Feature swFeat;

            swFeat = (Feature)swComp.FirstFeature();
            TraverseFeatureFeatures(swFeat, nLevel);
        }
        public void TraverseComponent(Component2 swComp, long nLevel)
        {
            object[] vChildComp;
            Component2 swChildComp;
            string sPadStr = " ";
            long i = 0;

            for (i = 0; i <= nLevel - 1; i++)
            {
                sPadStr = sPadStr + " ";
            }

            vChildComp = (object[])swComp.GetChildren();
            for (i = 0; i < vChildComp.Length; i++)
            {
                swChildComp = (Component2)vChildComp[i];
                Debug.Print(sPadStr + "+" + swChildComp.Name2 + " <" + swChildComp.ReferencedConfiguration + ">");

                TraverseComponentFeatures(swChildComp, nLevel);
                TraverseComponent(swChildComp, nLevel + 1);
            }
        }
        public void TraverseModelFeatures(ModelDoc2 swModel, long nLevel)
        {
            Feature swFeat;

            swFeat = (Feature)swModel.FirstFeature();
            TraverseFeatureFeatures(swFeat, nLevel);
        }
        public void Main()
        {

            ModelDoc2 swModel;
            ConfigurationManager swConfMgr;
            Configuration swConf;
            Component2 swRootComp;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConf = (Configuration)swConfMgr.ActiveConfiguration;
            swRootComp = (Component2)swConf.GetRootComponent();

            System.Diagnostics.Stopwatch myStopwatch = new Stopwatch();
            myStopwatch.Start();

            Debug.Print("File = " + swModel.GetPathName());

            TraverseModelFeatures(swModel, 1);

            if (swModel.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
            {
                TraverseComponent(swRootComp, 1);
            }

            myStopwatch.Stop();
            TimeSpan myTimespan = myStopwatch.Elapsed;
            Debug.Print("Time = " + myTimespan.TotalSeconds + " sec");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }

}
```
