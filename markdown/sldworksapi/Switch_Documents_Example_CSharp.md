---
title: "Switch Documents Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Documents_Example_CSharp.htm"
---

# Switch Documents Example (C#)

This example shows how to switch documents by opening documents in their own and client model windows.

```
//----------------------------------------------
// Preconditions:
// 1. Verify that the specified documents to open exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified documents in their own
//    and client model windows.
// 2. Closes all open documents.
// 3. Examine the Immediate window.
//----------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FrameCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModelDoc = default(ModelDoc2);
            Frame swFrame = default(Frame);
            ModelWindow swModelWindow = default(ModelWindow);
            object[] modelWindows = null;
            int errors = 0;
            int warnings = 0;
            int HWnd = 0;
            string fileName = null;
            string strFolder = null;

            //Open the specified documents in their own windows
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\assemblymates\\knee.sldprt";
            swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            //Open client model window containing the active document
            swApp.CreateNewWindow();

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\assemblymates\\bracket.sldprt";
            swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            //Open client model window containing the active document
            swApp.CreateNewWindow();

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\assemblymates\\clamp.sldprt";
            swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            //Open client model window containing the active document
            swApp.CreateNewWindow();

            swFrame = (Frame)swApp.Frame();
            modelWindows = (object[])swFrame.ModelWindows;
            Debug.Print("Open documents in their own windows:");
            foreach (object obj in modelWindows)
            {
                swModelWindow = (ModelWindow)obj;
                //Get the model document in this model window
                swModelDoc = (ModelDoc2)swModelWindow.ModelDoc;
                //Rebuild the document
                swModelDoc.EditRebuild3();
                swModelDoc = null;
                //Show the model window
                Debug.Print("");
                swFrame.ShowModelWindow(swModelWindow);
                //Get and print the model window handle
                HWnd = swModelWindow.HWnd;
                Debug.Print("  Model window handle: " + HWnd);
                //Get and print the model title as it is seen in the model window's title bar
                Debug.Print("  Model title as it seen in the model's window's title bar: " + swModelWindow.Title);
            }

            strFolder = "";
            //Specify true to close all documents, specify false to close
            //only the documents not modified
            swApp.CloseAllDocuments(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
