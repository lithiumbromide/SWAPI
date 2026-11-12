---
title: "Pack and Go Part and Linked Equation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Pack_and_Go_Part_and_Linked_Equation_Example_CSharp.htm"
---

# Pack and Go Part and Linked Equation Example (C#)

This example shows how to determine if a part document includes any equations and whether those equations are linked files. The example also shows how to add the part document and any linked equations to Pack and Go.

```
//----------------------------------------
// Preconditions:
// 1. Verify that the specified part and equation documents
//    exist.
// 2. Verify that c:\temp exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Adds the part and linked equation documents
//    to Pack and Go and copies the files to
//    c:\temp.
// 3. To verify, examine c:\temp.
//
// NOTE: Because the model is used elsewhere,
// do not save changes.
//-----------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace EquationsPackAndGoCSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            EquationMgr swEqnMgr = default(EquationMgr);
            PackAndGo swPackAndGo = default(PackAndGo);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int i = 0;
            int nCount = 0;
            bool eqnLinked = false;
            object fileNames = null;
            object[] pgFileNames = null;
            bool status = false;
            int[] statuses = null;
            string myPath = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\microphonehousing.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print(" ");

            // Get Equation manager object
            swEqnMgr = (EquationMgr)swModel.GetEquationMgr();

            // List the equations, get whether they're linked
            // to files, make sure any equations are up to date,
            // and get the paths where they're stored
            nCount = swEqnMgr.GetCount();
            for (i = 0; i <= nCount - 1; i++)
            {
                Debug.Print("  Equation #" + i + " = " + swEqnMgr.get_Equation(i));

                eqnLinked = swEqnMgr.LinkToFile;
                Debug.Print("  Equation linked to file? " + eqnLinked);

                if (eqnLinked)
                {
                    //Make sure equations are up to date
                    swEqnMgr.UpdateValuesFromExternalEquationFile();

                    //Get path and name of linked equation file
                    Debug.Print("  Path and filename of linked equation: " + swEqnMgr.FilePath);
                }
            }

            Debug.Print(" ");

            // Get Pack and Go object
            Debug.Print("  Pack and Go");
            swPackAndGo = swModelDocExt.GetPackAndGo();

            // Get current paths and names of the documents
            status = swPackAndGo.GetDocumentNames(out fileNames);
            pgFileNames = (object[])fileNames;
            Debug.Print("    Add these SOLIDWORKS Design files to Pack and Go: ");
            if ((pgFileNames != null))
            {
                for (i = 0; i <= pgFileNames.GetUpperBound(0); i++)
                {
                    Debug.Print("      The file to pack up is: " + pgFileNames[i]);
                }
            }

            // Set document paths and names for Pack and Go
            status = swPackAndGo.SetDocumentSaveToNames(pgFileNames);

            // Override path where to save documents
            myPath = "c:\\temp\\";
            status = swPackAndGo.SetSaveToName(true, myPath);

            // Pack and Go both SOLIDWORKS Design and non-SOLIDWORKS-Design files
            statuses = (int[])swModelDocExt.SavePackAndGo(swPackAndGo);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
