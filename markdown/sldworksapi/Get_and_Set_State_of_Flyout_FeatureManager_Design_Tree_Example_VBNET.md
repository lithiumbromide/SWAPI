---
title: "Get and Set the State of the Flyout FeatureManager Design Tree Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_VBNET.htm"
---

# Get and Set the State of the Flyout FeatureManager Design Tree Example (VB.NET)

This example shows how to display, expand, and hide the flyout FeatureManager design tree.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Click OK to close each of the three message boxes after examining the
'    graphics area.
' 2. Examine the Immediate window.
' ---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim status As Integer

    Public Sub Main()

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        status = swModelDocExt.FlyoutFeatureTreeVisibility

        Debug.Print("-------Flyout state at start-------")
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_Hidden Then Debug.Print("FlyoutFeatureTree Hidden")
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded Then Debug.Print("FlyoutFeatureTree Expanded")
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded Then Debug.Print("FlyoutFeatureTree UnExpanded")

        swModelDocExt.FlyoutFeatureTreeVisibility = swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded
        status = swModelDocExt.FlyoutFeatureTreeVisibility
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded Then MsgBox("Flyout state is now swFlyoutFeatureTree_ShownExpanded.")

        swModelDocExt.FlyoutFeatureTreeVisibility = swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded
        status = swModelDocExt.FlyoutFeatureTreeVisibility
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded Then MsgBox("Flyout state is now swFlyoutFeatureTree_ShownUnExpanded.")

        swModelDocExt.FlyoutFeatureTreeVisibility = swFeatureTreeState_e.swFlyoutFeatureTree_Hidden
        status = swModelDocExt.FlyoutFeatureTreeVisibility
        If status = swFeatureTreeState_e.swFlyoutFeatureTree_Hidden Then MsgBox("Flyout state is now swFlyoutFeatureTree_Hidden.")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
