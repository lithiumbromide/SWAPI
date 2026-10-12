---
title: "Open And Save Document to 3DEXPERIENCE Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_And_Save_3DEXPERIENCE_Document_Example_CSharp.htm"
---

# Open And Save Document to 3DEXPERIENCE Example (C#)

This example shows how to open and save a **3D**EXPERIENCE document with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

```vb
  //---------------------------------------------------------------
 // Preconditions:
 // 1. Open SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
 // 2. Open a new part.
 // 3. Open the Immediate window.
 // 4. Run the macro to the Break.
 // 5. Close the document in the user interface.
 // 6. Press F5 to re-load the document from
 //    your collaborative space in 3DEXPERIENCE.
 //
 // Postconditions:
 // 1.  NonActiveSave.sldprt is saved to a collaborative space
 //    on the 3DEXPERIENCE platform and re-opened.
 // 2. Use 3DEXPERIENCE 3DSearch to find NonActiveSave.sldprt
```

// in your collaborative space.

```
// NOTE: Before running this example again, change strFileName to a
//       unique file name or delete NonActiveSave.sldprt.
//-------------------------------------------------------------------
```

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace OpenAndSave_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            public  void Main()
           {
                ModelDoc2 swModel;
                ModelDocExtension swModExt;
                 SaveTo3DExperienceOptions swSaveTo3DExp;
                PLMObjectSpecification swPLMObjectSpecification;
                DocumentSpecification swDocSpecification;
                string strPLMid;
                string strFileName, strComment;
                bool bStat;
                int lError = 0;
                int IWarning = 0;

              swModel = (ModelDoc2)swApp.ActiveDoc;
              swModExt = swModel.Extension;

               if (swApp.ApplicationType == (int)   swApplicationType_e.swApplicationType_3DEXPERIENCE)
              {
                  swSaveTo3DExp = (SaveTo3DExperienceOptions)swApp.GetSaveTo3DExperienceOptions();

                  strFileName =   "NonActiveSave.sldprt";
                  strComment =   "No comment";
                  swSaveTo3DExp.FileName = strFileName;
                  bStat = swSaveTo3DExp.SetRevisionComments(strComment);

                  bStat = swModExt.SaveTo3DExperience(swSaveTo3DExp,  ref lError,  ref IWarning);

                  strPLMid = swModExt.GetPLMID();
                   Debug.Print(swModel.GetPathName() +   " " + strPLMid);

                  System.Diagnostics.Debugger.Break();   // Close the document in the user interface

                   // Re-open the document from 3DEXPERIENCE
                  swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("");
                  swDocSpecification.DocumentType = (int)   swDocumentTypes_e.swDocPART;
                  swPLMObjectSpecification = (PLMObjectSpecification)swDocSpecification.PLMObjectSpecification;
                  swPLMObjectSpecification.PLMID = strPLMid;

                  swModel = swApp.OpenDoc7(swDocSpecification);

              }
 }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```
