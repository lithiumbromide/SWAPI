---
title: "Add ActiveX Tab to FeatureManager Design Tree Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_CSharp.htm"
---

# Add ActiveX Tab to FeatureManager Design Tree Example (C#)

This example shows how to add a tab to the FeatureManager design tree using three on-disk bitmap files for the tab's scaleable icon.

```
//----------------------------------------------------------
// Preconditions:
// 1. In the IDE, reference your ActiveX control file
//    a. Click Project > Add > Reference > Browse.
//    b. Browse to c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SldUtils.
//    c. Select RichEditCtrl.ocx.
//    d. Click OK.
// 2. Verify that the specified part document exists.
// 3. Modify the namespace to match your project name.
// 4. Modify bitmapnames to reference your icon bitmaps in three sizes.
// 5. Review the ActiveX control reference and ensure that ctrlBtm is correct.
// 6. Search for RichEditCtrl.ocx in the registry and ensure that the second
//    argument to CreateFeatureMgrControl4 is correct.
//
// Postconditions:
// 1. Opens the part document and adds a new tab to the
//    FeatureManager design tree with an icon that uses the bitmap size
//    that fits the screen resolution.
//    NOTE: To add a tab to the FeatureManager tree,
//    you must set IModelViewManager::CreateFeatureMgrControl2's
//    WhichPane parameter to swFeatMgrPane_e.swFeatMgrPaneBottom.
// 2. Activates the new tab.
//
// NOTE: Because the part document is used elsewhere,
// do not save changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

namespace AddTabFeatureManagerDesignTreeCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
```

```vb
               ModelDoc2 swModel =  default(ModelDoc2);
                ModelViewManager swModViewMgr =  default(ModelViewManager);
               FeatMgrView swFeatMgrTabBtm =  default(FeatMgrView);
                RICHEDITCTRLLib.RichEditCtrl ctrlBtm =  default(RICHEDITCTRLLib.RichEditCtrl);
               string fileName =  null;
               int errors = 0;
               int warnings = 0;
               int activePane = 0;
               string[] bitmapnames =  new  String[3];
```

```vb
                 bitmapnames[0] =  "C:\\Users\\J4M\\Desktop\\icons\\mainicon_20.png";
                 bitmapnames[1] =  "C:\\Users\\J4M\\Desktop\\icons\\mainicon_32.png";
                 bitmapnames[2] =  "C:\\Users\\J4M\\Desktop\\icons\\mainicon_40.png";
```

```vb
                 fileName =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2020\\samples\\tutorial\\fillets\\knob.sldprt";
                swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent,  "",  ref errors,  ref warnings);
                swModViewMgr = (ModelViewManager)swModel.ModelViewManager;            // Create new tab
```

```vb
              swFeatMgrTabBtm = (FeatMgrView)swModViewMgr.CreateFeatureMgrControl4(bitmapnames,  "GTSWRICHEDITCTRL.RichEditCtrlCtrl.1",  "",  "Tab ToolTip", (int)swFeatMgrPane_e.swFeatMgrPaneBottom);
                ctrlBtm = (RICHEDITCTRLLib.RichEditCtrl)swFeatMgrTabBtm.GetControl();
```

activePane = swFeatMgrTabBtm.ActivateView();

```
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
