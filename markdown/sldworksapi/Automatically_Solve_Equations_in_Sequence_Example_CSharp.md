---
title: "Automatically Solved Equations in Sequence Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Automatically_Solve_Equations_in_Sequence_Example_CSharp.htm"
---

# Automatically Solved Equations in Sequence Example (C#)

This example shows how to automatically sequence the equations in an order determined to produce accurate results.

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Sets the equation's Automatic solve order option
//    to true, which results in the model's
//    independent equations executing before
//    dependent equations, if any.
// 2. Examine the Immediate window.
//
// NOTE: Because this model is used elsewhere,
// do save changes.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace AutomaticSolveOrderCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            EquationMgr swEquationMgr = default(EquationMgr);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\partEquations.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swEquationMgr = (EquationMgr)swModel.GetEquationMgr();
            //Make sure that this model includes equations
            //by getting the number of equations
            Debug.Print("Number of equations: " + swEquationMgr.GetCount());
            if (swEquationMgr.GetCount() >= 1)
            {
                //Get whether equations are automatically
                //solved in sequence
                Debug.Print("  Are equations automatically solved in sequence? " + swEquationMgr.AutomaticSolveOrder);
                if (swEquationMgr.AutomaticSolveOrder)
                {
                    return;
                }
                else
                {
                    //Automatically solve equations in sequence
                    swEquationMgr.AutomaticSolveOrder = true;
                    Debug.Print("  Are equations automatically solved in sequence? " + swEquationMgr.AutomaticSolveOrder);
                }
            }
            else
            {
                Debug.Print("No equations included with this model.");
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
