---
title: "Remove Material Properties from Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Material_From_Bodies_Example_VBNET.htm"
---

# Remove Material Properties from Bodies Example (VB.NET)

This example shows how to remove materials from bodies in a multibody part. This example also works with a part with a single body and an assembly with single and multibody components.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
' 2. Expand Solid Bodies(2) > right-click Extrude-Thin1 > click
'    Appearances > Body > any color in Appearances(color) > OK.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree.
' 2. Removes the color that you applied to Extrude-Thin1.
' 3. Examine the Immediate window and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swPart As PartDoc
    Dim vBody As Object
    Dim bRet As Boolean

    Public Sub main()

        Dim j As Integer

        swModel = swApp.ActiveDoc
        swModel.ClearSelection2(True)
        Debug.Print("File = " & swModel.GetPathName)
        Select Case swModel.GetType
            Case swDocumentTypes_e.swDocPART
                swPart = swModel
                ' Solid bodies
                Dim vBodyArr() As Object
                Dim swBody As Body2
                vBodyArr = swPart.GetBodies2(swBodyType_e.swSolidBody, True)
                If Not IsNothing(vBodyArr) Then
                    Debug.Print("  Number of solid bodies: " & UBound(vBodyArr) + 1)
                    Debug.Print("    Material removed from: ")
                    j = 1
                    For Each vBody In vBodyArr
                        swBody = vBody
                        Dim vConfigName() As Object
                        vConfigName = swModel.GetConfigurationNames
                        bRet = swBody.RemoveMaterialProperty(swInConfigurationOpts_e.swAllConfiguration, (vConfigName))
                        Debug.Print("      Body " & j & "? " & bRet)
                        j = j + 1
                    Next
                End If
            Case swDocumentTypes_e.swDocASSEMBLY
                ProcessAssembly(swApp, swModel)
            Case Else
                Exit Sub
        End Select

    End Sub

    Sub ProcessAssembly(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2)
        Dim swConfigMgr As ConfigurationManager
        Dim swConf As Configuration
        Dim swRootComp As Component2

        swConfigMgr = swModel.ConfigurationManager
        swConf = swConfigMgr.ActiveConfiguration
        swRootComp = swConf.GetRootComponent3(True)
        ProcessComponent(swApp, swModel, swRootComp)

    End Sub

    Sub ProcessComponent(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swComp As Component2)
        Dim vChildComp() As Object
        Dim swChildComp As Component2 = Nothing
        Dim childComp As Object

        Debug.Print(swComp.Name2 & " <" & swComp.ReferencedConfiguration & ">")
        ' Solid bodies
        Dim vBodyArr() As Object
        Dim swBody As Body2
        vBodyArr = swComp.GetBodies2(swBodyType_e.swSolidBody)
        If Not IsNothing(vBodyArr) Then
            Debug.Print("       Number of bodies: " & UBound(vBodyArr) + 1)
            For Each vBody In vBodyArr
                swBody = vBody
                Dim vConfigName() As Object
                Debug.Print("         Body name: " & swBody.Name)
                vConfigName = swModel.GetConfigurationNames
                bRet = swBody.RemoveMaterialProperty(swInConfigurationOpts_e.swThisConfiguration, (vConfigName))
                Debug.Print("           Material removed from body? " & bRet)
            Next
        End If
        vChildComp = swComp.GetChildren
        For Each childComp In vChildComp
            swChildComp = childComp
            ProcessComponent(swApp, swModel, swChildComp)
        Next
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
