---
title: "SOLIDWORKS Design Connected to the 3DEXPERIENCE Platform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SOLIDWORKS_Connected.htm"
---

# SOLIDWORKS Design Connected to the 3DEXPERIENCE Platform

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS Design can run on the **3D**EXPERIENCE platform as SOLIDWORKS Design connected to the 3DEXPERIENCE platform. SOLIDWORKS Design connected to the 3DEXPERIENCE platform provides access to all the **3D**EXPERIENCE services and apps that you are entitled to use based on your role. Before using the SOLIDWORKS APIs with SOLIDWORKS Design connected to the 3DEXPERIENCE platform, you must install and set up roles and collaborative spaces in the **3D**EXPERIENCE platform and install SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

Read **SOLIDWORKS Design connected to the 3DEXPERIENCE platform Help > Installation**.

#### Using SOLIDWORKS APIs with SOLIDWORKS Design connected to the 3DEXPERIENCE platform

As with SOLIDWORKS Design Desktop, you can use the Macro toolbar in SOLIDWORKS Design connected to the 3DEXPERIENCE platform to create and edit macros. Macros are saved in the local directories that you specify. You can make references to type libraries and interop assemblies in the local SOLIDWORKS Design installation that SOLIDWORKS Design connected to the 3DEXPERIENCE platform deploys. You can also presume that most of your working SOLIDWORKS Design macros will also work with SOLIDWORKS Design connected to the 3DEXPERIENCE platform. However due **3D**EXPERIENCE file storage, some SOLIDWORKS APIs have been added, changed, or discontinued for use with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

Note the following:

- SOLIDWORKS Design connected to the 3DEXPERIENCE platform opens **3D**EXPERIENCE documents with limited options. See the [ISldWorks::OpenDoc7](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDocumentSpecification.html) Remarks.

  - Open a part in one of two modes: Resolved or Quick View.
  - Open an assembly in one of three modes: Large Design Review, LightWeight, or Resolved. You can also opt to use Speedpak and load hidden components.
  - Open a drawing in one of four modes: Quick View, Detailing, LightWeight, or Resolved. You can also opt to use Speedpak.
  - See IDocumentSpecification::Selective, IDocumentSpecification::LightWeight, IDocumentSpecification::UseLightWeightDefault, IDocumentSpecification::ViewOnly, IDocumentSpecification::DetailingMode, IDocumentSpecification::UseSpeedPak, and IDocumentSpecification::IgnoreHiddenComponents.
- Documents opened with SOLIDWORKS Design connected to the 3DEXPERIENCE platform can be saved only to a **3D**EXPERIENCE collaborative space that you previously set up. Documents cannot be saved locally and, once saved to the **3D**EXPERIENCE platform with SOLIDWORKS Design connected to the 3DEXPERIENCE platform, cannot be retrieved from outside of the **3D**EXPERIENCE platform.
- Documents that have been saved with either SOLIDWORKS Design Desktop or SOLIDWORKS Design connected to the 3DEXPERIENCE platform can be opened with SOLIDWORKS Design connected to the 3DEXPERIENCE platform. However, documents saved with SOLIDWORKS Design connected to the 3DEXPERIENCE platform can only be opened from within the **3D**EXPERIENCE platform or with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
- SOLIDWORKS Design connected to the 3DEXPERIENCE platform employs the Product Lifecycle Management (PLM) software provided by **3D**EXPERIENCE. Therefore, the SOLIDWORKS PDM Pro API does not work with SOLDWORKS Design connected to the 3DEXPERIENCE platform.

APIs that support opening and saving documents with SOLIDWORKS Design connected to the 3DEXPERIENCE platform are available as of SOLIDWORKS Design 2020 SP03.1. In future releases, more APIs specific to SOLIDWORKS Design connected to the 3DEXPERIENCE platform functionality may be added. You should always read the API Help Release Notes in each service pack to learn about API changes for SOLIDWORKS Design connected to the 3DEXPERIENCE platform functionality. Use the Index and Search tabs in the SOLIDWORKS API Help to search for "3DEXPERIENCE" or "SOLIDWORKS Design connected to the 3DEXPERIENCE platform".

After you install SOLIDWORKS Design connected to the 3DEXPERIENCE platform, run the following two examples in order:

#### Example 1: Save a SOLIDWORKS Design connected to the 3DEXPERIENCE platform document

' VBA

' Preconditions: Open a new part with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

' Postconditions:

' 1. **NonActiveSave.sldprt** is saved to a collaborative space on the **3D**EXPERIENCE platform.

' 2. Use **3D**EXPERIENCE **3D**Search to find **NonActiveSave.sldprt** on the **3D**EXPERIENCE platform.

' 3. Do not close the document as Example 2 requires that it be open.

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModExt As SldWorks.ModelDocExtension
Dim swSaveTo3DExp As SldWorks.SaveTo3DExperienceOptions
Dim strFileName, strComment As String
Dim bStat As Boolean
Dim lError As Long
Dim IWarning As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
Set swModExt = swModel.**Extension**

If swApp.**ApplicationType** = swApplicationType_3DEXPERIENCE Then

Set swSaveTo3DExp = swApp.**GetSaveTo3DExperienceOptions**

strFileName = "NonActiveSave.sldprt"
strComment = "No comment"
swSaveTo3DExp.**FileName** = strFileName
bStat = swSaveTo3DExp.**SetRevisionComments**(strComment)

bStat = swModExt.**SaveTo3DExperience**(swSaveTo3DExp, lError, IWarning)

End If

End Sub

#### Example 2: Open a SOLIDWORKS Design connected to the 3DEXPERIENCE platform document

' VBA

' Preconditions:
' 1. **NonActiveSave.sldprt** is open in SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
' 2. Open the Immediate window.
' 3. Run the macro.
' 4. When the macro stops, close the document.
' 5. Press F5 to reopen the **3D**EXPERIENCE document.

' Postconditions: **NonActiveSave.sldprt** is re-opened from the **3D**EXPERIENCE platform.

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModExt As SldWorks.ModelDocExtension
Dim swPart As SldWorks.PartDoc
Dim swPLMObjectSpecification As SldWorks.PLMObjectSpecification
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim strPartTitle As String
Dim strPLMid As String

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
Set swModExt = swModel.**Extension**

If swApp.**ApplicationType** = swApplicationType_3DEXPERIENCE Then

strPLMid = swModExt.**GetPLMID**
Debug.Print swModel.**GetPathName** & " " & strPLMid

Stop 'Close document in the user interface

'Open **3D**EXPERIENCE document using the API

Set swDocSpecification = swApp.**GetOpenDocSpec**("")
Set swPLMObjectSpecification = swDocSpecification.**PLMObjectSpecification**
swPLMObjectSpecification.**PLMID** = strPLMid

Set swModel = swApp.**OpenDoc7**(swDocSpecification)

End If

End Sub

Also see the [IPLMObjectSpecification](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPLMObjectSpecification.html) .NET examples.
