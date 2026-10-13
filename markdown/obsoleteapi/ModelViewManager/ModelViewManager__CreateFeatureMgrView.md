---
title: "ModelViewManager::CreateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelViewManager/ModelViewManager__CreateFeatureMgrView.htm"
---

# ModelViewManager::CreateFeatureMgrView

This method is obsolete and has been superseded by [ModelViewManager::CreateFeatureMgrView2](sldworksAPI.chm::/ModelViewManager/ModelViewManager__CreateFeatureMgrView2.htm).

Description

This method creates a new tab on this FeatureManager design tree view.

Syntax (OLE Automation)

retval = ModelViewManager.CreateFeatureMgrView ( pPicture, toolTip, whichPane )

| Input: | (LPDISPATCH) pPicture | Pointer to the bitmap that you want to use for the tab |
| --- | --- | --- |
| Input: | (BSTR) toolTip | Text for the ToolTip |
| Input: | (long) whichPane | Pane to use as defined in swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the new tab |

Syntax (COM)

status = ModelViewManager->CreateFeatureMgrView ( pPicture, toolTip, whichPane, &retval )

| Input: | (LPDISPATCH) pPicture | Pointer to the bitmap that you want to use for the tab |
| --- | --- | --- |
| Input: | (BSTR) toolTip | Text for the ToolTip |
| Input: | (long) whichPane | Pane to use as defined in swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the new tab |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
