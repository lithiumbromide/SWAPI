---
title: "Set Tolerances and Compare Geometry Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Set_Tolerances_and_Compare_Geometry_VBNET.htm"
---

# Set Tolerances and Compare Geometry Example (VB.NET)

This example shows how to set the tolerances and then compare the volume and geometry of two versions of the same part using the SOLIDWORKS Utilities API.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Utilities as an add-in
 '    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
 ' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
 '    (right-click the project in Project Explorer, click Add Reference >
 '    browse to install_dir\api\redist > SolidWorks.Interop.gtswutilities.dll).
 ' 3. Verify that the specified files exist.
 ' 4. Verify that C:\test\ exists.
 '
 ' Postconditions:
 ' 1. Creates a geometry comparison report, C:\test\Report\gtReportIndex.htm.
 ' 2. Gets position and angular tolerance statuses.
 ' 3. Gets face and volume comparison statuses.
 ' 4. Examine the Immediate window, graphics area, and C:\test\Report\gtReportIndex.htm.
 '
 ' NOTE: Because the parts are used elsewhere, do not save changes.
 '-------------------------------------------------------------------------
Imports SOLIDWORKS.Interop.sldworks
Imports SOLIDWORKS.Interop.swconst
Imports SOLIDWORKS.Interop.gtswutilities
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SOLIDWORKSMacro

    Dim Part As PartDoc

    Sub main()

        Part = swApp.ActiveDoc

        Dim swUtil As gtcocswUtilities
        Dim swUtilCompGeom As gtcocswCompareGeometry
        Dim OUtils As gtcocswUtilOptions
        Dim file1 As String
        Dim file2 As String
        Dim reportname As String
        Dim errorcode As Integer
        Dim posTol As Double
        Dim angTol As Double
        Dim AddToDesignBinder As Boolean
        Dim OverwriteReport As Boolean

        reportname = "C:\test\Report"
        AddToDesignBinder = False
        OverwriteReport = True

        ' Get pointer to SOLIDWORKS Utilities interface
        swUtil = swApp.GetAddInObject("Utilities.UtilitiesApp")

        ' Get pointer to SOLIDWORKS Utilities Compare Geometry tool
        swUtilCompGeom = swUtil.GetToolInterface(gtSwTools_e.gtSwToolGeomDiff, errorcode)

        ' Get SOLIDWORKS Utilities options
        OUtils = swUtil.Options
        posTol = 0.0001 ' Meters
        angTol = 0.000001 ' Radians

        ' Set position tolerance
        errorcode = OUtils.SetPositionTolerance(posTol)
        Debug.Print("Position tolerance is set." & " gtError_e: " & errorcode)

        ' Set angular tolerance
        errorcode = OUtils.SetAngularTolerance(angTol)
        Debug.Print("Angular tolerance is set." & " gtError_e: " & errorcode)
        Debug.Print("")
        Dim volDiffStatus As Integer
        Dim faceDiffStatus As Integer
        file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
        file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

        ' Compare the geometry of the faces and volumes and save results to a report
        errorcode = swUtilCompGeom.CompareGeometry3(file1, "", file2, "", gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare, gtResultOptions_e.gtResultSaveReport, reportname, AddToDesignBinder, OverwriteReport, volDiffStatus, faceDiffStatus)
        If Not errorcode = gtError_e.gtNOErr Then
            Debug.Print("Error comparing geometries. Inspect gtError_e = " & errorcode & " in the API help.")
        End If

        Call diffStatus("Volume comparison", volDiffStatus)
        Call diffStatus("Face comparison", faceDiffStatus)

        ' Perform any necessary cleanup
        errorcode = swUtilCompGeom.Close()

    End Sub

    Sub diffStatus(ByVal name As String, ByVal diffCode As gtVolDiffStatusOptionType_e)
        Debug.Print(name)
        Select Case diffCode
            Case gtVolDiffStatusOptionType_e.gtSuccess
                Debug.Print("Succeeded")
            Case gtVolDiffStatusOptionType_e.gtNotPerformed
                Debug.Print("Not performed")
            Case gtVolDiffStatusOptionType_e.gtCanceled
                Debug.Print("Canceled")
            Case gtVolDiffStatusOptionType_e.gtFailed
                Debug.Print("Failed")
            Case gtVolDiffStatusOptionType_e.gtIdenticalParts
                Debug.Print("Identical parts")
            Case gtVolDiffStatusOptionType_e.gtDifferentParts
                Debug.Print("Different parts")
            Case gtVolDiffStatusOptionType_e.gtNoSolidBody
                Debug.Print("No solid body found")
            Case gtVolDiffStatusOptionType_e.gtAlreadySaved
                Debug.Print("Already saved")
        End Select
        Debug.Print("")
    End Sub
    Public swApp As SldWorks
End Class
```
