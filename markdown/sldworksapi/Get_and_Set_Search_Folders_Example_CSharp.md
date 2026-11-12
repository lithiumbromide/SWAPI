---
title: "Get and Set Search Folders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Search_Folders_Example_CSharp.htm"
---

# Get and Set Search Folders Example (C#)

This example shows how to get and set the file locations in which SOLIDWORKS Design searches for reference documents.

```
//----------------------------------------------------------------------------
// Preconditions: Open the Immediate window.
//
// Postconditions:
// 1. Adds c:\; to the beginning of the search folder path for reference
//    documents.
// 2. Examine the Immediate window.
//
// NOTE: This macro changes your SOLIDWORKS Design search folders system settings.
// ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 Part;
        string searchFolders;

        bool boolstatus;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;

            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swUseFolderSearchRules, false);

            searchFolders = swApp.GetSearchFolders((int)swSearchFolderTypes_e.swDocumentType);
            Debug.Print("Current search path: " + searchFolders);
            searchFolders = "c:\\;" + searchFolders;
            boolstatus = swApp.SetSearchFolders((int)swSearchFolderTypes_e.swDocumentType, searchFolders);
            searchFolders = swApp.GetSearchFolders((int)swSearchFolderTypes_e.swDocumentType);
            Debug.Print("New search path: " + searchFolders);
        }

        public SldWorks swApp;

    }
}
```
