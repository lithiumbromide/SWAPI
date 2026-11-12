---
title: "Get Hidden Components Filenames Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hidden_Components_Filenames_Example_CSharp.htm"
---

# Get Hidden Components Filenames Example (C#)

This example shows how to get the filenames of the hidden components in an assembly.

```
//-----------------------------------------------------------
// Preconditions:
// 1. In SOLIDWORKS Design , click File > Open, and browse to
//    public_documents\samples\tutorial\routing-pipes.
// 2. Click ball valve with flanges.sldasm > Mode >
//    Large Design Review > Open > OK.
//
//    NOTE: If the path to the Design Library does not exist,
//    then multiple dialogs informing you that SOLIDWORKS Design is unable
//    to locate might be displayed some components. Click No or OK
//    to close these dialogs.
//
// 3. Click ball valve-1 in the FeatureManager design tree
//    and click Selective Open > Selective Open > Selected components >
//    Open Selected > OK.
//
//    NOTE: Only the selected components are loaded. Components
//    not selected are not loaded and not visible in the
//    SOLIDWORKS Design graphics area.
//
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Does not load the slip on weld flange components because
//    they are hidden.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because this assembly elsewhere, do not save changes.
//-----------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

            ModelDoc2 swModel;
            AssemblyDoc swAssembly;
            Boolean boolStatus;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;
            boolStatus = swAssembly.HasUnloadedComponents();
            if (boolStatus == true)
            {
                object oPaths = null;
                object oRefdConfigs = null;
                object oReasons = null;
                object oDocTypes = null;
                object oNames = null;

                oNames = swAssembly.GetUnloadedComponentNames(out oPaths, out oRefdConfigs, out oReasons, out oDocTypes);

                string[] Paths = null;
                string[] RefdConfigs = null;
                int[] Reasons = null;
                int[] DocTypes = null;
                string[] Names = null;

                Paths = (string[])oPaths;
                RefdConfigs = (string[]) oRefdConfigs;
                Reasons = (int[]) oReasons;
                DocTypes =(int[]) oDocTypes;
                Names = (string[]) oNames;

                if (!(Paths is System.Array) & (RefdConfigs is System.Array) & (Reasons is System.Array) & (DocTypes is System.Array) & (Names is System.Array))
                {
                    MessageBox.Show("Error: Non-array parameter!");
                    Debug.Assert(false);
                    return;
                }
                if ((Paths.Length != RefdConfigs.Length) | (Paths.Length != Reasons.Length) | (Paths.Length != DocTypes.Length) | (Paths.Length != Names.Length))
                {
                    MessageBox.Show("Error: Lengths of the arrays do not match!");
                    Debug.Assert(false);
                    return;
                }

                for (int index = 0; index < Paths.Length; index++)
                {
                    string debugMessage = null;
                    debugMessage = index + ": ";
                    swDocumentTypes_e eDocType;
                    eDocType = (swDocumentTypes_e)(DocTypes[index]);
                    switch (eDocType)
                    {
                        case swDocumentTypes_e.swDocNONE:
                            debugMessage = debugMessage + "The document ";
                            break;
                        case swDocumentTypes_e.swDocPART:
                            debugMessage = debugMessage + "The part ";
                            break;
                        case swDocumentTypes_e.swDocASSEMBLY:
                            debugMessage = debugMessage + "The assembly ";
                            break;
                        case swDocumentTypes_e.swDocDRAWING:
                            debugMessage = debugMessage + "The drawing ";
                            break;
                        case swDocumentTypes_e.swDocSDM:
                            debugMessage = debugMessage + "The SDM ";
                            break;
                        default:
                            debugMessage = debugMessage + "The document is an unknown type ";
                            break;
                    }
                    debugMessage = debugMessage + Paths[index] + " was not loaded because it is ";
                    bool bUnloadedBecauseHidden = false;
                    if (Reasons[index] == 1)
                        bUnloadedBecauseHidden = true;
                    else
                        bUnloadedBecauseHidden = false;

                    if (bUnloadedBecauseHidden)
                    {
                        debugMessage = debugMessage + "hidden.";
                    }
                    else
                    {
                        debugMessage = debugMessage + "suppressed.";
                    }
                    Debug.Print(debugMessage);
                }
            }

        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
