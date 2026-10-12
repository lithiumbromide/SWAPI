---
title: "Remove Material Properties from Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Material_From_Bodies_Example_CSharp.htm"
---

# Remove Material Properties from Bodies Example (C#)

This example shows how to remove materials from bodies in a multibody part. This example also works with a part with a single body and an assembly with single and multibody components.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
// 2. Expand Solid Bodies(2) > right-click  Extrude-Thin1 > click
//    Appearances > Body > any color in Appearances(color) > OK.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the FeatureManager design tree.
// 2. Removes the color that you applied to Extrude-Thin1.
// 3. Examine the Immediate window and graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        PartDoc swPart;
        object vBody;
        bool bRet;

        public void Main()
        {
            int j = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModel.ClearSelection2(true);
            Debug.Print("File = " + swModel.GetPathName());
            switch (swModel.GetType())
            {
                case (int)swDocumentTypes_e.swDocPART:
                    swPart = (PartDoc)swModel;
                    // Solid bodies
                    object[] vBodyArr = null;
                    Body2 swBody = default(Body2);
                    vBodyArr = (object[])swPart.GetBodies2((int)swBodyType_e.swSolidBody, true);
                    if ((vBodyArr != null))
                    {
                        Debug.Print("  Number of solid bodies: " + vBodyArr.Length);
                        Debug.Print("    Material removed from: ");
                        j = 1;
                        foreach (object vBody_loopVariable in vBodyArr)
                        {
                            vBody = vBody_loopVariable;
                            swBody = (Body2)vBody;
                            string[] vConfigName = null;
                            vConfigName = (string[])swModel.GetConfigurationNames();
                            bRet = swBody.RemoveMaterialProperty((int)swInConfigurationOpts_e.swAllConfiguration, (vConfigName));
                            Debug.Print("      Body " + j + "? " + bRet);
                            j = j + 1;
                        }
                    }
                    break;
                case (int)swDocumentTypes_e.swDocASSEMBLY:
                    ProcessAssembly(swApp, swModel);
                    break;
                default:
                    return;
                    break;
            }

        }

        public void ProcessAssembly(SldWorks swApp, ModelDoc2 swModel)
        {
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConf = default(Configuration);
            Component2 swRootComp = default(Component2);

            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConf = (Configuration)swConfigMgr.ActiveConfiguration;
            swRootComp = (Component2)swConf.GetRootComponent3(true);
            ProcessComponent(swApp, swModel, swRootComp);

        }

        public void ProcessComponent(SldWorks swApp, ModelDoc2 swModel, Component2 swComp)
        {
            object[] vChildComp = null;
            Component2 swChildComp = null;
            object childComp = null;

            Debug.Print(swComp.Name2 + " <" + swComp.ReferencedConfiguration + ">");
            // Solid bodies
            object[] vBodyArr = null;
            Body2 swBody = default(Body2);
            vBodyArr = (object[])swComp.GetBodies2((int)swBodyType_e.swSolidBody);
            if ((vBodyArr != null))
            {
                Debug.Print("       Number of bodies: " + vBodyArr.Length);
                foreach (object vBody_loopVariable in vBodyArr)
                {
                    vBody = vBody_loopVariable;
                    swBody = (Body2)vBody;
                    string[] vConfigName = null;
                    Debug.Print("         Body name: " + swBody.Name);
                    vConfigName = (string[])swModel.GetConfigurationNames();
                    bRet = swBody.RemoveMaterialProperty((int)swInConfigurationOpts_e.swThisConfiguration, (vConfigName));
                    Debug.Print("           Material removed from body? " + bRet);
                }
            }
            vChildComp = (object[])swComp.GetChildren();
            foreach (object childComp_loopVariable in vChildComp)
            {
                childComp = (object)childComp_loopVariable;
                swChildComp = (Component2)childComp;
                ProcessComponent(swApp, swModel, swChildComp);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
