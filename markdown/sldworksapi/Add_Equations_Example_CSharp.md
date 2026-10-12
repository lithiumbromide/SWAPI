---
title: "Add and Modify Equations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equations_Example_CSharp.htm"
---

# Add and Modify Equations Example (C#)

This example shows how to add equations to multiple configurations of a part created in SOLIDWORKS 2014 or later.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a part created in SOLIDWORKS 2014 or later that has a
 // Boss-Extrude1 feature and multiple configurations.
 //
 // Postconditions:
 // 1. Adds two equations to all configurations.
 // 2. Modifies the equation at index 1.
 // 3. Click Tools > Equations and examine each configuration in the dialog.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace Add3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             EquationMgr swEquationMgr = default(EquationMgr);
             long longEquation = 0;

             Part = (ModelDoc2)swApp.ActiveDoc;

             swEquationMgr = Part.GetEquationMgr();
             if (swEquationMgr == null)
                 ErrorMsg(swApp, "Failed to get the equation manager");

             //Add a global variable assignment at index, 0, to all configurations
             longEquation = swEquationMgr.Add3(0, "\"A\" = 2in", true, (int)swInConfigurationOpts_e.swAllConfiguration, null);
             if (longEquation != 0)
                 ErrorMsg(swApp, "Failed to add a global variable assignment");

             //Add a dimension equation at index, 1, to all configurations
             longEquation = swEquationMgr.Add3(1, "\"D1@Boss-Extrude1\" = 0.05in", true, (int)swInConfigurationOpts_e.swAllConfiguration, null);
             if (longEquation != 1)
                 ErrorMsg(swApp, "Failed to add a dimension equation");

             //Modify dimension equation at index, 1, in all configurations
             longEquation = swEquationMgr.SetEquationAndConfigurationOption(1, "\"D1@Boss-Extrude1\" = 0.07in", (int)swInConfigurationOpts_e.swAllConfiguration, null);
             if (longEquation != 1)
                 ErrorMsg(swApp, "Failed to modify a dimension equation");

         }

         public void ErrorMsg(SldWorks swApp, string Message)
         {
             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");
         }

         public SldWorks swApp;

     }

 }
```
