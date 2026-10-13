---
title: "Set User-defined Route Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Set_User-defined_Route_Example_CSharp.htm"
---

# Set User-defined Route Example (C#)

This example shows how to:

- set the type of route of the active component to user defined.
- get and set the name and cross-section type of the user-defined route of an active component.

```
//-----------------------------------------------------------------------------
// Preconditions:
// 1. Add SOLIDWORKS Routing as an add-in
//   (in SOLIDWORKS click Tools > Add-Ins > SOLIDWORKS Routing).
// 2. Add SOLIDWORKS.interop.SwRoutingLib.dll as a reference
//   (in the IDE right-click the project,
//    click Add Reference, and browse to install_dir\api\redist).
// 3. In Tools > Options > System Options > Routing > Routing File Locations,
//    add the locations of your SOLIDWORKS Routing files.
// 4. Open an assembly containing a route that has rectangular sections.
// 5. Open an Immediate Window.
//
// Postconditions:
// 1. Sets the active component's route to user defined.
// 2. Gets and sets the active component's user-defined route's
//    name and cross-section type.
// 3. Examine the Immediate window.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using SolidWorks.Interop.SWRoutingLib;

namespace RectDuctEndCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            RoutingComponentManager swRtCompMgr = default(RoutingComponentManager);
            int crossSectionCompType = 0;
            string compUserDefinedRouteName = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swRtCompMgr = (RoutingComponentManager)swModelDocExt.GetRoutingComponentManager();
            if (swRtCompMgr == null)
                return;

            // Set the active component's route type to user defined
           swRtCompMgr.SetComponentRouteTypeToCustomProperty ((int)swComponentRouteType_e.swUserDefinedType);

            // Get and set the name of the user-defined route
            Debug.Print("Name of user-defined route for the active component: ";
            compUserDefinedRouteName = swRtCompMgr.GetComponentUserDefinedRouteTypeName();
            Debug.Print("  Current: " + crossSectionCompType);
            compUserDefinedRouteName = "HVAC";
            swRtCompMgr.SetComponentUserDefinedRouteTypeName(compUserDefinedRouteName);
            Debug.Print("  Modified: " + compUserDefinedRouteName);

            Debug.Print("");

            // Get and set the cross-section type for the user-defined route
            Debug.Print("Type of cross section for the user-defined route for the active component: ";
            crossSectionCompType = swRtCompMgr.GetComponentCrossSectionType();
            Debug.Print("  Current: " + crossSectionCompType);
            crossSectionCompType = (int)swComponentCrossSectionType_e.swRectangularCrossSection;
            swRtCompMgr.SetComponentCrossSectionType(crossSectionCompType);
            Debug.Print("  Modified: " + crossSectionCompType);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
