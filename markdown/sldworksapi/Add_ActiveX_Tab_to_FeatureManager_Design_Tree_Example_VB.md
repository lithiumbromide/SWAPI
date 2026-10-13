---
title: "Add ActiveX Tab to FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VB.htm"
---

# Add ActiveX Tab to FeatureManager Design Tree Example (VBA)

This example shows how to add a tab to the FeatureManager design tree using three on-disk bitmap files for the tab's scaleable icon.

```
'----------------------------------------------------------
```

```
' Preconditions:
' 1. In the IDE, reference the ActiveX control file
'    a. Click Tools > References > Browse.
'    b. Browse to c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SldUtils.
'    c. Select RichEditCtrl.ocx.
'    d. Click Open.
'    e. Click OK.
' 2. Insert the ActiveX component
'    Click Insert > Components > RichEditCtrl ActiveX Control module > OK.
' 3. Verify that the specified part document exists.
' 4. Modify the paths in bitmapnames to reference your tab icon's bitmap files in three sizes.
' 5. Review the ActiveX control reference and ensure that the ctrlBtm declaration is correct.
' 6. Search for RichEditCtrl.ocx in the registry and ensure that the second
'    argument of the CreateFeatureMgrControl4 call is correct.
'
' Postconditions:
' 1. Opens the part document and adds a new tab
'    to the FeatureManager design tree with an icon that uses the bitmap size that
'    fits the screen resolution.
'    NOTE: To add a tab to the FeatureManager tree,
'    you must set IModelViewManager::CreateFeatureMgrControl4's
'    WhichPane parameter to swFeatMgrPane_e.swFeatMgrPaneBottom.
' 2. Activates the new tab and displays the ActiveX control.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
```

```
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModViewMgr As SldWorks.ModelViewManager
    Dim swFeatMgrTabBtm As SldWorks.FeatMgrView
    Dim ctrlBtm As RICHEDITCTRLLib.RichEditCtrl
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim activePane As Long
    Dim bitmapnames(2) As String
```

```
     Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModViewMgr = swModel.ModelViewManager

    bitmapnames(0) = "C:\Users\J4M\Desktop\icons\mainicon_20.png"
    bitmapnames(1) = "C:\Users\J4M\Desktop\icons\mainicon_32.png"
    bitmapnames(2) = "C:\Users\J4M\Desktop\icons\mainicon_40.png"
```

```
    ' Create and activate the new tab
    Set swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl4(bitmapnames, "GTSWRICHEDITCTRL.RichEditCtrlCtrl.1", "", "Tab ToolTip", swFeatMgrPaneBottom)
    Set ctrlBtm = swFeatMgrTabBtm.GetControl
    activePane = swFeatMgrTabBtm.ActivateView
```

```
End Sub
```
