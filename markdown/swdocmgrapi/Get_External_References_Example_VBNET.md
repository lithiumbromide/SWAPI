---
title: "Get External References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_External_References_Example_VBNET.htm"
---

# Get External References Example (VB.NET)

This example shows how to get all of the external references for the base part using the SOLIDWORKS Document Manager API.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the
 '    required DLLs are registered.
 ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Modify the path to the specified assembly.
 ' 4. Add the SolidWorks.Interop.swdocumentmgr.dll
 '    reference to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click:
 '       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 ' 5. Substitute your_license_key with your SOLIDWORKS Document Manager license key.
 ' 6. Ensure that c:\temp exists.
```

```vb
' Postconditions:
 ' 1. Inspect the Immediate Window for the external references and their
 '    configurations.
 ' 2. Inspect c:\temp\extRef.xml for more information about the external
 '     references.
 '--------------------------------------------------------------------------
```

```vb
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
     Dim numExtRefs As  Integer
     Dim xmlError As Integer
     Const docPath As String = "public_documents\samples\tutorial\api\assem2.sldasm"
     Const licenseKey As String = "your_license_key"
```

```vb
    Sub main()

         setDocType()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         dmDocMgr = dmClassFact.GetApplication(licenseKey)
         dmDoc = dmDocMgr.GetDocument(docPath, dmDocType,  True, status)

         If Not (dmDoc Is Nothing) Then
             NewMethod()
             dmDoc.GetXmlStream("c:\temp\extRef.xml", xmlError)
             dmDoc.CloseDoc()
         Else
             Debug.Print("Unable to open document. Check 'docPath' variable.")
         End If

     End Sub

     Sub NewMethod()

         dmExtRefOption = dmDocMgr.GetExternalReferenceOptionObject2
         dmSearchOpt = dmDocMgr.GetSearchOptionObject

         dmExtRefOption.SearchOption = dmSearchOpt
         dmExtRefOption.Configuration =  "Default"
         dmExtRefOption.NeedSuppress = True
         numExtRefs = dmDoc.GetExternalFeatureReferences2(dmExtRefOption)

         Debug.Print("External references:")
         PrintStrings("FilePath", dmExtRefOption.ExternalReferences)
         Debug.Print("")
         Debug.Print("Configurations of external references:")
         PrintStrings("ConfigName", dmExtRefOption.ReferencedConfigurations)

         dmSearchOpt = Nothing
         dmExtRefOption =  Nothing

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

     Sub PrintStrings(ByVal name As String, ByVal varInp As Object)

         Dim I As  Integer

         For I = LBound(varInp) To UBound(varInp)
             Dim str As String
             str = varInp(I)
             Debug.Print(name   " : " & str)
         Next I

     End Sub

 End  Module
```
