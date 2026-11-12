---
title: "Get Process ID of SOLIDWORKS Design Session Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Process_ID_of_SOLIDWORKS_Session_Example_CSharp.htm"
---

# Get Process ID of SOLIDWORKS Design Session Example (C#)

This example shows how to get and verify the process ID of the current SOLIDWORKS Design session.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that only one SOLIDWORKS Design session is running.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the process ID of the SOLIDWORKS Design session.
// 2. Examine the Immediate window.
// 3. To verify the process ID, open a Command Prompt window,
//    type TASKLIST, and locate sldworks.exe in the Image Name
//    column and its process ID in the corresponding PID column.
// 4. Exit the Command Prompt window.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetProcessIDCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

            // Print the current SOLIDWORKS Design session's PID to the
            // Immediate window
            Debug.Print("SOLIDWORKS Design process ID: " + swApp.GetProcessID());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
