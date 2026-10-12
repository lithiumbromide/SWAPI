---
title: "Open And Save Document to 3DEXPERIENCE Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_And_Save_3DEXPERIENCE_Document_Example_VB.htm"
---

# Open And Save Document to 3DEXPERIENCE Example (VBA)

This example shows how to open and save a **3D**EXPERIENCE document with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

'------------------------------------------------------------------
' Preconditions:
' 1. Open SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
' 2. Open a new part.
' 3. Open the Immediate window.
' 4. Run the macro to the Stop.
' 5. Close the document in the user interface.
' 6. Press F5 to re-load the document from your collaborative space
' in **3D**EXPERIENCE.
'
' Postconditions:
' 1. **NonActiveSave.sldprt** is saved to a collaborative space
' on the 3DEXPERIENCE platform and re-opened.
' 2. Use **3D**EXPERIENCE **3D**Search to find **NonActiveSave.sldprt**
' in your collaborative space.
'
' NOTE: Before running this example again, change strFileName to
' a unique file name or delete **NonActiveSave.sldprt**.
'------------------------------------------------------------------

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModExt As SldWorks.ModelDocExtension
Dim swSaveTo3DExp As SldWorks.SaveTo3DExperienceOptions
Dim swPLMObjectSpecification As SldWorks.PLMObjectSpecification
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim strPartTitle As String
Dim strPLMid As String
Dim strFileName, strComment As String
Dim bStat As Boolean
Dim lError As Long
Dim IWarning As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModExt = swModel.Extension

If swApp.ApplicationType = swApplicationType_3DEXPERIENCE Then

Set swSaveTo3DExp = swApp.**GetSaveTo3DExperienceOptions**

strFileName = "NonActiveSave.sldprt"
strComment = "No comment"
swSaveTo3DExp.**FileName** = strFileName
bStat = swSaveTo3DExp.**SetRevisionComments**(strComment)

bStat = swModExt.**SaveTo3DExperience**(swSaveTo3DExp, lError, IWarning)

strPLMid = swModExt.**GetPLMID**
Debug.Print swModel.**GetPathName** & " " & strPLMid

Stop 'Close the document in the user interface

'Re-open the document from **3D**EXPERIENCE
Set swDocSpecification = swApp.**GetOpenDocSpec**("")
Set swPLMObjectSpecification = swDocSpecification.**PLMObjectSpecification**
swPLMObjectSpecification.**PLMID** = strPLMid

Set swModel = swApp.**OpenDoc7**(swDocSpecification)

End If

End Sub
