---
title: "Get Version Number Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_Number_Example_CSharp.htm"
---

# Get Version Number Example (C#)

This example shows how to get the version number of SOLIDWORKS Design.

```
//----------------------------------
// Preconditions: Open the Immediate
// window.
//
// Postconditions: Examine the Immediate
// window.
//-----------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace VersionCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        string BaseVersion;
        string CurrentVersion;
        string HotFixes;

        public void Main()
        {
            Debug.Print("Version number: " + swApp.RevisionNumber());
            swApp.GetBuildNumbers2(out BaseVersion, out CurrentVersion, out HotFixes);
            Debug.Print("Major revision number: " + BaseVersion);
            Debug.Print("Build number: " + CurrentVersion);
            Debug.Print("Hot fix numbers: " + HotFixes);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
