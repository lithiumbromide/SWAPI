---
title: "Get DimXpert Block Tolerance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Block_Tolerance_Example_VB.htm"
---

# Get DimXpert Block Tolerance Example (VBA)

This example shows how to get the following block tolerance values:

* ASME

* ISO Code

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\shaft.sldprt.
' 2. Open an Immediate window.
' 3. Ensure that the latest SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
' 4. Ensure that the Microsoft Scripting Runtime library is loaded
'    in Tools > References.
'
' Postconditions:
' 1. Inspect the Immediate window to see the ISO code for the part.
' 2. Open public_documents\api\cover_with_geometric_tolerances.sldprt.
' 3. Run this macro (F5).
' 4. Inspect the Immediate Window to see the ASME block tolerance values
'    for the part.
' 5. Logs the output of this macro in c:\temp\dimXpertInfo.txt.
' 6. Inspect the Immediate window.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
Sub Main()
    Dim swapp As SldWorks.SldWorks
    Set swapp = Application.SldWorks
 Dim swModelDoc As SldWorks.ModelDoc2
  Set swModelDoc = swapp.ActiveDoc
   If swModelDoc Is Nothing Then
     Exit Sub
   End If
    Dim f As New FileSystemObject
    Dim textStr As TextStream
    Set textStr = f.CreateTextFile("C:\temp\dimXpertInfo.txt", True)
    If textStr Is Nothing Then
        Debug.Print "Error creating temp file."
        Exit Sub
    End If

    Call log("------------------------", textStr)
    Call log("Starting DimXpert log...", textStr)
    Call retrieve_info_text(swapp, textStr)
    textStr.Close
End Sub
Private Sub log(text As String, textStr As TextStream)
    Debug.Print text
    textStr.WriteLine (text)
End Sub
Private Sub retrieve_info_text(swapp As SldWorks.SldWorks, textStr As TextStream)
    Dim dimXpertMgr As SldWorks.DimXpertManager

    Set dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
    Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
    Dim dimXpertPartObj As dimXpertPart
    Set dimXpertPartObj = dimXpertMgr.dimXpertPart

    Dim dimXpertPart As SwDimXpert.dimXpertPart
    Set dimXpertPart = dimXpertPartObj

    Dim vAnnotations As Variant

    vAnnotations = dimXpertPart.GetAnnotations()

    Call log("------------------------", textStr)
    Call log("Block Tolerances...", textStr)
    Call log("------------------------", textStr)

    Call listBlockTolerances_text(dimXpertPart, textStr)

End Sub
Private Sub listBlockTolerances_text(dimXpertPart As SwDimXpert.dimXpertPart, textStr As TextStream)
    Dim blockTols As SwDimXpert.DimXpertBlockTolerances
    Dim boolstatus As Boolean
    Dim lin1 As Double, lin1prec As Long
    Dim lin2 As Double, lin2prec As Long
    Dim lin3 As Double, lin3prec As Long
    Dim ang As Double
    Dim isoCode As Long

    Set blockTols = dimXpertPart.GetBlockTolerances()
    If Not blockTols Is Nothing Then
        Select Case blockTols.Type

            Case swDimXpertBlockToleranceType_ASMEInch
                boolstatus = blockTols.GetToleranceValues(lin1, lin1prec, lin2, lin2prec, lin3, lin3prec, ang)
                Call log("swDimXpertBlockToleranceType_ASMEInch", textStr)
                Call log( _
                    "Linear1: " + Format(lin1prec) + " Places = " + Format(lin1, "##0.000000") + "        " + _
                    "Linear3: " + Format(lin3prec) + " Places = " + Format(lin3, "##0.000000") + vbNewLine + _
                    "Linear2: " + Format(lin2prec) + " Places = " + Format(lin2, "##0.000000") + "        " + _
                    "Angular = " + Format(ang * 57.2957795130823, "##0.000000"), textStr)

            Case swDimXpertBlockToleranceType_ISO2768
            Call log("swDimXpertBlockToleranceType_ISO2768", textStr)
                boolstatus = blockTols.GetISO2768PartType(isoCode)
                Select Case isoCode

                    Case swDimXpertISO2768PartType_Fine
                     Call log("General Tolerance: Fine", textStr)

                    Case swDimXpertISO2768PartType_Medium
                     Call log("General Tolerance: Medium", textStr)

                    Case swDimXpertISO2768PartType_Coarse
                     Call log("General Tolerance: Coarse", textStr)

                    Case swDimXpertISO2768PartType_VeryCoarse
                     Call log("General Tolerance: Very Coarse", textStr)

                End Select
        End Select
    End If

End Sub
```
