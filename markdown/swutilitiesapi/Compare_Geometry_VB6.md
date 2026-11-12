---
title: "Compare Geometry (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swutilitiesapi/Compare_Geometry_VB6.htm"
---

# Compare Geometry (VBA)

## Compare Geometry Example (VBA)

This example shows how to use the SOLIDWORKS Utilities API to compare geometries in two part documents.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that the specified parts exist.
' 4. Verify that C:\test\ exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates the geometry comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets face and volume comparison statuses.
' 3. Examine the Immediate window, graphics area, and
'    and C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'------------------------------------------------------------------------------
```

```vb
Option Explicit
Sub main()
    Dim swapp                   As SldWorks.SldWorks
    Dim swUtil                  As SWUtilities.gtcocswUtilities
    Dim swUtilCompGeom          As SWUtilities.gtcocswCompareGeometry
    Dim longStatus              As gtError_e
    Dim bAddToBinder            As Boolean
    Dim bOverwrite              As Boolean

    ' Connect to SOLIDWORKS
    Set swapp = Application.SldWorks

    ' Get the SOLIDWORKS Utilities tool interface
    Set swUtil = swapp.GetAddInObject("Utilities.UtilitiesApp")

    ' Get the CompareGeometry tool
    Set swUtilCompGeom = swUtil.GetToolInterface(2, longStatus)

    If Not longStatus = gtNOErr Then
        Debug.Print "Error getting compare geometry tool."
    End If

   ' Compare the volumes and faces of the specified part documents
    bAddToBinder = False
    bOverwrite = True
    Dim file1 As String
    Dim file2 As String
    Dim volDiffStatus As gtVolDiffStatusOptionType_e
    Dim faceDiffStatus As gtVolDiffStatusOptionType_e
    file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
    file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

    longStatus = swUtilCompGeom.CompareGeometry3(file1, "", file2, "", gtGdfFaceAndVolumeCompare, gtResultSaveReport, "C:\test\Report", bAddToBinder, bOverwrite, volDiffStatus, faceDiffStatus)

    If Not longStatus = gtNOErr Then
        Debug.Print "Error comparing geometries."
    End If

    Call diffStatus("Volume comparison", volDiffStatus)
    Call diffStatus("Face comparison", faceDiffStatus)

   ' Perform any necessary clean up
   longStatus = swUtilCompGeom.Close()

End Sub

Sub diffStatus(ByVal name As String, ByVal diffCode As gtVolDiffStatusOptionType_e)
    Debug.Print name
    Select Case diffCode
        Case gtSuccess
            Debug.Print "Succeeded"

        Case gtNotPerformed
            Debug.Print "Not performed"

        Case gtCanceled
            Debug.Print "Canceled"

        Case gtFailed
            Debug.Print "Failed"

        Case gtIdenticalParts
            Debug.Print "Identical parts"

        Case gtDifferentParts
            Debug.Print "Different parts"

        Case gtNoSolidBody
            Debug.Print "No solid body found"

        Case gtAlreadySaved
            Debug.Print "Already saved"

    End Select
    Debug.Print ""
End Sub
```
