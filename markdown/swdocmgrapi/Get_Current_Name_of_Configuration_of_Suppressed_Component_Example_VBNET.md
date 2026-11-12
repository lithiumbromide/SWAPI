---
title: "Get the Current Name of the Configuration of a Suppressed Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm"
---

# Get the Current Name of the Configuration of a Suppressed Component Example (VB.NET)

## Get Current Name of Configuration of Suppressed Component Example (VB.NET)

This example shows how to get the current name of the configuration of a suppressed component.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 '    and ensure that the required DLLs are registered.
 ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference
 '    to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
 '    e. Click Add.
 '    f. Click OK.
 ' 4. Substitute your_license_key with your SOLIDWORKS
 '    Document Manager license key.
 ' 5. Substitute assembly_with_suppressed_comps with the path to an assembly
 '    that contains one or more suppressed components.
 ' 6. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window for configuration information.
 '----------------------------------------------------------------------------

 Imports System
 Imports System.Diagnostics
 Imports SolidWorks.Interop.swdocumentmgr
 Imports System.IO

 Module Module1

     'Specify your license key and path and filename of assembly document
     Const sLicenseKey As String = "your_license_key"
     Const sDocFileName As String = "assembly_with_suppressed_comps"

     Dim dmClassFact As SwDMClassFactory
     Dim dmDocMgr As SwDMApplication4
     Dim dmDoc As SwDMDocument18
     Dim dmDoc2 As SwDMDocument18
     Dim nRetVal As SwDmDocumentOpenError
     Dim dmSearchOpt As SwDMSearchOption
     Dim dmExtRefOption As SwDMExternalReferenceOption2
     Dim numExtRefs As Integer

     Sub Main()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory.1")
         dmDocMgr = dmClassFact.GetApplication(sLicenseKey)
         dmDoc = dmDocMgr.GetDocument(sDocFileName, GetDocType(sDocFileName), True, nRetVal)
         Debug.Print("File = " + dmDoc.FullName)
         Debug.Print("")

         dmExtRefOption = dmDocMgr.GetExternalReferenceOptionObject2
         dmSearchOpt = dmDocMgr.GetSearchOptionObject
         dmSearchOpt.SearchFilters = (SwDmSearchFilters.SwDmSearchExternalReference + SwDmSearchFilters.SwDmSearchForAssembly + SwDmSearchFilters.SwDmSearchInContextReference)

         dmExtRefOption.SearchOption = dmSearchOpt
         dmExtRefOption.Configuration = "Default"
         dmExtRefOption.NeedSuppress = True
         numExtRefs = dmDoc.GetExternalFeatureReferences3(dmExtRefOption)

         Dim arrExtRefs As Array
         arrExtRefs = dmExtRefOption.ExternalReferences

         Dim config As SwDMConfiguration12
         Dim configMgr As SwDMConfigurationMgr = dmDoc.ConfigurationManager
         config = configMgr.GetConfigurationByName(configMgr.GetActiveConfigurationName())
         Dim comps As Object = config.GetComponents()
         Dim arrComps As Array
         arrComps = comps

         For Each swComp As SwDMComponent9 In arrComps
             Debug.Print("Component name: " + swComp.Name2)
             Debug.Print("Component configuration name: " + swComp.ConfigurationName)
             Debug.Print("Component configuration ID: " + swComp.ConfigurationID.ToString)
             Debug.Print("Component ID: " + swComp.GetID.ToString)
             Debug.Print("")

             Dim ComponentPathName As String = swComp.PathName
             'Check validity of the component's path name
             'It might be out of date if the path changed after
             'the component was suppressed
             If Not File.Exists(ComponentPathName) Then
                 'If that file cannot be found, look for an external
                 'reference with the same name
                 ComponentPathName = FindExtRefPath(swComp.PathName, arrExtRefs)
             End If

             dmDoc2 = dmDocMgr.GetDocument(ComponentPathName, GetDocType(ComponentPathName), False, nRetVal)
             Dim config2 As SwDMConfiguration12
             Dim configMgr2 As SwDMConfigurationMgr = dmDoc2.ConfigurationManager
             Dim confignames As String()
             confignames = configMgr2.GetConfigurationNames()
             Dim arrConfigNames As New ArrayList(confignames)

             ' If the configuration name for the component doesn't match an
             ' existing config name in the reference part, go find the
             ' updated config name from the part
             If Not arrConfigNames.Contains(swComp.ConfigurationName) Then

                 For Each configName As String In arrConfigNames
                     config2 = configMgr2.GetConfigurationByName(configName)
                     If config2.GetID() = swComp.ConfigurationID Then
                         Debug.Print("Reference part configuration name: " + config2.Name2)
                     End If
                 Next
             End If

             dmDoc2.CloseDoc()
         Next
     End Sub

     Private Function FindExtRefPath(ByVal name As String, ByVal arrComps As Array) As String
         Dim ExtrefPathName As String = name
         Dim nameParts As String() = name.Split("\"c)
         Dim justName As String = nameParts.GetValue(nameParts.GetUpperBound(0)).ToString()

         Dim i As Integer = arrComps.GetLowerBound(0)
         Dim found As [Boolean] = False
         While (i <= arrComps.GetUpperBound(0)) AndAlso Not found
             Dim extref As String = (arrComps.GetValue(i)).ToString()
             Dim extrefParts As String() = extref.Split("\"c)
             Dim justextrefName As String = extrefParts.GetValue(extrefParts.GetUpperBound(0)).ToString()
             If justextrefName = justName Then
                 found = True
                 ExtrefPathName = extref
             End If
             i += 1
         End While

         Return ExtrefPathName

     End Function

     Private Function GetDocType(ByVal name As String) As SwDmDocumentType
         Dim nDocType As SwDmDocumentType = SwDmDocumentType.swDmDocumentUnknown
         If name.EndsWith("SLDPRT") Then
             nDocType = SwDmDocumentType.swDmDocumentPart
         ElseIf name.EndsWith("SLDASM") Then
             nDocType = SwDmDocumentType.swDmDocumentAssembly
         End If

         Return nDocType
     End Function

 End Module
```
