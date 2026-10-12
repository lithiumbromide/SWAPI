---
title: "Save Roll Backed Part as Parasolid File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm"
---

# Save Roll Backed Part as Parasolid File Example (VBA)

## Save Rolled Backed Part as Parasolid File Example (VBA)

This example shows how to save a part in a rolled backed state as a Parasolid file.

NOTE: When a part is in a rolled back state, you cannot export the part to any other format until the model has been rolled forward. This example shows how to use various geometry-related and topology-related method to create a temporary part that you can then export to any other format, in this example, Parasolid.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldprt.
' 2. Drag the rollback bar to just below Boss-Extrude1.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Saves the Parasolid file to the same folder as the part,
'    overwriting any existing file of the same name; the
'    Parasolid file has same geometry as the part in the rolled back
'    state.
' 2. Examine the Immediate window.
' 3. Open public_documents\samples\tutorial\api\box.x_t.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swNewPart As SldWorks.PartDoc
    Dim swNewModel As SldWorks.ModelDoc2
    Dim sNewModelName As String
    Dim vBodyArr As Variant
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim swCopyBody As SldWorks.Body2
    Dim swFeat As SldWorks.Feature
    Dim sPathName As String
    Dim nOldVal As Long
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim nRetval As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swNewPart = swApp.NewPart
    Set swNewModel = swNewPart
```

```
    sNewModelName = swNewModel.GetTitle
```

```
    Debug.Print "Parasolid settings:"
```

```
    ' Current Parasolid settings
    Debug.Print "  Current:"
    Debug.Print "    swUserPreferenceIntegerValue_e.ParasolidOutputVersion (0 = swParasolidOutputVersion_e.swParasolidOutputVersion_latest) = " + Str(swApp.GetUserPreferenceIntegerValue(swParasolidOutputVersion))
    Debug.Print "    swUserPreferenceStringValue_e.SaveAsCoordinateSystem (empty string signifies that the default coordinate system that does not require a transform) = " + swModel.GetUserPreferenceStringValue(swFileSaveAsCoordinateSystem)
```

```
    ' Strip off SOLIDWORKS Design file extension (sldxxx)
    ' and add Parasolid extension (x_b)
    sPathName = swModel.GetPathName
    sPathName = Left(sPathName, Len(sPathName) - 6)
    sPathName = sPathName + "x_t"
```

```
    ' Store existing Parasolid export version and change to v10.0
    nOldVal = swApp.GetUserPreferenceIntegerValue(swParasolidOutputVersion)
    bRet = swApp.SetUserPreferenceIntegerValue(swParasolidOutputVersion, swParasolidOutputVersion_100)
    Debug.Print "  Modified: "
    Debug.Print "    swUserPreferenceIntegerValue_e.ParasolidOutputVersion (4 = swParasolidOutputVersion_e.swParasolidOutputVersion_100) = " + Str(swApp.GetUserPreferenceIntegerValue(swParasolidOutputVersion))
```

```
    ' Create temporary part with bodies from existing part
    For i = 0 To 5
        vBodyArr = swPart.GetBodies2(i, False)
        If Not IsEmpty(vBodyArr) Then
            For Each vBody In vBodyArr
                Set swBody = vBody
                Set swCopyBody = swBody.Copy
                Set swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyCheck + swCreateFeatureBodySimplify)
            Next vBody
        End If
    Next i
```

```
    ' Export temporary part to Parasolid
    bRet = swNewModel.SaveAs4(sPathName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, nErrors, nWarnings)
```

```
    If bRet = False Then
        nRetval = swApp.SendMsgToUser2("Problems saving file.", swMbWarning, swMbOk)
    End If
```

```
    ' Get rid of temporary file
    swApp.QuitDoc sNewModelName
```

```
    ' Restore old Parasolid export version
    bRet = swApp.SetUserPreferenceIntegerValue(swParasolidOutputVersion, nOldVal)
    Debug.Print "  Restored:"
    Debug.Print "    swUserPreferenceIntegerValue_e.ParasolidOutputVersion (0 = swParasolidOutputVersion_e.swParasolidOutputVersion_latest) = " + Str(swApp.GetUserPreferenceIntegerValue(swParasolidOutputVersion))
```

```
End Sub
```
