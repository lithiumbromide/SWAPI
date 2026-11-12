---
title: "ModelDoc::IsActive"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsActive.htm"
---

# ModelDoc::IsActive

This method is obsolete and has been superseded by [ModelDoc2::IsActive](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsActive.htm).

Description

This method determines if the specified assembly component is displayed; this is, the show and hide functionality associated with assembly components.

Syntax (OLE Automation)

retval = ModelDoc.IsActive ( compStr)

| Input: | (BSTR) compStr | Name specification of the component |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if model is shown, FALSE if model is hidden |

Syntax (COM)

status = ModelDoc->IsActive ( compStr, &retval )

| Input: | (BSTR) compStr | Name specification of the component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if model is shown, FALSE if model is hidden |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The compStr parameter is the full assembly component name designation. The format of the name designation is:

parentModel/childModel

where the child model is the model you wish to determine the display status. For example, if you want to determine the display status of a part named SPOKE.SLDPRT and if this part was a child of WHEEL.SLDPRT, which itself is a child of AXIS.SLDPRT, then you would specify compStr as follows:

AXIS/WHEEL/SPOKE

TIP: The assembly component name designation is shown in the lower-eft hand corner of the SolidWorks application when an assembly component is selected.
