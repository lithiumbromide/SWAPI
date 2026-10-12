---
title: "Expand Component in Specified FeatureManager Design Tree Pane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VB.htm"
---

# Expand Component in Specified FeatureManager Design Tree Pane Example (VBA)

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
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swComp As SldWorks.Component2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim featName As String
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
    Set swFeat = swAssy.FeatureByName("speaker_frame-1")
    Set swFeat = swComp.FeatureByName("Cut-Extrude1")
    featName = swFeat.Name
    Set swFeatMgr = swModel.FeatureManager
    status = swFeatMgr.ExpandFeature(swComp, featName, swFeatMgrPane_e.swFeatMgrPaneTop)
    Debug.Print "Selected component expanded in top pane of FeatureManager design tree? " & status
```

```
End Sub
```
