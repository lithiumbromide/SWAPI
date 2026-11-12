---
title: "Get Paths of Open Documents (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_of_Open_Documents_Example_CSharp.htm"
---

# Get Paths of Open Documents (C#)

This example shows how to get an array of the open documents, and their paths and filenames, in the current SOLIDWORKS Design session.

```vb
 //---------------------------------------------------------------------------
// Preconditions: At least one model document is
//                open in SOLIDWORKS Design.
//
// Postconditions: None.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
namespace GetOpenDocPaths_CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        object[] models;
        int count;
        int index;
        string pathName;
        public void Main()
        {
            count = swApp.GetDocumentCount();
            Debug.Print("Number of open documents in this SOLIDWORKS Design session: " + count);
            models = (object[])swApp.GetDocuments();
            for (index = 0; index < count; index++)
            {
                swModel = models[index] as ModelDoc2;
                pathName = swModel.GetPathName();
                Debug.Print("Path and name of open document: " + pathName);
            }
        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
