---
title: "ModelDoc::GetUpdateStamp"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUpdateStamp.htm"
---

# ModelDoc::GetUpdateStamp

This method is obsolete and has been superseded by [ModelDoc2::GetUpdateStamp](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUpdateStamp.htm).

Description

This method returns the current update stamp for this document.

Syntax (OLE Automation)

retval = ModelDoc.GetUpdateStamp ()

| Return: | (long) retval | Current update stamp value for this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetUpdateStamp ( &retval )

| Output: | (long) retval | Current update stamp value for this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The update stamp is essentially an integer form of a time stamp. The update stamp is incremented for model state changes (for example, suppressing or unsuppressing features in a model, configuration changes, feature changes, and so on) and for geometric changes (for example, anything that requires a rebuild). This time stamp is not incremented for operations such as color changes, feature or configuration name changes, and so on.
