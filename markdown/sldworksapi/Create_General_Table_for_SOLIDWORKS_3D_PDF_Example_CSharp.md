---
title: "Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_CSharp.htm"
---

# Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (C#)

This example shows how to create a general table annotation for SOLIDWORKS MBD 3D PDF.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open a model document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a general table annotation for SOLIDWORKS MBD 3D PDF.
// 2. Examine the Immediate window.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetGeneralTableAnno_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        TableAnnotation swTable;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;
            swTable = swModelDocExt.GetGeneralTableAnnotation(true, 0, 0, (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "", 2, 2);
            if (swTable == null)
            {
                Debug.Print("Failed to create general table annotation!");
                return;
            }
            else
            {
                Debug.Print("Succeeded in creating general table annotation!");
            }
            Debug.Print(" Total number of rows: " + swTable.TotalRowCount);
            Debug.Print(" Total number of columns: " + swTable.TotalColumnCount);

        }

        public SldWorks swApp;

    }
}
```
