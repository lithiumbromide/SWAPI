---
title: "Open Specified Sheet in Drawing Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Specified_Sheet_in_Drawing_Document_Example_CSharp.htm"
---

# Open Specified Sheet in Drawing Document Example (C#)

This example shows how to open a specific sheet when programmatically opening a drawing document.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified sheet in the specified drawing
//    document as view-only.
// 2. Examine the drawing and Immediate window.
//
// NOTE: Because this drawing document is used
// elsewhere, do not save changes.
//------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
```

```
namespace Macro1.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DocumentSpecification swDocSpecification = default(DocumentSpecification);
            string sName = null;
            long longstatus = 0;
            long longwarnings = 0;
```

```
            // Drawing document path and name
            swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw");
            sName = swDocSpecification.FileName;
```

```
            // Sheet name
            swDocSpecification.SheetName = "Sheet2";
            swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocDRAWING;
            swDocSpecification.ReadOnly = true;
            swDocSpecification.Silent = false;
```

```
            // Open the specified sheet in the specified drawing document
            swModel = swApp.OpenDoc7(swDocSpecification);
            longstatus = swDocSpecification.Error;
            longwarnings = swDocSpecification.Warning;
```

```
            Debug.Print ("Name of active sheet? " + swDocSpecification.SheetName);
            Debug.Print ("Drawing read-only? " + swDocSpecification.ReadOnly);
```

```
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
