---
title: "Get Configuration Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Configuration_Information_Example_VBNET.htm"
---

# Get Configuration Information Example (VB.NET)

This example shows how to use the SOLIDWORKS Document Manager API to get configuration-related information for an external part document whose custom properties were transferred from the original part document.

```vb
 ' --------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 '    and ensure that the required DLLs are registered.
 ' 2. Copy and paste this module into a VB.NET console application in Microsoft
 '    Visual Studio.
 ' 3. Add the Solidworks.Interop.swdocumentmgr.dll reference to the project:
 '    a. Right-click the solution in the Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click install_dir\api\redist\Solidworks.Interop.swdocumentmgr.dll.
 '    e. Click Add.
 '    f. Click OK.
 ' 4. In the code:
'    a. Substitute your_license_key with your SOLIDWORKS Document Manager license key.
 '    b. Ensure that the file pointed to by sDocFileName exists.
 ' 5. Press F5 to run the program.
 '
 ' Postconditions:
 ' 1. Examine the Immediate Window.
 ' 2. Verify that both fromparent+ prefaced and non-prefaced custom property
 '    values are shown.
 '---------------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr

 Module Module1

     Sub ProcessDocCustomProperties(ByVal swDoc As SwDMDocument19)

         Dim vCustPropNameArr As Object
         Dim vCustPropName As Object
         Dim sCustPropStr As String
         Dim sCustPropStrWOPrefix As String
         Dim nPropType As Integer

         vCustPropNameArr = swDoc.GetCustomPropertyNames : If IsNothing(vCustPropNameArr) Then Exit Sub
         Debug.Print("  Document Custom Properties:")

         For Each vCustPropName In vCustPropNameArr
             sCustPropStr = swDoc.GetCustomProperty(vCustPropName, nPropType)
             Debug.Print("    Prefaced     = " & vCustPropName & " <" & nPropType & "> = " & sCustPropStr)

             sCustPropStrWOPrefix = swDoc.GetCustomProperty2(vCustPropName, nPropType)
             Debug.Print("    Not Prefaced = " & vCustPropName & " <" & nPropType & "> = " & sCustPropStrWOPrefix)

             Debug.Print("")

         Next

         Debug.Print("")

     End Sub

     Sub ProcessConfigCustomProperties(ByVal swCfg As SwDMConfiguration14)

         Dim vCustPropNameArr As Object
         Dim vCustPropName As Object
         Dim sCustPropStr As String
         Dim sCustPropStrWOPrefix As String
         Dim nPropType As Integer

         vCustPropNameArr = swCfg.GetCustomPropertyNames
         If IsNothing(vCustPropNameArr) Then Exit Sub
         Debug.Print("    Configuration Custom Properties:")

         For Each vCustPropName In vCustPropNameArr
             sCustPropStr = swCfg.GetCustomProperty(vCustPropName, nPropType)
             Debug.Print("      Prefaced     = " & vCustPropName & " <" & nPropType & "> = " & sCustPropStr)

             sCustPropStrWOPrefix = swCfg.GetCustomProperty2(vCustPropName, nPropType)
             Debug.Print("      Not Prefaced = " & vCustPropName & " <" & nPropType & "> = " & sCustPropStrWOPrefix)

             Debug.Print("")
         Next

         Debug.Print("")

     End Sub

     Sub main()

         Const sLicenseKey As String = "your_license_key"
         Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\ExternalReferencedPart.sldprt"

         Dim swClassFact As SwDMClassFactory
         Dim swDocMgr As SwDMApplication
         Dim swDoc As SwDMDocument19
         Dim swCfgMgr As SwDMConfigurationMgr2
         Dim vCfgNameArr As Object
         Dim vCfgName As Object
         Dim swCfg As SwDMConfiguration17
         Dim nDocType As Integer
         Dim nRetVal As Integer
         Dim results As Integer

         ' Determine type of SOLIDWORKS file based on file extension

         If InStr(LCase(sDocFileName), "sldprt") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentPart
         ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentAssembly
         ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentDrawing
         Else

             ' Not a SOLIDWORKS file
             nDocType = SwDmDocumentType.swDmDocumentUnknown

             ' So cannot open
             Exit Sub

         End If

         ' Because drawing documents do not have configurations,
         ' only continue running the project if the document
         ' is a part or assembly document

         If (nDocType <> SwDmDocumentType.swDmDocumentDrawing) Then

             swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
             swDocMgr = swClassFact.GetApplication(sLicenseKey)
             swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, False, nRetVal) : Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone = nRetVal)
             swCfgMgr = swDoc.ConfigurationManager

             Debug.Print("File = " & swDoc.FullName)
             Debug.Print("  Active Configuration Name           = " & swCfgMgr.GetActiveConfigurationName)
             Debug.Print("")
             Debug.Print("  Version                 = " & swDoc.GetVersion)
             Debug.Print("  Author                  = " & swDoc.Author)
             Debug.Print("  Comments                = " & swDoc.Comments)
             Debug.Print("  Creation Date (string)   = " & swDoc.CreationDate)
             Debug.Print("  Creation Date (numeric)  = " & swDoc.CreationDate2)
             Debug.Print("  Keywords                = " & swDoc.Keywords)
             Debug.Print("  Last Saved By             = " & swDoc.LastSavedBy)
             Debug.Print("  Last Saved Date (string)  = " & swDoc.LastSavedDate)
             Debug.Print("  Last Saved Date (numeric) = " & swDoc.LastSavedDate2)
             Debug.Print("  Subject                 = " & swDoc.Subject)
             Debug.Print("  Title                   = " & swDoc.Title)
             Debug.Print("  Last Update Timestamp         = " & swDoc.GetLastUpdateStamp)
             Debug.Print("  Is Detached Drawing ? " & swDoc.IsDetachedDrawing)
             Debug.Print("")

             vCfgNameArr = swCfgMgr.GetConfigurationNames2(results)

             Debug.Print("  Number of configurations: " & swCfgMgr2.GetConfigurationCount2(results))

             For Each vCfgName In vCfgNameArr
                 swCfg = swCfgMgr.GetConfigurationByName2(vCfgName, results)

                 Debug.Print("  " & vCfgName)
                 Debug.Print("    Description              = " & swCfg.Description)
                 Debug.Print("    Parent Configuration Name            = " & swCfg.GetParentConfigurationName)
                 Debug.Print("    Last Update Timestamp          = " & swCfg.GetLastUpdateStamp)
                Debug.Print("    3DExperience configuration type as defined by swDm3DExperienceCfgType_e          = " & swCfg.Get3DExperienceType)
                Debug.Print("    3DExperience physical product represented by this configuration          = " & swCfg.GetRepresentationParent)
                 Debug.Print("")

                 ProcessConfigCustomProperties(swCfg)
             Next

             ProcessDocCustomProperties(swDoc)

         End If

     End Sub

 End Module
```
