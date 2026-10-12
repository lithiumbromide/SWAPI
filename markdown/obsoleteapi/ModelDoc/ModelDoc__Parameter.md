---
title: "ModelDoc::Parameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Parameter.htm"
---

# ModelDoc::Parameter

This method is obsolete and has been superseded by [ModelDoc2::Parameter](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Parameter.htm).

Description

This method returns a pointer to the parameter or to the Dispatch object. Most parameters are dimensions.

Syntax (OLE Automation)

retval = ModelDoc.Parameter ( stringIn)

| Input: | (BSTR) stringIn | Name of parameter (feature@name@component@assembly) |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the parameter |

Syntax (COM)

status = ModelDoc->IParameter ( stringIn, &retval )

| Input: | (BSTR) stringIn | Name of parameter (feature@name@component@assembly). |
| --- | --- | --- |
| Output: | (LPDIMENSION) retval | Pointer to the parameter |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The stringIn argument must be the fully qualified dimension name; for example, Error! Reference source not found."D1@Base-Extrude. You do not need to use the full dimension if you are calling, for example, the Feature::Parameter function.

SolidWorks recognizes some characters as special characters. The use of these characters in names of parts or features can cause the this method to fail to return a dimension. Special characters are: at sign (@), the period (.), and the slash (/).
