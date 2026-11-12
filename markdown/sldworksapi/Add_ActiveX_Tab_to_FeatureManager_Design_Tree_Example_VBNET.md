---
title: "Add ActiveX Tab to FeatureManager Design Tree Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VBNET.htm"
---

# Add ActiveX Tab to FeatureManager Design Tree Example (VB.NET)

This example shows how to add a tab to the FeatureManager design tree using three on-disk bitmap files for the tab's scaleable icon.

```
'----------------------------------------------------------
' Preconditions:
' 1. In the IDE, reference your ActiveX control file
'    a. Click Project > Add > Reference > Browse.
'    b. Browse to c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SldUtils.
'    c. Select RichEditCtrl.ocx.
'    d. Click OK.
' 2. Verify that the specified part document exists.
' 3. Modify bitmapnames to reference your icon bitmaps in three sizes.
' 4. Review the ActiveX control reference and ensure that ctrlBtm is correct.
' 5. Search for RichEditCtrl.ocx in the registry and ensure that the second
'    argument to CreateFeatureMgrControl4 is correct.
'
' Postconditions:
' 1. Opens the part document and adds a new tab to the
'    FeatureManager design tree with an icon that uses the bitmap size
'    that fits the screen resolution.
'    NOTE: To add a tab to the FeatureManager tree,
'    you must set IModelViewManager::CreateFeatureMgrControl2's
'    WhichPane parameter to swFeatMgrPane_e.swFeatMgrPaneBottom.
' 2. Activates the new tab.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModViewMgr As ModelViewManager
        Dim swFeatMgrTabBtm As FeatMgrView
        Dim ctrlBtm As RICHEDITCTRLLib.RichEditCtrl
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim activePane As Integer
        Dim BitmapFileNames(2) As String

        BitmapFileNames(0) = "C:\Users\J4M\Desktop\icons\mainicon_20.png"
        BitmapFileNames(1) = "C:\Users\J4M\Desktop\icons\mainicon_32.png"
        BitmapFileNames(2) = "C:\Users\J4M\Desktop\icons\mainicon_40.png"

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\fillets\knob.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        swModViewMgr = swModel.ModelViewManager

        ' Create new tab

        swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl4(BitmapFileNames, "GTSWRICHEDITCTRL.RichEditCtrlCtrl.1", "", "Tab ToolTip", swFeatMgrPane_e.swFeatMgrPaneBottom)
        ctrlBtm = swFeatMgrTabBtm.GetControl
        activePane = swFeatMgrTabBtm.ActivateView

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
