---
title: "Get Whether Component Is Envelope And Excluded From BOM (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm"
---

# Get Whether Component Is Envelope And Excluded From BOM (VB.NET)

This example shows how to find out if a component is an envelope and whether the component is included in the bill of materials (BOM).

```vb
 '---------------------------------------------------------------------------
' Preconditions:
' 1. Open SOLIDWORKS and copy the code below to a VB.NET macro.
' 2. Ensure that the  specified file exists.
' 3. Specify your_license_key.
' 4. Open an Immediate window.
'
' Postconditions: Inspect the Immediate window.
'
' NOTE: ISwDMComponent5::ExcludeFromBom and ISwDMComponent5::IsEnvelope print
' to the Immediate Window for each component.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports SwDocumentMgr
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Public Sub main()
        Dim swClassFact As SwDocumentMgr.SwDMClassFactory
        Dim swDocMgr As SwDocumentMgr.SwDMApplication
        Dim swDoc As SwDocumentMgr.SwDMDocument7
        Dim swCfgMgr As SwDocumentMgr.SwDMConfigurationMgr
        Dim swConfiguration7 As SwDMConfiguration7
        Dim swComponents As Object
        Dim sDocFileName As String
        Dim nDocType As SwDocumentMgr.SwDmDocumentType
        Dim nRetVal As SwDocumentMgr.SwDmDocumentOpenError
        Dim sLicenseKey As String
        sLicenseKey = "your_license_key"
        sDocFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
        nDocType = SwDocumentMgr.SwDmDocumentType.swDmDocumentAssembly
        swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
        swDocMgr = swClassFact.GetApplication(sLicenseKey)
        swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
        swCfgMgr = swDoc.ConfigurationManager
        Dim SWConfigNames() As String
        SWConfigNames = swCfgMgr.GetConfigurationNames
        For j As Integer = 0 To UBound(SWConfigNames)
            swConfiguration7 = swCfgMgr.GetConfigurationByName(SWConfigNames(j))
            swComponents = swConfiguration7.GetComponents
            Debug.Print("Configuration Name = " & SWConfigNames(j))
            For I As Integer = 0 To UBound(swComponents)
                Dim comp As SwDMComponent5
                comp = swComponents(I)
                Debug.Print("Component Name = " & comp.Name)
                Debug.Print("       IsEnvelope = " & comp.IsEnvelope)
                Debug.Print("       ExcludeFromBOM = " & comp.ExcludeFromBOM)
            Next
            Debug.Print("_______________________________________________________")
        Next
        swDoc.CloseDoc()
    End Sub
    Public swApp As SldWorks

End Class
```
