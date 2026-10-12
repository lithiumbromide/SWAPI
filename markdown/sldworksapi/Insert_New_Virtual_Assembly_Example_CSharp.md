---
title: "Insert New Virtual Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_CSharp.htm"
---

# Insert New Virtual Assembly Example (C#)

This example shows how to insert an assembly as a virtual component into the main assembly or selected sub-assembly.

```vb
//-------------------------------------------------------------------------
// Preconditions: Open an assembly document.
//
// Postconditions: A new virtual component displays in the
// FeatureManager design tree.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace InsertNewVirtualAssembly_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swDoc;
        AssemblyDoc swADoc;
        Component2 swComp;
        long status;
        public void Main()
        {
            swDoc = (ModelDoc2)swApp.ActiveDoc;
            swADoc = (AssemblyDoc)swDoc;
            swComp = null;
            status = swADoc.InsertNewVirtualAssembly(out swComp);
            if ((swComp == null))
            {
                System.Windows.Forms.MessageBox.Show("Virtual component did not get created.");
            }
            else
            {
                Debug.Print("New virtual component: " + swComp.Name2);
                Debug.Print("Is virtual: " + swComp.IsVirtual);
            }
        }
        public SldWorks swApp;
    }
}
```
