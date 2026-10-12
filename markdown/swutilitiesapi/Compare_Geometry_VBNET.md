---
title: "Compare Geometry Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Compare_Geometry_VBNET.htm"
---

# Compare Geometry Example (VB.NET)

This example shows how to use the SOLIDWORKS Utilities API to compare geometries in two part documents.

```
'---------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference >
'     browse to install_dir\api\redist > SolidWorks.Interop.gtswutilities.dll).
' 3. Verify that the specified files exist.
' 4. Verify that C:\test\ exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates C:\test\Report\gtReportIndex.htm.
' 2. Gets the face and volume comparison statuses.
' 3. Examine the Immediate window, graphics area, and
'    C:\test\report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'--------------------------------------------------------------------------------
```

```vb
Imports SOLIDWORKS.Interop.sldworks
Imports SOLIDWORKS.Interop.swconst
Imports SOLIDWORKS.Interop.gtswutilities
Imports System
Imports System.Diagnostics
Partial Class SOLIDWORKSMacro

    Sub main()

        Dim swUtil As gtcocswUtilities
        Dim swUtilCompGeom As gtcocswCompareGeometry
        Dim longStatus As gtError_e
        Dim bAddToBinder As Boolean
        Dim bOverwrite As Boolean
        Dim errorCode As Integer

        ' Get the SOLIDWORKS Utilities tool interface
        swUtil = swapp.GetAddInObject("Utilities.UtilitiesApp")

        ' Get the CompareGeometry tool
        swUtilCompGeom = swUtil.GetToolInterface(2, errorCode)
        If Not errorCode = gtError_e.gtNOErr Then
            Debug.Print("Error getting compare geometry tool.")
        End If

        ' Compare the volumes and faces of the specified part documents
        bAddToBinder = False
        bOverwrite = True
        Dim file1 As String
        Dim file2 As String
        Dim volDiffStatus As Integer
        Dim faceDiffStatus As Integer
        file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
        file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"
        longStatus = swUtilCompGeom.CompareGeometry3(file1, "", file2, "", gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare, gtResultOptions_e.gtResultSaveReport, "C:\test\Report", bAddToBinder, bOverwrite, volDiffStatus, faceDiffStatus)
        If Not longStatus = gtError_e.gtNOErr Then
            Debug.Print("Error comparing geometries.")
        End If
        Call diffStatus("Volume comparison", volDiffStatus)
        Call diffStatus("Face comparison", faceDiffStatus)

        ' Perform any necessary clean up
        longStatus = swUtilCompGeom.Close()

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
    End Sub

    Public swApp As SldWorks
End Class
```
