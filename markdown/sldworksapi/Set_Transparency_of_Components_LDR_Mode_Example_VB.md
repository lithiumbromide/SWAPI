---
title: "Set Transparency of Unmodified Components in Large Design Review Assembly Example(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Transparency_of_Components_LDR_Mode_Example_VB.htm"
---

# Set Transparency of Unmodified Components in Large Design Review Assembly Example(VBA)

## Set Transparency of Unmodified Components in Large Design Review Mode Example (VBA)

This example shows how to:

- open an assembly in Large Design Review mode
- open, modify, save, and close an assembly component, and
- set the transparency level of unmodified components in the assembly.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Create c:\temp\LDR.
' 2. Copy these files from public_documents\samples\tutorial\api to c:\temp\LDR:
'    * landing_gear.sldasm
'    * lwrsway_lnk.sldprt
'    * oleopiston.sldprt
'    * oleostrut.sldprt
'    * part4.sldprt
'    * upprsway_lnk.sldprt
'    * wheel_hub.sldprt
'    * wheelassy.sldasm
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Click OK in the Large Design Review dialog.
' 2. Opens the assembly in Large Design Review mode.
' 3. Opens, modifies, saves, and closes the assembly component, oleostrut.sldprt.
'    a. When prompted to rebuild, click Rebuild and save the document.
'    b. If prompted to update the graphics data in Large Design Review,
'       click Yes.
' 4. Sets the transparency level of unmodified components in the assembly to 0.75.
' 5. Close the assembly and part documents.
' 6. Examine the Immediate window and graphics area.
'---------------------------------------------------------------------------

Option Explicit

Sub main()
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swAssemblyDoc As SldWorks.AssemblyDoc
 Dim fileName As String
 Dim status As Boolean
 Dim errors As Long, warnings As Long

 Set swApp = Application.SldWorks

 ' Open assembly in Large Design Review mode
 fileName = "C:\temp\LDR\landing_gear.sldasm"
 Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_ViewOnly, "", errors, warnings)
 Set swModelDocExt = swModel.Extension
 Set swAssemblyDoc = swApp.ActiveDoc

 ' Open component, modify it, and save it
 Dim swCompModel As ModelDoc2
 status = swModelDocExt.SelectByID2("oleostrut-1@landing_gear", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
 swApp.OpenDoc6 "C:\templ\LDR\oleostrut.sldprt", 1, 0, "", errors, warnings
 swApp.ActivateDoc3 "oleostrut.sldprt", False, swRebuildOnActivation_e.swUserDecision, errors
 Set swCompModel = swApp.ActiveDoc
 swCompModel.ClearSelection2 (True)
 status = swModelDocExt.SelectByID2("Sketch9", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
 swCompModel.EditSketch
 swCompModel.ClearSelection2 (True)
 status = swModelDocExt.SelectByID2("D3@Sketch9@oleostrut.SLDPRT", "DIMENSION", 7.92805491990847E-02, -0.020779176201373, 0, False, 0, Nothing, 0)
 Dim swDimension As Object
 Set swDimension = swCompModel.Parameter("D3@Sketch9")
 swDimension.SystemValue = 0.025
 swCompModel.ClearSelection2 (True)
 status = swCompModel.Save3(swSaveAsOptions_e.swSaveAsOptions_SaveReferenced, errors, warnings)
 swApp.CloseDoc ("oleostrut.sldprt")

 ' Set the transparency level of unmodified components in the assembly
 swAssemblyDoc.LargeDesignReviewTransparencyLevelDynamic = True
 swAssemblyDoc.LargeDesignReviewTransparencyLevelEnabled = True
 swAssemblyDoc.LargeDesignReviewTransparencyLevel = 0.75
 Debug.Print ("Transparency level: " & swAssemblyDoc.LargeDesignReviewTransparencyLevel)
 Debug.Print (" Enabled = " & swAssemblyDoc.LargeDesignReviewTransparencyLevelEnabled)
 Debug.Print (" Dynamic = " & swAssemblyDoc.LargeDesignReviewTransparencyLevelDynamic)
```

```vb
End Sub
```
