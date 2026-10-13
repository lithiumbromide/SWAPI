---
title: "Get Display State Settings Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Settings_VBNET.htm"
---

# Get Display State Settings Example (VB.NET)

This example shows how to get display modes, transparency states, and visibility states of components.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions: Open an assembly that contains a minimum of three top-level
 ' components and two display states, "DS_1" and "DS_2".
 '
 ' Postconditions: Inspect the Immediate Window for the display modes,
 ' transparency states, and visibility states of all three components
 ' in both DS_1 and DS_2.
 '-----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Diagnostics

 Partial Public Class SolidWorksMacro
     Private swDoc As ModelDoc2 = Nothing
     Private swExt As ModelDocExtension = Nothing
     Private swDSS As DisplayStateSetting = Nothing
     Private varStatus As Object
     Private varTStatus As Object
     Private varVStatus As Object
     Private statusArray As Array
     Private statusTArray As Array
     Private statusVArray As Array
     Const maxEntMode As Integer = 3

     Public Sub Main()
         swDoc = DirectCast(swApp.ActiveDoc, ModelDoc2)
         swExt = swDoc.Extension
         Dim docType As Integer = swDoc.[GetType]()
         If docType = CInt(swDocumentTypes_e.swDocASSEMBLY) Then

             CreateDisplayStateSetting()

             varStatus = swExt.DisplayMode(swDSS)
             statusArray = DirectCast(varStatus, Array)

             varTStatus = swExt.Transparency(swDSS)
             statusTArray = DirectCast(varTStatus, Array)

             varVStatus = swExt.Visibility(swDSS)
             statusVArray = DirectCast(varVStatus, Array)

             WriteOutput()

         End If
     End Sub

     Public Sub CreateDisplayStateSetting()
         swDSS = swExt.GetDisplayStateSetting(CInt(swDisplayStateOpts_e.swThisDisplayState))
         swDSS.Option = CInt(swDisplayStateOpts_e.swSpecifyDisplayState)

         Dim specDSNames As String() = New  String(1) {}
         specDSNames(0) = "DS_1"
         specDSNames(1) =  "DS_2"
         Dim varSpecDSNames As Object = specDSNames
         swDSS.Names = varSpecDSNames

         Dim swADoc As AssemblyDoc
         swADoc = DirectCast(swDoc, AssemblyDoc)
         Dim compCnt As Integer = swADoc.GetComponentCount(True)
         Dim listComp As Component2() = New Component2(maxEntMode - 1) {}
         If compCnt >= maxEntMode Then
             Dim varComp As Object() = DirectCast(swADoc.GetComponents(True), Object())
             listComp(0) = DirectCast(varComp(0), Component2)
             listComp(1) = DirectCast(varComp(1), Component2)
             listComp(2) = DirectCast(varComp(2), Component2)
             swDSS.Entities = listComp
         End If

     End Sub

     Public Sub WriteOutput()
         Dim entCount As Integer = swDSS.GetEntityCount()
         Dim listComp As Object() = DirectCast(swDSS.Entities, Object())
         Dim allCtr As Integer = 0
         For entctr As Integer = 0 To entCount - 1
             Dim swComp As Component2 = DirectCast(listComp(entctr), Component2)
             Debug.Print(swComp.Name2)
             Dim dsNameCount As Integer = swDSS.GetNameCount()
             Dim dsNames As Object() = DirectCast(swDSS.Names, Object())

             For namectr As Integer = 0 To dsNameCount - 1
                 Debug.Print("   " & DirectCast(dsNames(namectr), String))
                 Dim status As Integer = CInt(statusArray.GetValue(allCtr))
                 Dim statusT As Integer = CInt(statusTArray.GetValue(allCtr))
                 Dim statusV As Integer = CInt(statusVArray.GetValue(allCtr))
                 WriteMode(status)
                 WriteTransparency(statusT)
                 WriteVisibility(statusV)
                 allCtr += 1
             Next
         Next
     End Sub
     Public Sub WriteMode(ByVal status As Integer)
         Select Case status
             Case CInt(swDisplayMode_e.swDisplayModeDEFAULT)
                 Debug.Print("       swDisplayModeDEFAULT")
                 Exit Select
             Case CInt(swDisplayMode_e.swHIDDEN)
                 Debug.Print("       swHIDDEN")
                 Exit Select
             Case CInt(swDisplayMode_e.swHIDDEN_GREYED)
                 Debug.Print("       swHIDDEN_GREYED")
                 Exit Select
             Case CInt(swDisplayMode_e.swSHADED)
                 Debug.Print("       swSHADED")
                 Exit Select
             Case CInt(swDisplayMode_e.swSHADED_EDGES)
                 Debug.Print("       swSHADED_EDGES")
                 Exit Select
             Case CInt(swDisplayMode_e.swWIREFRAME)
                 Debug.Print("       swWIREFRAME")
                 Exit Select
             Case CInt(swDisplayMode_e.swDisplayModeUNKNOWN)
                 Debug.Print("       Error:swDisplayModeUNKNOWN")
                 Exit Select
            Case CInt(swDisplayMode_e.swFACETED_WIREFRAME)
                 Debug.Print ("       swFACETED_WIREFRAME")
                 Exit Select
            Case CInt(swDisplayMode_e.swFACETED_HIDDEN_GREYED)
                 Debug.Print ("       swFACETED_HIDDEN_GREYED")
                 Exit Select
            Case CInt(swDisplayMode_e.swFACETED_HIDDEN)
                 Debug.Print ("       swFACETED_HIDDEN")
                 Exit Select
         End Select
     End Sub
     Public Sub WriteTransparency(ByVal status As Integer)
         Select Case status
             Case CInt(swTransparencyState_e.swTransparencyStateTransparent)
                 Debug.Print("       swTransparencyStateTransparent")
                 Exit Select
             Case CInt(swTransparencyState_e.swTransparencyStateNonTransparent)
                 Debug.Print("       swTransparencyStateNonTransparent")
                 Exit Select
             Case CInt(swTransparencyState_e.swTransparencyStateUnknown)
                 Debug.Print("       ERROR : swTransparencyStateUnknown")
                 Exit Select
         End Select
     End Sub
     Public Sub WriteVisibility(ByVal status As Integer)
         Select Case status
             Case CInt(swVisibilityState_e.swVisibilityStateHide)
                 Debug.Print("       swVisibilityStateHide")
                 Exit Select
             Case CInt(swVisibilityState_e.swVisibilityStateShown)
                 Debug.Print("       swVisibilityStateShown")
                 Exit Select
             Case CInt(swVisibilityState_e.swVisibilityStateUnknown)
                 Debug.Print("       ERROR : swVisibilityStateUnknown")
                 Exit Select
         End Select
     End Sub

     Public swApp As SldWorks
 End  Class
```
