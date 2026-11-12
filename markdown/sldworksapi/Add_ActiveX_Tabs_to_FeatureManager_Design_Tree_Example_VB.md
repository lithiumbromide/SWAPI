---
title: "Add ActiveX Tabs to FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm"
---

# Add ActiveX Tabs to FeatureManager Design Tree Example (VBA)

This example shows how to add tabs to a split FeatureManager design tree using an on-disk bitmap file for the tabs' icon.

```
'----------------------------------------------------------
' Preconditions:
' 1. In the IDE:
'    a. Reference your ActiveX control file (click Tools >
'       References > Browse > browse to the folder where the
'       ActiveX control file resides and click the ActiveX
'       control file > Open > OK).
'    a. Insert the ActiveX component (click Insert > Components >
'       ActiveX component's check box > OK).
' 2. Verify that the specified part document and bitmap exist.
' 3. Replace activex_control_component_declaration and
'    activex_control_CLSID_or_ProgID with your ActiveX control's
'    information.
'
' Postconditions:
' 1. Opens the part document and splits the FeatureManager
'    design tree.
' 2. Adds a new tab to each FeatureManager design tree.
' 3. Activates the new tab on the top FeatureManager design tree.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'----------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Const iconSmall As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\button.bmp"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModViewMgr As SldWorks.ModelViewManager
    Dim swFeatMgrTabTop As SldWorks.FeatMgrView
    Dim swFeatMgrTabBtm As SldWorks.FeatMgrView
    Dim ctrlTop As activex_control_component_declaration
    Dim ctrlBtm As activex_control_component_declaration
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim activePane As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Set swModViewMgr = swModel.ModelViewManager
```

```
    ' Split the FeatureManager design tree;
    ' the original is displayed below the copy
    swModel.FeatureManagerSplitterPosition = 0.5
```

```
    ' New tab on copy of FeatureManager design tree
    Set swFeatMgrTabTop = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Top tab ToolTip", swFeatMgrPaneTop)
    Set ctrlTop = swFeatMgrTabTop.GetControl
```

```
    ' New tab on original FeatureManager design tree
    Set swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Bottom tab ToolTip", swFeatMgrPaneBottom)
    Set ctrlBtm = swFeatMgrTabBtm.GetControl
    activePane = swFeatMgrTabTop.ActivateView
```

```
End Sub
```
