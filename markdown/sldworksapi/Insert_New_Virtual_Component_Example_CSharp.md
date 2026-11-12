---
title: "Insert New Virtual Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Component_Example_CSharp.htm"
---

# Insert New Virtual Component Example (C#)

This example shows how to insert a new part as a virtual component in an assembly and save it to an external file.

```
//---------------------------------------------------------------------
// Preconditions:
// 1. Add a reference to Microsoft Scripting Runtime (right-click
//    the name of the project in the Project Explorer and click Add Reference >
//    the Browse tab > C:\windows\system32\scrrun.dll > OK.
// 2. Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
// 3. Select a planar face on the assembly.
// 4. Open the Immediate window.
// 5. Step through this macro by pressing F8.
//
// Postconditions:
// 1. Inserts a new part as a virtual component in the assembly.
// 2. Attempts to save the virtual component to an external file,
// 3. Examine the Immediate window and FeatureManager design tree.
//
// NOTE: Because this assembly is used elsewhere,
// do not save changes.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using Scripting;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        AssemblyDoc swAssy;
        Component2 swComponent;
        SelectionMgr swSelMgr;
        FileSystemObject objFSO;
        string compName;
        object[] splits;
        long status;

        public void Main()
        {

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;

            // Get the pre-selected planar face
            Face2 swFeature = default(Face2);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Face2)swSelMgr.GetSelectedObject6(1, 0);

            // Create the part and insert it as a virtual component
            // in the assembly
            status = swAssy.InsertNewVirtualPart(swFeature, out swComponent);

            if (status == 1)
            {

                Debug.Print("Virtual component inserted!");
                Debug.Print("Name of virtual component: " + swComponent.Name2);

                // Check to see if the part is a virtual component
                Debug.Print("Is component virtual? " + swComponent.IsVirtual);

                objFSO = new Scripting.FileSystemObject();

                splits = swComponent.Name2.Split('^');
                compName = objFSO.GetParentFolderName(swModel.GetPathName()) + "\\" + splits[0];

                ModelDoc2 compModel = default(ModelDoc2);
                compModel = (ModelDoc2)swComponent.GetModelDoc();

                if (compModel.GetType() == (int)swDocumentTypes_e.swDocPART)
                {
                    compName = compName + ".sldprt";
                }
                else
                {
                    compName = compName + ".sldasm";
                }

                Debug.Print("Path and name of virtual component: " + compName);

                bool ret;
                ret = swComponent.SaveVirtualComponent(compName);
                if (ret)
                {
                    Debug.Print("    Virtual component saved!");
                }
                else
                {
                    Debug.Print("    Virtual component not saved!");
                    Debug.Print("       Check the folder's attributes where to save the virtual component and check your permissions to this folder.");
                }

            }
            else
            {
                Debug.Print("Error code returned when attempting to insert new part as virtual component: " + status);
            }

            swModel.ClearSelection2(true);
        }

        public SldWorks swApp;

    }
}
```
