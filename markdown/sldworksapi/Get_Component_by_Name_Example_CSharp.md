---
title: "Get Component by Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_by_Name_Example_CSharp.htm"
---

# Get Component by Name Example (C#)

This examples shows how to get a component by name and to determine if that component is fixed or floating.

```
//-------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\EDraw\claw\claw-mechanism.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the specified component.
// 2. Gets whether the specified component is fixed.
// 3. Examine the Immediate window.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        AssemblyDoc swAssy;
        Component2 swComp;
        public void Main()
        {
            swModel = swApp.ActiveDoc as ModelDoc2;
            swAssy = swModel as AssemblyDoc;
            string compName;
            compName = "center-1";
            swComp = swAssy.GetComponentByName(compName);
            bool bRet;
            bRet = swComp.IsFixed();
            Debug.Print("Is component fixed: " + bRet);
        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
