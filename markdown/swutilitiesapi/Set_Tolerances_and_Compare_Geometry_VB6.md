---
title: "Set Tolerances and Compare Geometry Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Set_Tolerances_and_Compare_Geometry_VB6.htm"
---

# Set Tolerances and Compare Geometry Example (VBA)

```vb
This example shows how to set the tolerances and then compare the volume and geometry of two versions of the same part using the SOLIDWORKS Utilities API.
```

```
'----------------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS , click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that the specified parts exist.
' 4. Verify that C:\test\ exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates a geometry comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets position and angular tolerance statuses.
' 3. Gets face and volume comparison statuses.
' 4. Examine the Immediate window, graphics area, and C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'-------------------------------------------------------------------------------------
```

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

Dim swUtil  As SWUtilities.gtcocswUtilities
Dim swUtilCompGeom  As SWUtilities.gtcocswCompareGeometry
Dim OUtils As SWUtilities.gtcocswUtilOptions
Dim file1 As String
Dim file2 As String
Dim reportname As String
Dim errorcode As gtError_e
Dim longStatus  As gtError_e
Dim posTol As Double
Dim angTol As Double
Dim AddToDesignBinder As Boolean
Dim OverwriteReport As Boolean

reportname = "C:\test\Report"
AddToDesignBinder = False
OverwriteReport = True

' Get pointer to SOLIDWORKS Utilities interface
Set swUtil = swApp.GetAddInObject("Utilities.UtilitiesApp")

' Get pointer to SOLIDWORKS Utilities Compare Geometry tool
Set swUtilCompGeom = swUtil.GetToolInterface(gtSwToolGeomDiff, errorcode)

' Get SOLIDWORKS Utilities options
Set OUtils = swUtil.Options
posTol = 0.0001 ' Meters
angTol = 0.000001 ' Radians

' Set position tolerance
errorcode = OUtils.SetPositionTolerance(posTol)
Debug.Print "Position tolerance set." & " gtError_e: " & errorcode

' Set angular tolerance
errorcode = OUtils.SetAngularTolerance(angTol)
Debug.Print "Angular tolerance set." & " gtError_e: " & errorcode
Debug.Print ""
Dim volDiffStatus As gtVolDiffStatusOptionType_e
Dim faceDiffStatus As gtVolDiffStatusOptionType_e
file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

' Compare the geometry of the faces and volumes and save results to a report
errorcode = swUtilCompGeom.CompareGeometry3(file1, "", file2, "", gtGdfFaceAndVolumeCompare, gtResultSaveReport, reportname, AddToDesignBinder, OverwriteReport, volDiffStatus, faceDiffStatus)
    If Not longStatus = gtNOErr Then
        Debug.Print "Error comparing geometries. Inspect gtError_e = " & longStatus & " in the API help."
    End If

    Call diffStatus("Volume comparison", volDiffStatus)
    Call diffStatus("Face comparison", faceDiffStatus)

' Perform any necessary cleanup
errorcode = swUtilCompGeom.Close()
```

```vb
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
