---
title: "Get and Set Routing Component Grouping Options for BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_CSharp.htm"
---

# Get and Set Routing Component Grouping Options for BOM Table Example (C#)

This example shows how to get and set the routing component grouping options for this BOM table in a drawing of an assembly containing routing components.

```
//----------------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\AutoRouteThroughSketchEntities.sldddrw.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the Bill of Materials1 feature.
// 2. Examine the Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//---------------------------------------------------------------------------------

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
            SelectionMgr swSelMgr = default(SelectionMgr);
            BomFeature swBomFeature = default(BomFeature);
            bool status = false;
            int options = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Bill of Materials1", "BOMFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swBomFeature = (BomFeature)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Print("Name of configuration used for BOM table: " + swBomFeature.Configuration);

            //Get current routing component grouping options
            Debug.Print("Current routing component grouping options: " + swBomFeature.RoutingComponentGrouping);

            //Set new routing component grouping options
            options = (int)swRoutingComponentGroupingOption_e.swShowOnlyRoutingComponentsInBOM + (int)swRoutingComponentGroupingOption_e.swDisplayUnitsInBOM;
            swBomFeature.RoutingComponentGrouping = options;
            Debug.Print("Modified routing component grouping options: " + swBomFeature.RoutingComponentGrouping);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
