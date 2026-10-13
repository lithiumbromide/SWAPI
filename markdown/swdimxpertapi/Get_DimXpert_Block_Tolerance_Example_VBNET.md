---
title: "Get DimXpert Block Tolerance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Block_Tolerance_Example_VBNET.htm"
---

# Get DimXpert Block Tolerance Example (VB.NET)

This example shows how to build and get attributes for the following DimXpert features:

* Hole

* Notch

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
' 2. Open an Immediate window.
' 3. Ensure that the SolidWorks.Interop.swdimxpert.dll interop
'    is loaded (right-click the project in the Project Explorer,
'    click Add Reference > .NET tab).
' 4. Ensure that the Microsoft Scripting Runtime library is loaded
'    (right-click the project in the Project Explorer and click
'     Add Reference > COM tab).
'
' Postconditions:
' 1. Inspect the Immediate window to see the ISO code for the part.
' 2. Open public_documents\samples\tutorial\api\cover_with_geometric_tolerances.sldprt.
' 3. Run this macro (F5).
' 4. Inspect the Immediate Window to see the ASME block tolerance values
'    for the part.
' 5. Logs the output of this macro in c:\temp\dimXpertInfo.txt.
' 6. Inspect the Immediate window.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swdimxpert
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports Scripting
Partial Class SolidWorksMacro
    Public Sub main()

        Dim swModelDoc As ModelDoc2
        swModelDoc = swapp.ActiveDoc
        If swModelDoc Is Nothing Then
            Exit Sub
        End If
        Dim f As New FileSystemObject
        Dim textStr As TextStream
        textStr = f.CreateTextFile("C:\temp\dimXpertInfo.txt", True)
        If textStr Is Nothing Then
            Debug.Print("Error creating temp file.")
            Exit Sub
        End If
        Call log("------------------------", textStr)
        Call log("Starting DimXpert log...", textStr)
        Call retrieve_info_text(swapp, textStr)
        textStr.Close()
    End Sub
    Private Sub log(ByVal text As String, ByVal textStr As TextStream)
        Debug.Print(text)
        textStr.WriteLine(text)
    End Sub
    Private Sub retrieve_info_text(ByVal swapp As SldWorks, ByVal textStr As TextStream)
        Dim dimXpertMgr As DimXpertManager
        dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
        Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
        Dim dimXpertPartObj As DimXpertPart
        dimXpertPartObj = dimXpertMgr.DimXpertPart
        Dim dimXpertPart As DimXpertPart
        dimXpertPart = dimXpertPartObj
        Dim vAnnotations As Object
        vAnnotations = dimXpertPart.GetAnnotations()
        Call log("------------------------", textStr)
        Call log("Block Tolerances...", textStr)
        Call log("------------------------", textStr)
        Call listBlockTolerances_text(dimXpertPart, textStr)
    End Sub
    Private Sub listBlockTolerances_text(ByVal dimXpertPart As DimXpertPart, ByVal textStr As TextStream)
        Dim blockTols As DimXpertBlockTolerances
        Dim boolstatus As Boolean
        Dim lin1 As Double, lin1prec As Long
        Dim lin2 As Double, lin2prec As Long
        Dim lin3 As Double, lin3prec As Long
        Dim ang As Double
        Dim isoCode As Long
        blockTols = dimXpertPart.GetBlockTolerances()
        If Not blockTols Is Nothing Then
            Select Case blockTols.Type
                Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
                    boolstatus = blockTols.GetToleranceValues(lin1, lin1prec, lin2, lin2prec, lin3, lin3prec, ang)
                    Call log("swDimXpertBlockToleranceType_ASMEInch", textStr)
                    Call log( _
                        "Linear1: " + Format(lin1prec) + " Places = " + Format(lin1, "##0.000000") + "        " + _
                        "Linear3: " + Format(lin3prec) + " Places = " + Format(lin3, "##0.000000") + vbNewLine + _
                        "Linear2: " + Format(lin2prec) + " Places = " + Format(lin2, "##0.000000") + "        " + _
                        "Angular = " + Format(ang * 57.2957795130823, "##0.000000"), textStr)
                Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
                    Call log("swDimXpertBlockToleranceType_ISO2768", textStr)
                    boolstatus = blockTols.GetISO2768PartType(isoCode)
                    Select Case isoCode
                        Case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Fine
                            Call log("General Tolerance: Fine", textStr)
                        Case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Medium
                            Call log("General Tolerance: Medium", textStr)
                        Case  swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Coarse
                            Call log("General Tolerance: Coarse", textStr)
                        Case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_VeryCoarse
                            Call log("General Tolerance: Very Coarse", textStr)
                    End Select
            End Select
        End If
    End Sub

    Public swApp As SldWorks
End Class
```
