---
title: "Get Whether Part Has Frozen Features (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Part_Has_Frozen_Features_Example_vbnet.htm"
---

# Get Whether Part Has Frozen Features (VB.NET)

## Get Whether Part Has Frozen Features Example (VB.NET)

This example shows how to get whether a part document has frozen features, and, if so, whether those features need updating.

```vb
 '------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Help Getting Started
 '    topic and register the required DLLs.
  ' 2. Copy and paste this module into a VB.NET
 '    console application in Microsoft Visual Studio.
 ' 3. Load the latest SolidWorks.Interop.swdocumentmgr.dll
 '    interop assembly by:
 '    a. Right-clicking the project name in the Project Explorer.
 '    b. Clicking Add Reference.
 '    c. Clicking the interop assembly in the .NET
 '       tab or browsing for the DLL in install_dir/api/redist.
 ' 4. Substitute your license key for your_license_key in the code.
 ' 5. Make sure that the part document opened by this application
 '    exists.
 ' 6. Open the Immediate window.
 '
 ' Postconditions: Whether the part document contains frozen features
 ' is printed to the Immediate window, and, if so, whether
 ' those features need updating.
 '
 ' NOTE: This sample application was developed using
 ' Microsoft Visual Studio 2008. If you use another version of
 ' Microsoft Visual Studio, you might need to add more references to get
 ' this application to compile.
 '------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Imports System.Diagnostics

 Module Module1
     Sub Main()

         Dim dmClassFact As SwDMClassFactory = Nothing
         Dim dmDocMgr As ISwDMApplication3 = Nothing
         Dim dmDoc As ISwDMDocument16 = Nothing
         Dim dmError As SwDmDocumentOpenError = Nothing
         Dim namePart As String = ""
         Dim hasFrozenFeatures As Boolean = False
         Dim frozenFeaturesNeedUpdating As Boolean = False

         dmClassFact =  New SwDMClassFactory()
         'Do not distribute license key
         dmDocMgr =  DirectCast(dmClassFact.GetApplication("your_license_key"), ISwDMApplication3)
         namePart = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\FreezeBarNeedsRebuild2.sldprt"

         'Get the SOLIDWORKS part document
         dmDoc =  DirectCast(dmDocMgr.GetDocument(namePart, SwDmDocumentType.swDmDocumentPart, False, dmError), ISwDMDocument16)
         Debug.Print("Document's full name: " + dmDoc.FullName)
         Debug.Print("  Date document last saved: " + dmDoc.LastSavedDate)

         ' Get whether the part document has frozen features and
         ' whether those features need updating
         hasFrozenFeatures =  CBool(dmDoc.HasFrozenFeatures(frozenFeaturesNeedUpdating))
         Debug.Print("    Does the part document have frozen features? " & hasFrozenFeatures)
         If hasFrozenFeatures Then
             Debug.Print("    Do any of the frozen features need updating? " & frozenFeaturesNeedUpdating)
         End If
     End Sub

 End Module
```
