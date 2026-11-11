---
title: "Get Names of Available Printers Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Names_of_Available_Printers_Example_CSharp.htm"
---

# Get Names of Available Printers Example (C#)

This example shows how to get the names of the printers available to your computer to which you can print.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this project into the C# IDE.
// 3. Add a reference:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
// 4. Open the Immediate window.
// 5. Start DraftSight.
// 6. Run the macro.
//
// Postconditions: The names of available printers are written
// to the Immediate window.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

static class Module1
{

    public static void Main()
	{
	   DraftSight.Interop.dsAutomation.Application dsApp;

	   //Connect to DraftSight
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

           //Abort any command currently running in DraftSight
           //to avoid nested commands
           dsApp.AbortRunningCommand();

           //Get list of available printers
           PrintManager dsPrintMgr = default(PrintManager);
           dsPrintMgr = (PrintManager)dsApp.GetPrintManager();
           string[] printerArray = dsPrintMgr.GetAvailablePrinters();
           if(null != printerArray)
           {
              Debug.Print ("Available printers:");
              for (int i = 0; i < printerArray.Length; ++i)
              {
                    Debug.Print("  " + printerArray[i]);
              }
          }
       }

}
```
