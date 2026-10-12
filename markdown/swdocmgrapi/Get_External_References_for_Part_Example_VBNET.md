---
title: "Get External References for Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_External_References_for_Part_Example_VBNET.htm"
---

# Get External References for Part Example (VB.NET)

This example shows how to get all of the external references for a part document.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 '    and ensure that the required DLLs are registered.
 ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Substitute part_path_and_filename with the filename
 '    of a part document containing one or more external references to other
 '    part documents.
 ' 4. Add the SolidWorks.Interop.swdocumentmgr.dll
 '    reference to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click:
 '       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 ' 5. Substitute your_license_key with your SOLIDWORKS Document
 '    Manager license key.
 ' 6. Ensure that c:\temp exists.
 '
 ' Postconditions:
 ' 1. Examine the Immediate Window for information about the external references.
 ' 2. Examine c:\temp\extRefPart.xml for more information about the
 '    external references.
 '--------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Imports System
 Imports System.Diagnostics

 Module Module1

     Dim dmClassFact As SwDMClassFactory
     Dim dmDocMgr As SwDMApplication4
     Dim dmDoc As SwDMDocument18
     Dim dmDocType As SwDmDocumentType
     Dim dmSearchOpt As SwDMSearchOption
     Dim status As SwDmDocumentOpenError
     Dim dmExtRefOption As SwDMExternalReferenceOption2
     Dim numExtRefs As Integer
     Dim xmlError As Integer
     Dim extRefs() As String
     Dim refConfigs() As String
     Dim refIDs() as Integer
     Dim featStatus As Boolean
     Dim featNames() As String
     Dim featTypes() As String
     Dim brokenStatus() As Integer
     Dim numFeat As Integer
     Dim i As Integer
     Dim j As Integer
     Const docPath As String = "part_path_and_filename "
     Const licenseKey As String = "your_license_key"

     Sub Main()

         setDocType()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         dmDocMgr = dmClassFact.GetApplication(licenseKey)
         dmDoc = dmDocMgr.GetDocument(docPath, dmDocType, True, status)

         If Not (dmDoc Is Nothing) Then
             GetReferences()
             dmDoc.GetXmlStream("c:\temp\extRefPart.xml", xmlError)
             dmDoc.CloseDoc()
         Else
             Debug.Print("Unable to open document. Check 'docPath' variable.")
         End If

     End Sub

     Sub GetReferences()

         ' Get external references
         dmExtRefOption = dmDocMgr.GetExternalReferenceOptionObject2
         dmExtRefOption.Configuration = "Default"
         dmExtRefOption.NeedSuppress = True
         dmSearchOpt = dmDocMgr.GetSearchOptionObject()
         dmSearchOpt.SearchFilters = (SwDmSearchFilters.SwDmSearchExternalReference + SwDmSearchFilters.SwDmSearchForPart)
         dmExtRefOption.SearchOption = dmSearchOpt

         ' Gets the paths and filenames of the external references,
         ' whether the external references are broken, and the names of their
         ' referenced configurations
         numExtRefs = dmDoc.GetExternalFeatureReferences3(dmExtRefOption)
         extRefs = dmExtRefOption.ExternalReferences
         refConfigs = dmExtRefOption.ReferencedConfigurations
         brokenStatus = dmExtRefOption.BrokenStatus
         refIDs = dmExtRefOption.IDs

         If (numExtRefs > 0) Then

             For i = 0 To numExtRefs - 1
                 Debug.Print("External reference: " & extRefs(i))
                 Debug.Print("  Broken reference (1=broken, 2=not broken, 0 = older version or N/A): " & brokenStatus(i))
                 Debug.Print("  Configuration name: " & refConfigs(i))
                 Debug.Print("  ID: " & refIDs(i))
                 Debug.Print("")
             Next

             ' Get the referenced feature names and types in the part document
             featStatus = dmExtRefOption.ReferencedFeatures(featNames, featTypes)
             Debug.Print("Referenced feature names and types in part document: ")
             numFeat = 0
             If (featStatus And (featNames IsNot Nothing)) Then
                 For j = LBound(extRefs) To UBound(extRefs)
                     Debug.Print("  Feature name: " & featNames(numFeat))
                     Debug.Print("  Feature type: " & featTypes(numFeat))
                     Debug.Print("")
                     numFeat = numFeat + 1
                 Next j

             Else
                 Debug.Print("  No referenced features in model document.")
             End If
         Else
             Debug.Print("No external references in the part document.")
         End If

     End Sub

     Sub setDocType()

         Dim typeStr As String

         typeStr = Mid$(docPath, (Len(docPath) + 1 - 6), 6)
         typeStr = UCase$(typeStr)

         If (typeStr = "SLDPRT") Then
             dmDocType = SwDmDocumentType.swDmDocumentPart
         ElseIf (typeStr = "SLDASM") Then
             dmDocType = SwDmDocumentType.swDmDocumentAssembly
         End If

     End Sub

 End Module
```
