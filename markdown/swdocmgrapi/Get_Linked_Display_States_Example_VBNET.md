---
title: "Get Linked Display States Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Linked_Display_States_Example_VBNET.htm"
---

# Get Linked Display States Example (VB.NET)

This example gets an assembly and reports on its active configuration and display states.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the
 '    required DLLs are registered.
 ' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
 ' 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 '    interop assembly is loaded in the project.
 '    (right-click the project in Project Explorer, click
 '    Add Reference, click the interop assembly in the
 '    .NET tab, or browse for the DLL in
 '    install_dir\api\redist).
 ' 4. Substitute your license key for your_license_key in
 '    the code.
 ' 5. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate Window for output.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro

    Sub main()
        Dim swCf As SwDMClassFactory
        swCf = New SwDMClassFactory
        Dim swDocMgr As SwDMApplication

        swDocMgr = swCf.GetApplication("your_license_key")

        Dim i As Integer, j As Integer
        Dim swDoc12 As SwDMDocument14
        Dim res As SwDmDocumentOpenError
        Dim dt As SwDmDocumentType
        dt = SwDmDocumentType.swDmDocumentAssembly
        Dim filename As String
        Debug.Print("Opening an assembly...")
        filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\motor casing.sldasm"
        swDoc12 = swDocMgr.GetDocument(filename, dt, False, res)
        If swDoc12 Is Nothing Or (res <> SwDmDocumentOpenError.swDmDocumentOpenErrorNone) Then
            Debug.Print("Error opening file....")
            Exit Sub
        End If
        Dim activeConfig As SwDMConfiguration12
        Dim activeConfigName As String
        Dim configMgr As SwDMConfigurationMgr
        configMgr = swDoc12.ConfigurationManager
        activeConfigName = configMgr.GetActiveConfigurationName
        Debug.Print("Getting the active configuration: " & activeConfigName)
        activeConfig = configMgr.GetConfigurationByName(activeConfigName)
        If activeConfig Is Nothing Then
            Debug.Print("Error getting the active configuration...")
            Exit Sub
        End If
        Debug.Print("ID of " & activeConfig.Name2 & ": " & activeConfig.GetID)
        Debug.Print("")
        Dim numLinkedDisplayStates As Integer
        Dim ldsVariant As Object
        Dim lds As String
        Dim compVisibleList As Object
        Dim compFileDirectory As Object
        ldsVariant = Nothing
        numLinkedDisplayStates = activeConfig.GetLinkedDisplayStates(ldsVariant)
        Debug.Print("Number of linked display states of " & activeConfigName & ": " & numLinkedDisplayStates)
        ' Getting all the components for one linked display state
        compVisibleList = Nothing
        compFileDirectory = Nothing
        lds = ldsVariant(0)
        activeConfig.GetComponentVisibleByDisplayStateName(lds, compVisibleList, compFileDirectory)
        Debug.Print("")
        Debug.Print("Getting the paths and file names of all of the components in the linked display state, " & lds & ": ")
        Debug.Print("")
        For j = 0 To UBound(compFileDirectory)
            Debug.Print("Component: " & compFileDirectory(j))
            Debug.Print("  Is visible? " & compVisibleList(j))
        Next 'component
        'Getting all the components in the configuration
        Debug.Print("")
        Debug.Print("Getting the names of all of the components in the FeatureManager design tree for " & activeConfig.Name2 & ": ")
        Debug.Print("")
        Dim vComponents As Object
        vComponents = activeConfig.GetComponents
        If Not (IsNothing(vComponents)) Then
            Dim swDmComponent As SwDMComponent11
            For i = 0 To UBound(vComponents)
                swDmComponent = vComponents(i)
                Debug.Print("  Component name: " & swDmComponent.Name3)
                Debug.Print("     For a selective open with OpenDoc7, use: " & swDmComponent.SelectName2)
            Next 'component
        End If
        swDoc12.CloseDoc()
    End Sub

    Public swApp As SldWorks
End Class
```
