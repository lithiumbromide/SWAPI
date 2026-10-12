---
title: "Get Whether Part Has Frozen Features (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Part_Has_Frozen_Features_Example_CSharp.htm"
---

# Get Whether Part Has Frozen Features (C#)

## Get Whether Part Has Frozen Features Example (C#)

This example shows how to get whether a part document has frozen features, and, if so, whether those features need updating.

```vb
 //------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Help Getting Started
 //    topic and register the required DLLs.
 // 2. Copy and paste this module into a C#
 //    console application in Microsoft Visual Studio.
 // 3. Load the latest SolidWorks.Interop.swdocumentmgr.dll
 //    interop assembly by:
 //    a. Right-clicking the project name in the Project Explorer.
 //    b. Clicking Add Reference.
 //    c. Clicking the interop assembly in the .NET
 //       tab or browsing for the DLL in install_dir/api/redist.
 // 4. Substitute your license key for your_license_key in the code.
 // 5. Make sure that the part document opened by this application
 //    exists.
 // 6. Open the Immediate window.
 //
 // Postconditions: Whether the part document contains frozen features
 // is printed to the Immediate window, and, if so, whether
 // those features need updating.
 //
 // NOTE: This sample application was developed using
 // Microsoft Visual Studio 2008. If you use another version of
 // Microsoft Visual Studio, you might need to add more references to get
 // this application to compile.
 //------------------------------------------------------------------

 using SolidWorks.Interop.swdocumentmgr;
 using System;
 using System.Diagnostics;

 namespace HasFrozenFeatures
 {
     class Module1
     {
         static void Main()
         {
             SwDMClassFactory dmClassFact = default(SwDMClassFactory);
             ISwDMApplication3 dmDocMgr = default(ISwDMApplication3);
             ISwDMDocument16 dmDoc = default(ISwDMDocument16);
             SwDmDocumentOpenError dmError = default(SwDmDocumentOpenError);
             string namePart = "";
             bool hasFrozenFeatures = false;
             bool frozenFeaturesNeedUpdating = false;

             dmClassFact = new SwDMClassFactory();
             //Do not distribute license key
             dmDocMgr = (ISwDMApplication3)dmClassFact.GetApplication("your_license_key");
             namePart = " C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\api\\FreezeBarNeedsRebuild2.sldprt";

             //Get the SOLIDWORKS part document
             dmDoc = (ISwDMDocument16)dmDocMgr.GetDocument(namePart, SwDmDocumentType.swDmDocumentPart, false, out dmError);
             Debug.Print("Document's full name: " + dmDoc.FullName);
             Debug.Print("  Date document last saved: " + dmDoc.LastSavedDate);

             // Get whether the part document has frozen features and
             // whether those features need updating
             hasFrozenFeatures = (bool)dmDoc.HasFrozenFeatures(out frozenFeaturesNeedUpdating);
             Debug.Print("    Does the part document have frozen features? " + hasFrozenFeatures);
             if (hasFrozenFeatures)
                 Debug.Print("    Do any of the frozen features need updating? " + frozenFeaturesNeedUpdating);
         }
     }
 }
```
