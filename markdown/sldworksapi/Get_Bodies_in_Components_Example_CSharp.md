---
title: "Get Bodies in Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_in_Components_Example_CSharp.htm"
---

# Get Bodies in Components Example (C#)

This example shows how to get the number of normal and user bodies in the components in an assembly.

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document
//    to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets and prints each component's name, number of
//    solid bodies, body names, and body types
//    to the Immediate window.
// 2. Right-click filterholder<1> in the FeatureManager
//    design tree and click the Open Part button.
//    Notice that there are no screw holes in the part.
// 3. Close the part and examine the filterholder<1>
//    component, which is the orange, flat, circular
//    component located on the front of the assembly
//    in the graphics area. There are screw
//    holes in the component.
// 4. Examine the filterholder<1>'s information in the
//    Immediate window. Because the component was
//    modified in the assembly, its body is identified
//    as a user body.
//
// NOTE: Because this assembly document is used by
// elsewhere, do not save changes.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Collections;
namespace GetBodies3Component2CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            object[] vComponents = null;
            Component2 oneComponent = default(Component2);
            Body2 swBody = default(Body2);
            object[] vBodies = null;
            object vBodyInfo;
            int[] BodiesInfo = null;
            int BodyType = 0;
            int errors = 0;
            int warnings = 0;
            int i = 0;
            int j = 0;

            // Open this assembly
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\toolbox\\lens_mount.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssembly = (AssemblyDoc)swModel;

            // Get the components in the assembly
            vComponents = (object[])swAssembly.GetComponents(true);
            for (i = 0; i <= vComponents.Length - 1; i++)
            {
                oneComponent = (Component2)vComponents[i];
                Debug.Print(" ");
                Debug.Print("Component name: " + oneComponent.Name2);

                // Get the solid bodies in the component
                vBodies = (object[])oneComponent.GetBodies3((int)swBodyType_e.swSolidBody, out (object)vBodyInfo);
                BodiesInfo = (int[])vBodyInfo;
                Debug.Print(" Number of solid bodies: " + (vBodies.Length + 1));
                for (j = 0; j <= vBodies.Length - 1; j++)
                {
                    Debug.Print(" Body number: " + (j + 1));
                    swBody = (Body2)vBodies[j];
                    Debug.Print(" Body name: " + swBody.Name);

                    // Print the type of body
                    BodyType = (int)BodiesInfo[j];
                    switch (BodyType)
                    {
                        case 0:
                            Debug.Print(" Body type: user");
                            break;
                        case 1:
                            Debug.Print(" Body type: normal");
                            break;
                    }
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
