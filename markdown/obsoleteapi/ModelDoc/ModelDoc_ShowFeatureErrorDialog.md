---
title: "ModelDoc::ShowFeatureErrorDialog"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_ShowFeatureErrorDialog.htm"
---

# ModelDoc::ShowFeatureErrorDialog

This property is obsolete and has been superseded by [ModelDoc2::ShowFeatureErrorDialog](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowFeatureErrorDialog.htm).

Description

During feature creation operations, this property gets or sets whether an error dialog is displayed.

Syntax (OLE Automation)

dialogState = ModelDoc. ShowFeatureErrorDialog (VB Get property)

ModelDoc. ShowFeatureErrorDialog = dialogState (VB Set property)

dialogState = ModelDoc.GetShowFeatureErrorDialog ( ) (C++ Get property)

ModelDoc.SetShowFeatureErrorDialog (dialogState) (C++ Set property)

| Property: | (BOOL) dialogState | True if error dialogs will be displayed during feature creation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->get_ShowFeatureErrorDialog ( &dialogState)

status = ModelDoc->put_ShowFeatureErrorDialog (dialogState)

| Output: | (BOOL) retval | True if error dialogs will be displayed during feature creation |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Currently, this property only handles errors for the rebuild error dialog.

It is your responsibility to reset this value to the SolidWorks default (TRUE), when your are finished.

To obtain the specific error value associated with a feature, use Feature::GetErrorCode.
