---
title: "Add ActiveX Tabs to FeatureManager Design Tree Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm"
---

# Add ActiveX Tabs to FeatureManager Design Tree Example (VB.NET)

This example shows how to add tabs to a split FeatureManager design tree using an on-disk bitmap file for the tabs' icons.

```vb
 '----------------------------------------------------------
 ' Preconditions:
 ' 1. In the IDE, reference your ActiveX control file
 '    (click Project > Add Reference > Browse and browse
 '    to the folder where the ActiveX control resides and click
 '    the ActiveX control file > OK).
 ' 2. Verify that the specified part document and bitmap exist.
 ' 3. Replace activex_control_component_declaration and
 '    activex_control_CLSID_or_ProgID with your ActiveX control's
 '    information.
 '
 ' Postconditions:
 ' 1. Opens the part document and splits the FeatureManager
 '    design tree.
 ' 2. Adds a new tab to each FeatureManager design tree.
 ' 3. Activates the new tab on the top of the FeatureManager
 '    design tree.

 ' NOTE: Because the part document is used elsewhere,
 ' do not save changes.
 '----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Const iconSmall As  String =  "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\button.bmp"

         Dim swModel As ModelDoc2
         Dim swModViewMgr As ModelViewManager
         Dim swFeatMgrTabTop As FeatMgrView
         Dim swFeatMgrTabBtm As FeatMgrView
         Dim ctrlTop  As  activex_control_component_declaration
         Dim ctrlBtm  As  activex_control_component_declaration
         Dim fileName  As  String
         Dim errors As  Integer
         Dim warnings As  Integer
         Dim activePane As  Integer

         fileName =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent,  "", errors, warnings)

         swModViewMgr = swModel.ModelViewManager

        ' Split the FeatureManager design tree;
         ' the original is displayed below the copy
         swModel.FeatureManagerSplitterPosition = 0.5

         ' New tab on original of FeatureManager design tree
         swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID",  "",  "Bottom tab ToolTip", swFeatMgrPane_e.swFeatMgrPaneBottom)
         ctrlBtm = swFeatMgrTabBtm.GetControl

        ' New tab on copy of FeatureManager design tree
         swFeatMgrTabTop = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID",  "",  "Top tab ToolTip", swFeatMgrPane_e.swFeatMgrPaneBottom)
         ctrlTop = swFeatMgrTabTop.GetControl
         activePane = swFeatMgrTabTop.ActivateView

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
