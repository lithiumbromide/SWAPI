---
title: "Get Component Name From Selected Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_Name_From_Selected_Entity_Example_CSharp.htm"
---

# Get Component Name From Selected Entity Example (C#)

This example shows how to get the name of a component to possibly use with a future call to [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html), when selectively opening the assembly document and specific components using [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html), etc. This example also shows how to get and set a component reference.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Select an entity (face, edge, vertex, or loop) on any
//    component in the graphics area.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Adds a component reference to the component to which the
//    entity belongs.
// 2. Examine the Immediate window.
// 3. Locate the component to which the component reference was added
//    in the FeatureManager design tree. If necessary, use the scrollbar
//    at the bottom of the FeatureManager design tree to see the component
//    reference.
//--------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetSelectByIDStringComponent_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Entity swEntity = default(Entity);
            Component2 swComponent = default(Component2);

            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Get the selected entity (i.e., face, edge, vertex, or loop)
            // and get the name of its component
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swEntity = (Entity)swSelectionMgr.GetSelectedObject6(1, -1);
            swComponent = (Component2)swEntity.GetComponent();

            // Print the name of the component to which the
            // the selected entity belongs
            Debug.Print("Name of component to which the selected entity belongs: " + swComponent.GetSelectByIDString());

            // Set a component reference to this component
            swComponent.ComponentReference = "TestComponentReference";
            Debug.Print("Component reference added to the component to which the selected entity belongs: " + swComponent.ComponentReference);

            // Rebuild the assembly to see the component reference
            // beside the name of the component in the FeatureManager
            // design tree
            swModel.ForceRebuild3(true);
        }
        public SldWorks swApp;
    }
}
```
