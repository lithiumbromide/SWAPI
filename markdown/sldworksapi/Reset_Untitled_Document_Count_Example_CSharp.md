---
title: "Reset Untitled Document Count Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reset_Untitled_Document_Count_Example_CSharp.htm"
---

# Reset Untitled Document Count Example (C#)

For new untitled documents, SOLIDWORKS Design increments the untitled document count and generates a document name by appending the count to the document type. By default, Part1 is for the first untitled document in a SOLIDWORKS Design session, Part2 for the next untitled document in that same SOLIDWORKS Design session, etc.). The untitled document count is automatically reset between SOLIDWORKS Design sessions.

You can use ISldWorks::ResetUntitledCount to reset the untitled document count within a single SOLIDWORKS Design session.

The following code example demonstrates how to use ISldWorks::ResetUntitledCount to reset the untitled document count. The code resets the untitled document count at the beginning of the SOLIDWORKS Design session, creates two untitled documents, maximizes one document, and minimizes the second document.

**NOTE:** Programs designed to run multiple times in the same SOLIDWORKS Design session should either assign titles to new documents or reset the untitled document count at the beginning of the SOLIDWORKS Design session. This ensures that SOLIDWORKS Design creates predictable names for untitled documents, resulting in predictable outcomes for each invocation of the program.

```
//--------------------------------------------------------------
// Preconditions: Verify that the specified document template
// exists.
//
// Postconditions:
// 1. Creates two new untitled part documents, Part9 and Part10;
//    maximizes Part9 and minimizes Part10.
// 2. Minimize Part9 and maximize Part10.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 Part = null;
            ModelDoc2 Part2 = null;
            bool silent = false;
            int longstatus = 0;
            int longwarnings = 0;
```

```
            // Reset the counts for untitled documents
            // (parts, assemblies, and drawings) to 8
            swApp.ResetUntitledCount(8, 8, 8);
```

```
            // When a new untitled document is created,
            // SOLIDWORKS Design increments the untitled document
            // count to 9
            // The next untitled document gets a name with
            // count = 9 ("Part9")
            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part9", silent, ref longwarnings);
            ModelView myModelView = null;
            myModelView = (ModelView)Part.ActiveView;
```

```
            // Maximize Part9
            myModelView.FrameState = (int)swWindowState_e.swWindowMaximized;
```

```
            // When a new untitled document is created,
            // SOLIDWORKS Design increments the untitled document
            // count to 10
            // The next untitled document gets a name with
            // count = 10 ("Part10")
            Part2 = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part10", silent, ref longstatus);
            ModelView myModelView2 = null;
            myModelView2 = (ModelView)Part2.ActiveView;
```

```
            // Minimize Part10
            myModelView2.FrameState = (int)swWindowState_e.swWindowMinimized;

        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
