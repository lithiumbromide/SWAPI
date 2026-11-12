---
title: "Connect to SOLIDWORKS Session (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/Connect_to_SOLIDWORKS_Session_CSharp.htm"
---

# Connect to SOLIDWORKS Session (C#)

## Connect to SOLIDWORKS Session Example (C#)

This example shows how to connect to a SOLIDWORKS Design session.

```vb
using System;

namespace ConsoleApplication1
{
/// <summary>
/// Summary description for Class1
/// </summary>
class Class1
{
/// <summary>
/// Main entry point for the application
/// </summary>
[STAThread]
static void Main(string[] args)
{
//
// To do: Add code to start application here
//
SldWorks.SldWorks swApp = new SldWorks.SldWorksClass();
SldWorks.ModelDoc2 swDoc = swApp.IActiveDoc2;
swDoc.Extension.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
swDoc.InsertSketch2(false);
swDoc.SketchRectangle(0, 0.04, 0, 0.01, 0, 0, true);
swDoc.FeatureManager.FeatureExtrusion(true, false, false, 0, 0, 0.09, 0, false, false, false, false, 0.0, 0.0, false, false, false, false, true, false, false);
}
}
}
```
