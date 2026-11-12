---
title: "Get, Add, Change, And Delete Cut-List Custom Properties (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm"
---

# Get, Add, Change, And Delete Cut-List Custom Properties (VB.NET)

## Get, Add, Change, And Delete Cut-List Custom Properties Example (VB.NET)

This example shows how to get cut-list items and their custom properties and how to add, modify, and delete a cut-list custom property.

'---------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API
**' Getting Started** topic and ensure that the
' required DLLs have been registered.
' 2. Copy and paste this module into a VB.NET console
' application in Microsoft Visual Studio.
' 3. Ensure that the specified part exists or point
' to another document that contains a cut list with
' custom properties).
' 4. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference
' to the project:
' a. Right-click the solution in Solution Explorer.
' b. Click **Add Reference**.
' c. Click **Browse**.
' d. Click `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll.**
' e. Click **Add.**
' f. Click **Close.**
' 5. Substitute `your_license_code` with your SOLIDWORKS
' Document Manager license key.
' 6. Compile and run this program in Debug mode.
'
' Postconditions: Inspect the Output Window and the code to see
' how the API is used.
'---------------------------------------------------------------------------

Imports SolidWorks.Interop.swdocumentmgr

Module Module1

Sub main()

Dim swClassFact As SwDMClassFactory
Dim swDocMgr As SwDMApplication
Dim swDocument10 As SwDMDocument10
Dim swDocument13 As SwDMDocument13

```vb
        Dim swDMConfigurationMgr As SwDMConfigurationMgr
         Dim config As SwDMConfiguration16
```

Dim sDocFileName As String
Dim nDocType As SwDmDocumentType
Dim nRetVal As SwDmDocumentOpenError
Dim sLicenseKey As String

sLicenseKey = "`your_license_code`" ' Specify your SOLIDWORKS Document Manager license key
sDocFileName = ("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\weldments\weldment_box2.sldprt") ' Specify your model document
nDocType = SwDmDocumentType.swDmDocumentPart
swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")

swDocMgr = swClassFact.GetApplication(sLicenseKey)
swDocument10 = swDocMgr.GetDocument(sDocFileName, nDocType, False, nRetVal)
swDocument13 = swDocument10

Debug.Print("Last Update Stamp: " & swDocument13.**GetLastUpdateTimeStamp**)

```vb
        swDMConfigurationMgr = swDocument13.ConfigurationManager
         config = swDMConfigurationMgr.GetConfigurationByName("Default")

         Dim vCutListItems As Object
         vCutListItems = config.GetCutListItems

         Dim Cutlist As SwDMCutListItem3
         Dim I As  Integer
         Dim nType As Integer
         Dim nLink As String
         Dim J As  Integer
         Dim vPropNames As Object

         Debug.Print("GET CUT-LIST ITEM")

         For I = 0 To UBound(vCutListItems)
             Cutlist = vCutListItems(I)
             Debug.Print("Name : " & Cutlist.Name)
             Debug.Print("   Quantity : " & Cutlist.Quantity)
             vPropNames = Cutlist.GetCustomPropertyNames

             If Not (IsNothing(vPropNames)) Then
                 Debug.Print("   GET CUSTOM PROPERTIES")
                 For J = 0 To UBound(vPropNames)
                     Debug.Print("   Property Name : " & vPropNames(J))
                     Debug.Print("       Property Value : " & Cutlist.GetCustomPropertyValue2(vPropNames(J), nType, nLink))
                     Debug.Print("       Type : " & nType)
                     Debug.Print("       Link : " & nLink)
                 Next
             End If
             Debug.Print("_________________________")

         Next

         Cutlist = vCutListItems(0)
         Debug.Print("ADD CUSTOM PROPERTY CALLED Testing1")
         Debug.Print("   Custom Property added? " & Cutlist.AddCustomProperty("Testing1", SwDmCustomInfoType.swDmCustomInfoText,  "Verify1"))
         Debug.Print("   GET CUSTOM PROPERTIES")

         vPropNames = Cutlist.GetCustomPropertyNames

         For J = 0 To UBound(vPropNames)
             Debug.Print("   Property Name : " & vPropNames(J))
             Debug.Print("       Property Value : " & Cutlist.GetCustomPropertyValue2(vPropNames(J), nType, nLink))
             Debug.Print("       Type : " & nType)
             Debug.Print("       Link : " & nLink)
         Next

         Debug.Print("_________________________")
         Debug.Print("SET NEW CUSTOM PROPERTY VALUE FOR Testing1")
         Debug.Print("       Property Value Before Setting: " & Cutlist.GetCustomPropertyValue2("Testing1", nType, nLink))
         Debug.Print("       New Value Set? " & Cutlist.SetCustomProperty("Testing1", "Verify3"))
         Debug.Print("       Property Value After Setting : " & Cutlist.GetCustomPropertyValue2("Testing1", nType, nLink))
         Debug.Print("   GET CUSTOM PROPERTIES")

         vPropNames = Cutlist.GetCustomPropertyNames

         For J = 0 To UBound(vPropNames)
             Debug.Print("   Property Name : " & vPropNames(J))
             Debug.Print("       Property Value : " & Cutlist.GetCustomPropertyValue2(vPropNames(J), nType, nLink))
             Debug.Print("       Type : " & nType)
             Debug.Print("       Link : " & nLink)
         Next

         Debug.Print("_________________________")
         Debug.Print("DELETE CUSTOM PROPERTY Testing1")
         Debug.Print("       Delete Property Value? " & Cutlist.DeleteCustomProperty("Testing1"))

         vPropNames = Cutlist.GetCustomPropertyNames
         If Not (IsNothing(vPropNames)) Then
             Debug.Print("   GET CUSTOM PROPERTIES")
             For J = 0 To UBound(vPropNames)
                 Debug.Print("   Property Name : " & vPropNames(J))
                 Debug.Print("       Property Value : " & Cutlist.GetCustomPropertyValue2(vPropNames(J), nType, nLink))
                 Debug.Print("       Type : " & nType)
                 Debug.Print("       Link : " & nLink)
             Next
         End If

         Debug.Print("_________________________")

         'swDocument10.Save()
         swDocument10.CloseDoc()

     End Sub
 End Module
```
