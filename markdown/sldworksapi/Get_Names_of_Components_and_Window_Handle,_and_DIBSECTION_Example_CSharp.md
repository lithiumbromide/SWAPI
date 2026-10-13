---
title: "Get Names of Components, Window Handles, and DIBSECTIONs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm"
---

# Get Names of Components, Window Handles, and DIBSECTIONs Example (C#)

This example shows how to get:

- names of the assembly components in an open, inactive, assembly document.
- window handles and pointers to images of model documents.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified model documents to open exist.
//
// Postconditions:
// 1. Opens the specified model documents.
// 2. Prints to the Immediate window:
//    *  paths and file names of:
//       * assembly components of the open, inactive, assembly document
//       * open, active, part document
//       * open, inactive, assembly document
//    *  whether the assembly components, part, and assembly documents
//       are visible
// 3. Prints to the Immediate window each visible document's:
//    * Microsoft window handle
//    * pointer to its image as it looks in Normal view
//      or in the print preview
// 4. Examine the Immediate window.
//
// NOTE: Because the models are used elsewhere, do not save changes.
//-------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetViewHWndCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelView swModView = default(ModelView);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            //Open assembly document, then open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bowl and chute.sldasm";
            swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\switch.sldprt";
            swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //NOTE: Assembly components are open, but they
            //are not visible until opened by the user.

            //Get first open document
            swModel = (ModelDoc2)swApp.GetFirstDocument();

            while ((swModel != null))
            {
                Debug.Print(swModel.GetPathName());
                //Get whether assembly component, part, or assembly is visible
                Debug.Print("    Visible? " + swModel.Visible);
                swModView = (ModelView)swModel.ActiveView;
                while ((swModView != null))
                {

                    //NOTE: Model views exist only for visible model documents.

                    //Get Microsoft window handle and pointer to image
                    //for each visible model document
                    //64-bit SOLIDWORKS
                    Debug.Print("    Microsoft window handle = " + swModView.GetViewHWndx64());
                    Debug.Print("    Pointer to image = " + swModView.GetViewDIBx64());

                    swModView = (ModelView)swModView.GetNext();
                }
                //Get next open document
                swModel = (ModelDoc2)swModel.GetNext();
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
