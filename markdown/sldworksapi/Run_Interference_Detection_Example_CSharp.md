---
title: "Run Interference Detection Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_Interference_Detection_Example_CSharp.htm"
---

# Run Interference Detection Example (C#)

This example shows how to run interference detection and observe the interferences in an assembly.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\advdrawings\bowl and chute.sldasm.
// 2. Ensure c:\temp exists.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the Interference Detection pane.
 // 2. Gets interferences.
 // 3. Gets interfering components and transforms.
 // 4. Gets interference information.
 // 5. In the Results list on the Interference Detection pane,
 //    click on each interference and observe it in the graphics area (red).
 // 6. To close the Interference Detection pane, right-click the graphics area
 //    and select Cancel.
 // 7. Inspect the Immediate window and c:\temp\IntDetReport.xlsx.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace Interference_CSharp.csproj
 {
```

```vb
partial class  SolidWorksMacro
 {
```

```vb
public void Main()
 {
```

```vb
 ModelDoc2 swModelDoc =  default(ModelDoc2);
  AssemblyDoc swAssemblyDoc =  default(AssemblyDoc);
  InterferenceDetectionMgr pIntMgr =  default(InterferenceDetectionMgr);
 object[] vInts = null;
 long i = 0;
 long j = 0;
  IInterference interference =  default(IInterference);
 object vIntComps = null;
 object[] vComps = null;
  Component2 comp =  default(Component2);
 double vol = 0;
 object vTrans = null;
 bool ret = false;
```

```vb
 swModelDoc = (
```

ModelDoc2)swApp.**ActiveDoc**;
swAssemblyDoc = (AssemblyDoc

)swModelDoc;

//Open the Interference Detection pane
swAssemblyDoc.**ToolsCheckInterference**()**;**
pIntMgr = swAssemblyDoc.**InterferenceDetectionManager**;

//Specify the interference detection settings and options
pIntMgr.**TreatCoincidenceAsInterference** = false;
pIntMgr.**TreatSubAssembliesAsComponents** = false;
pIntMgr.**IncludeMultibodyPartInterferences** = true;
pIntMgr.**MakeInterferingPartsTransparent** = true;
pIntMgr.**CreateFastenersFolder** = false;
pIntMgr.**IgnoreHiddenBodies** = false;
pIntMgr.**ShowIgnoredInterferences** = false;
pIntMgr.**UseTransform** = false;

```vb
 //Specify how to display non-interfering components
 pIntMgr.NonInterferingComponentDisplay = (int)swNonInterferingComponentDisplay_e.swNonInterferingComponentDisplay_Wireframe;

 //Run interference detection
 vInts = (object[])pIntMgr.GetInterferences();
 Debug.Print("Number of interferences: " + pIntMgr.GetInterferenceCount());

 //Get interfering components and transforms
 ret = pIntMgr.GetComponentsAndTransforms(out vIntComps, out vTrans);

 //Get interference information
 for (i = 0; i <= vInts.GetUpperBound(0); i++)
 {
```

```vb
 Debug.Print("Interference " + (i + 1));
 interference = (IInterference)vInts[i];
  Debug.Print("  Number of components in this interference: " + interference.GetComponentCount());
 vComps = (object[])interference.Components;
 for (j = 0; j <= vComps.GetUpperBound(0); j++)
 {
```

```vb
comp = (Component2)vComps[j];
  Debug.Print("   " + comp.Name2);
```

```vb
}
 vol = interference.Volume;
  Debug.Print("  Interference volume is " + (vol * 1000000000) + " mm^3");
```

```vb
}
ret = pIntMgr.ExportResults("c:\\temp\\IntDetReport.xlsx", true);

 //Stop interference detection and close Inteference Detection pane
 //pIntMgr.Done();
```

```vb
    }

     public  SldWorks swApp;
 }
```

```vb
}
```
