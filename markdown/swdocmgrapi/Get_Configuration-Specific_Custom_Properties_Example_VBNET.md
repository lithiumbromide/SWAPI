---
title: "Get Configuration-Specific Custom Properties for Components (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Configuration-Specific_Custom_Properties_Example_VBNET.htm"
---

# Get Configuration-Specific Custom Properties for Components (VB.NET)

This example shows how to get custom properties for assembly components.

'---------------------------------------------------------------------------

' Preconditions:

' 1. Read the SOLIDWORKS Document Manager API **Getting Started**

' topic and ensure that the required DLLs are registered.

' 2. Copy and paste this code into a VB.NET console application

' in Microsoft Visual Studio.

' 3. Ensure the Solution Platform is of type x64.

' 4. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:

' a. Right-click the solution in Solution Explorer.

' b. Click **Add Reference**.

' c. Click **Browse**.

' d. Click:

' `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**

' e. Click **Add**.

' f. Click **Close**.

' 5. Add the **Microsoft Scripting Runtime** reference to the project.

' 6. Ensure that the model(s) to open exists and is(are) not readonly.

' 7. Substitute `your_license_key` with your SOLIDWORKS Document

' Manager license key.

' 8. Open the Immediate window.

'

' Postconditions:

' 1. Gets document-level, component-level, and configuration-level custom properties for all assembly components.

' 2. Inspect the Immediate window.

'

'--------------------------------------------------------------------------

Imports System.Diagnostics

Imports SolidWorks.Interop.swdocumentmgr

Module Module1

Sub Main()

Dim swDocMgr As SwDMApplication

Dim swCf As SwDMClassFactory

swCf = CreateObject("SwDocumentMgr.SwDMClassFactory")

Dim sKey As String

sKey = "`your_license_key`"

swDocMgr = swCf.GetApplication(sKey)

Dim swDmSearchOpt As SwDMSearchOption

swDmSearchOpt = swDocMgr.GetSearchOptionObject

swDmSearchOpt.ClearAllSearchPaths()

swDmSearchOpt.AddSearchPath("`public_documents`\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\advdrawings")

Dim dOpenDocs As New Scripting.Dictionary

Dim swDoc12 As SwDMDocument12

Dim res As SwDmDocumentOpenError

Dim dt As SwDmDocumentType

dt = SwDmDocumentType.swDmDocumentAssembly

Dim filename As String

filename = "`public_documents`\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\advdrawings\98food processor.SLDASM"

swDoc12 = swDocMgr.GetDocument(filename, dt, False, res)

If swDoc12 Is Nothing Or (res <> SwDmDocumentOpenError.swDmDocumentOpenErrorNone) Then

Debug.Print("Error opening file...")

Exit Sub

End If

dOpenDocs.Add(filename, swDoc12)

Dim activeConfig As SwDMConfiguration8

Dim configMgr As SwDMConfigurationMgr

configMgr = swDoc12.ConfigurationManager

Dim vConfigNames As Object

vConfigNames = configMgr.GetConfigurationNames

Dim j As Integer

Debug.Print("Assembly configurations: ")

For j = 0 To UBound(vConfigNames)

Debug.Print(" " & vConfigNames(j))

Next j

Debug.Print("Get the active assembly configuration...")

Dim sActiveConfig As String

sActiveConfig = configMgr.GetActiveConfigurationName

activeConfig = configMgr.GetConfigurationByName(sActiveConfig)

If activeConfig Is Nothing Then

Debug.Print("Error getting the active assembly configuration...")

Return

End If

Debug.Print("The active assembly configuration is " & sActiveConfig)

Debug.Print("Get the components of the active assembly configuration...")

Dim vComponents As Object

vComponents = activeConfig.GetComponents

Dim swDmComponent As SwDMComponent12

Dim i As Integer

For i = 0 To UBound(vComponents)

swDmComponent = vComponents(i)

Debug.Print("")

Debug.Print("Component name = " & swDmComponent.Name3 & " Config = " & swDmComponent.ConfigurationName)

Dim swDmCompDocCur As SwDMDocument

Dim lErr As Integer

Dim bIsInDict As Boolean

bIsInDict = dOpenDocs.Exists(swDmComponent.Name)

If Not bIsInDict Then

swDmCompDocCur = swDmComponent.GetDocument2(False, swDmSearchOpt, lErr)

If Not swDmCompDocCur Is Nothing Then

dOpenDocs.Add(swDmComponent.Name, swDmCompDocCur)

End If

Else

swDmCompDocCur = dOpenDocs(swDmComponent.Name)

End If

Dim vCustomPropNamesFromDoc As Object

Dim lPropType As Integer

Dim sPropVal As String

Dim k As Integer

If swDmCompDocCur IsNot Nothing Then

Debug.Print("********* Document-level custom properties **************")

vCustomPropNamesFromDoc = swDmCompDocCur.GetCustomPropertyNames()

If vCustomPropNamesFromDoc IsNot Nothing Then

For k = 0 To UBound(vCustomPropNamesFromDoc)

sPropVal = swDmCompDocCur.**GetCustomProperty**(vCustomPropNamesFromDoc(k), lPropType)

Debug.Print(vCustomPropNamesFromDoc(k) & ": Value: " & sPropVal & ", Type: " & lPropType)

Next k

Debug.Print("********* Component-level custom properties **************")

Dim m As Integer

For m = 0 To UBound(vCustomPropNamesFromDoc)

sPropVal = swDmComponent.**GetCustomProperty**(vCustomPropNamesFromDoc(m), lPropType)

Debug.Print(vCustomPropNamesFromDoc(m) & ": Value: " & sPropVal & ", Type: " & lPropType)

Next m

Dim swDmCompDocCurConfigMgr As SwDMConfigurationMgr

swDmCompDocCurConfigMgr = swDmCompDocCur.ConfigurationManager

Dim swDmCompDocCurConfigMgr2 As SwDMConfigurationMgr2

swDmCompDocCurConfigMgr2 = swDmCompDocCurConfigMgr

Dim swDmCompConfigCur As SwDMConfiguration

Dim swDmCompConfigCur14 As SwDMConfiguration14

Dim swDmConfigErr As SwDMConfigurationError

swDmCompConfigCur = swDmCompDocCurConfigMgr2.GetConfigurationByName2(swDmComponent.ConfigurationName, swDmConfigErr)

swDmCompConfigCur14 = swDmCompConfigCur

Dim lCustPropCount As Integer

lCustPropCount = swDmCompConfigCur.GetCustomPropertyCount

Dim vCustPropNames As Object

vCustPropNames = swDmCompConfigCur.GetCustomPropertyNames

Debug.Print("********* Configuration-level custom properties **************")

If lCustPropCount > 0 Then

Dim r As Integer

For r = 0 To UBound(vCustPropNames)

sPropVal = swDmCompConfigCur.**GetCustomProperty**(vCustPropNames(r), lPropType)

Debug.Print(vCustPropNames(r) & ": " & sPropVal & ", " & lPropType)

Next r

Else

Debug.Print("None")

End If

Else

Debug.Print("None")

End If

End If

Next

Dim s As Integer

Dim swDmDocCur As SwDMDocument

For s = 0 To dOpenDocs.Count - 1

swDmDocCur = dOpenDocs.Items()(s)

swDmDocCur.CloseDoc()

swDmDocCur = Nothing

Next s

dOpenDocs.RemoveAll

dOpenDocs = Nothing

End Sub

End Module
