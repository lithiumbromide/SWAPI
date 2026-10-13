---
title: "Get Display State Settings Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Settings_Example_VB.htm"
---

# Get Display State Settings Example (VBA)

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
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swExt As SldWorks.ModelDocExtension
 Dim swDSS As SldWorks.DisplayStateSetting
 Dim varStatus As Variant
 Dim varTStatus As Variant
 Dim varVStatus As Variant
 Dim statusArray(5) As Long
 Dim statusTArray(5) As Long
 Dim statusVArray(5) As Long
 Dim varComp As Object
 Dim varDS As Object
 Dim returnCode As Boolean
 Const maxEntMode As Integer = 3
 Public Sub Main()
     Set swApp = Application.SldWorks
     Set swDoc = swApp.ActiveDoc
     Set swExt = swDoc.Extension
     Dim docType As Integer
     docType = swDoc.GetType
     If docType = swDocumentTypes_e.swDocASSEMBLY Then
```

```vb
    Set swDSS = swExt.GetDisplayStateSetting(swDisplayStateOpts_e.swThisDisplayState)
    swDSS.Option = swDisplayStateOpts_e.swSpecifyDisplayState
    Dim specDSNames(1) As String
    specDSNames(0) = "DS_1"
    specDSNames(1) = "DS_2"
    Dim varSpecDSNames As Variant
    varSpecDSNames = specDSNames
    swDSS.Names = varSpecDSNames
    Dim swADoc As AssemblyDoc
    Set swADoc = swDoc
    Dim compCnt As Integer
    compCnt = swADoc.GetComponentCount(True)
    Dim listComp(maxEntMode - 1) As Component2
    If compCnt >= maxEntMode Then
        Dim varComp As Variant
        varComp = swADoc.GetComponents(True)
        Set listComp(0) = varComp(0)
        Set listComp(1) = varComp(1)
        Set listComp(2) = varComp(2)
        swDSS.Entities = listComp
    End If
```

```vb
         varStatus = swExt.DisplayMode(swDSS)
         statusArray(0) = varStatus(0)
         statusArray(1) = varStatus(1)
         statusArray(2) = varStatus(2)
         statusArray(3) = varStatus(3)
         statusArray(4) = varStatus(4)
         statusArray(5) = varStatus(5)

         varTStatus = swExt.Transparency(swDSS)
         statusTArray(0) = varTStatus(0)
         statusTArray(1) = varTStatus(1)
         statusTArray(2) = varTStatus(2)
         statusTArray(3) = varTStatus(3)
         statusTArray(4) = varTStatus(4)
         statusTArray(5) = varTStatus(5)

        varVStatus = swExt.Visibility(swDSS)
         statusVArray(0) = varVStatus(0)
         statusVArray(1) = varVStatus(1)
         statusVArray(2) = varVStatus(2)
         statusVArray(3) = varVStatus(3)
         statusVArray(4) = varVStatus(4)
         statusVArray(5) = varVStatus(5)

         WriteOutput

    End If
 End Sub

 Public Sub WriteOutput()
     Dim entCount As Integer
     entCount = swDSS.GetEntityCount
     Dim listComp() As Component2
     listComp = swDSS.Entities
     Dim allCtr As Integer
     allCtr = 0
     Dim entctr As Long
     For entctr = 0 To entCount - 1
         Dim swComp As Component2
         Set swComp = listComp(entctr)
         Debug.Print (swComp.Name2)
         Dim dsNameCount As Integer
         dsNameCount = swDSS.GetNameCount()
         Dim dsNames() As String
         dsNames = swDSS.Names
         Dim namectr As Long
         For namectr = 0 To dsNameCount - 1
             Debug.Print ("   " & dsNames(namectr))
             Dim status As Integer
             status = statusArray(allCtr)
             Dim statusT As Integer
             statusT = statusTArray(allCtr)
             Dim statusV As Integer
             statusV = statusVArray(allCtr)
             WriteMode (status)
             WriteTransparency (statusT)
             WriteVisibility (statusV)
             allCtr = allCtr + 1
         Next
     Next
 End Sub
 Public Sub WriteMode(ByVal status As Integer)
     Select Case status
         Case CInt(swDisplayMode_e.swDisplayModeDEFAULT)
             Debug.Print ("       swDisplayModeDEFAULT")

        Case CInt(swDisplayMode_e.swHIDDEN)
             Debug.Print ("       swHIDDEN")

        Case CInt(swDisplayMode_e.swHIDDEN_GREYED)
             Debug.Print ("       swHIDDEN_GREYED")

        Case CInt(swDisplayMode_e.swSHADED)
             Debug.Print ("       swSHADED")

        Case CInt(swDisplayMode_e.swSHADED_EDGES)
             Debug.Print ("       swSHADED_EDGES")

        Case CInt(swDisplayMode_e.swWIREFRAME)
             Debug.Print ("       swWIREFRAME")

        Case CInt(swDisplayMode_e.swDisplayModeUNKNOWN)
             Debug.Print ("       Error:swDisplayModeUNKNOWN")
        Case CInt(swDisplayMode_e.swFACETED_WIREFRAME)
             Debug.Print ("       swFACETED_WIREFRAME")
        Case CInt(swDisplayMode_e.swFACETED_HIDDEN_GREYED)
             Debug.Print ("       swFACETED_HIDDEN_GREYED")
        Case CInt(swDisplayMode_e.swFACETED_HIDDEN)
             Debug.Print ("       swFACETED_HIDDEN")

    End Select
 End Sub
 Public Sub WriteTransparency(ByVal status As Integer)
     Select Case status
         Case CInt(swTransparencyState_e.swTransparencyStateTransparent)
             Debug.Print ("       swTransparencyStateTransparent")

        Case CInt(swTransparencyState_e.swTransparencyStateNonTransparent)
             Debug.Print ("       swTransparencyStateNonTransparent")

        Case CInt(swTransparencyState_e.swTransparencyStateUnknown)
             Debug.Print ("       ERROR : swTransparencyStateUnknown")

    End Select
 End Sub
 Public Sub WriteVisibility(ByVal status As Integer)
     Select Case status
         Case CInt(swVisibilityState_e.swVisibilityStateHide)
             Debug.Print ("       swVisibilityStateHide")

        Case CInt(swVisibilityState_e.swVisibilityStateShown)
             Debug.Print ("       swVisibilityStateShown")

        Case CInt(swVisibilityState_e.swVisibilityStateUnknown)
             Debug.Print ("       ERROR : swVisibilityStateUnknown")

    End Select
 End Sub
```
