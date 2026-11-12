---
title: "Get Collapsed Transform of Component in Exploded View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_CSharp.htm"
---

# Get Collapsed Transform of Component in Exploded View Example (C#)

This example shows how to get the collapsed transform of a component in an exploded view.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the name of the active configuration.
// 2. Creates five exploded views for the active configuration.
// 3. Gets the name of each exploded view for the active configuration
//    and shows each exploded view.
// 4. Gets the name of the exploded view shown in the model.
// 5. Selects a component and get its collapsed transform.
// 6. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
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
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            Component2 swComponent = default(Component2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            MathTransform swTransform = default(MathTransform);
            string activeConfigName = null;
            string[] viewNames = null;
            string viewName = null;
            int i = 0;
            double[] transformArrayData = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;

            //Get active configuration name
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
            activeConfigName = swConfig.Name;

            //Create five exploded views in the active configuration
            for (i = 0; i <= 4; i++)
            {
                swAssembly.CreateExplodedView();
            }

            //Get the name of each exploded view in the active configuration
            //and show each exploded view
            viewNames = (string[])swAssembly.GetExplodedViewNames2(activeConfigName);
            for (i = 0; i < viewNames.Length; i++)
            {
                viewName = viewNames[i];
                swAssembly.ShowExploded2(true, viewName);
            }

            //Get the name of exploded view shown in model
            viewName = "";
            swModelDocExt = swModel.Extension;
            swModelDocExt.IsExploded(out viewName);
            Debug.Print("Name of exploded view shown in model: " + viewName);

            //Select a component and get its collapsed transform
            swModelDocExt.SelectByID2("speaker_frame-1@speaker", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swComponent = (Component2)swSelectionMgr.GetSelectedObjectsComponent4(1, -1);
            Debug.Print("  Name of component whose collapsed transform to get in the exploded view: " + swComponent.Name2);
            swTransform = (MathTransform)swComponent.GetSpecificTransform(true);
            transformArrayData = (double[])swTransform.ArrayData;
            Debug.Print("    Transform:");
            Debug.Print("      Rotate     = (" + transformArrayData[0].ToString("###0.0#####") + ", " + transformArrayData[1].ToString("###0.0#####") + ", " + transformArrayData[2].ToString("###0.0#####") + ")");
            Debug.Print("                 = (" + transformArrayData[3].ToString("###0.0#####") + " " + transformArrayData[4].ToString("###0.0#####") + " " + transformArrayData[5].ToString("###0.0#####") + ")");
            Debug.Print("                 = (" + transformArrayData[6].ToString("###0.0#####") + " " + transformArrayData[7].ToString("###0.0#####") + " " + transformArrayData[8].ToString("###0.0#####") + ")");
            Debug.Print("      Translate  = (" + transformArrayData[9].ToString("###0.0#####") + " " + transformArrayData[10].ToString("###0.0#####") + " " + transformArrayData[11].ToString("###0.0#####") + ")");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
