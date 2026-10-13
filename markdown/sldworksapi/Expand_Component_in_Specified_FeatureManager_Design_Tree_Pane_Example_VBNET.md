---
title: "Expand Component in Specified FeatureManager Design Tree Pane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VBNET.htm"
---

# Expand Component in Specified FeatureManager Design Tree Pane Example (VB.NET)

This example shows how to expand a component in the specified FeatureManager design tree pane.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
' 2. Select speaker_frame<1> in the FeatureManager design
'    tree.
'
' Postconditions:
' 1. Expands the selected component in the top pane of the
'    FeatureManager design tree.
' 2. Examine the top pane of the FeatureManager design tree
'    and the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not
' save changes.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssy As AssemblyDoc
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swComp As Component2
        Dim swFeatMgr As FeatureManager
        Dim featName As String
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swAssy = swModel
        swSelMgr = swModel.SelectionManager
        swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
        swFeat = swAssy.FeatureByName("speaker_frame-1")
        swFeat = swComp.FeatureByName("Cut-Extrude1")
        featName = swFeat.Name
        swFeatMgr = swModel.FeatureManager
        status = swFeatMgr.ExpandFeature(swComp, featName, swFeatMgrPane_e.swFeatMgrPaneTop)
        Debug.Print("Selected component expanded in top pane of FeatureManager design tree? " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
