---
title: "Open And Save Document to 3DEXPERIENCE Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_And_Save_3DEXPERIENCE_Document_Example_VBNET.htm"
---

# Open And Save Document to 3DEXPERIENCE Example (VB.NET)

This example shows how to open and save a **3D**EXPERIENCE document with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

```vb
  '----------------------------------------------------------------
 ' Preconditions:
 ' 1. Open SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
 ' 2. Open a new part.
 ' 3. Open the Immediate window.
 ' 4. Run the macro to the Stop.
 ' 5. Close the document in the user interface.
 ' 6. Press F5 to re-load the document from your
 '    collaborative space In 3DEXPERIENCE.
 '
 ' Postconditions:
 ' 1.  NonActiveSave.sldprt is saved to a collaborative space
 '    on the 3DEXPERIENCE platform and re-opened.
 ' 2. Use 3DEXPERIENCE 3DSearch to find NonActiveSave.sldprt
 '    in your collaborative space.
```

```
'
' NOTE: Before running this example again, change strFileName to
'       a unique file name or delete NonActiveSave.sldprt.
'---------------------------------------------------------------
```

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst

 Partial   Class   SolidWorksMacro

       Dim swModel  As  ModelDoc2
       Dim swModExt  As  ModelDocExtension
       Dim swSaveTo3DExp  As   SaveTo3DExperienceOptions
       Dim swPLMObjectSpecification  As   PLMObjectSpecification
       Dim swDocSpecification  As   DocumentSpecification
       Dim strPartTitle  As   String
       Dim strPLMid  As  String
       Dim strFileName, strComment  As   String
       Dim bStat  As  Boolean
       Dim lError  As   Integer
       Dim IWarning  As   Integer

       Sub main()

           swModel = swApp.ActiveDoc
           swModExt = swModel.Extension

            If swApp.ApplicationType =   swApplicationType_e.swApplicationType_3DEXPERIENCE   Then

              swSaveTo3DExp = swApp.GetSaveTo3DExperienceOptions

              strFileName =   "NonActiveSave.sldprt"
              strComment =   "No comment"
              swSaveTo3DExp.FileName = strFileName
              bStat = swSaveTo3DExp.SetRevisionComments(strComment)

              bStat = swModExt.SaveTo3DExperience(swSaveTo3DExp, lError, IWarning)

              strPLMid = swModExt.GetPLMID
               Debug.Print(swModel.GetPathName()   " " & strPLMid)

               Stop  'Close the document in the user interface

               'Re-open the document from 3DEXPERIENCE
              swDocSpecification = swApp.GetOpenDocSpec("")
              swDocSpecification.DocumentType =   swDocumentTypes_e.swDocPART
              swPLMObjectSpecification = swDocSpecification.PLMObjectSpecification
              swPLMObjectSpecification.PLMID = strPLMid

              swModel = swApp.OpenDoc7(swDocSpecification)

            End  If

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
