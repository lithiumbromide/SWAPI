---
title: "Add Equation and Evaluate All Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equation_And_Evaluate_All_Example_CSharp.htm"
---

# Add Equation and Evaluate All Example (C#)

This example shows how to use EquationMgr interfaces to add an equation to a model and

delay evaluation until all equations have been added.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Open any model document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Rebuild the model.
// 2. Observe the 26 (A-Z) new equations in the Equations folder in the
//    FeatureManager design tree.
// 3. Observe the near-zero evaluation time for each equation in the
//    Immediate Window, demonstrating that the evaluations were delayed.
//------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace AddEquationAndEvaluateAll_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            EquationMgr MyEqu = default(EquationMgr);
            int Index = 0;
            long lValue = 0;
            long evalStatus = 0;

                System.DateTime t1 = default(System.DateTime);
                System.DateTime t2 = default(System.DateTime);

            long i = 0;
            i = 0;
            MyEqu = swModel.GetEquationMgr();
            if (MyEqu.GetCount() > 0)
            {
                while ((i < 26))
                {
                    MyEqu.Delete(0);
                    i = i + 1;
                }
            }
            Debug.Print("Delaying evaluation of equations until the end...");
            for (Index = System.Convert.ToInt32('A'); Index <= System.Convert.ToInt32('Z'); Index++)
            {
                t1 = DateTime.Now;
                //Delay solving each equation until after all equations are added
                 //(set solve parameter to false)
                 //FeatureManager design tree not updated
                lValue = MyEqu.Add2(Index, "\"" + System.Convert.ToChar(Index) + "\"=" + Index, false);

                t2 = DateTime.Now;
                Debug.Print("Time of evaluation for character " + System.Convert.ToChar(Index) + ": ");
                TimeSpan t3 = t2 - t1;
                Debug.Print(t3.ToString());
            }
            Debug.Print("Number of equations added to EquationMgr is " + MyEqu.GetCount());
            //Solve all equations after they have been added
             //FeatureManager design tree updated
            Debug.Print("Evaluating all equations...");
            evalStatus = MyEqu.EvaluateAll();
            Debug.Print("Finished Add2 and EvaluateAll");
            MyEqu = null;
            swModel = null;
            //swApp.CloseAllDocuments True
            swApp = null;
        }
        public SldWorks swApp;
    }
}
```
