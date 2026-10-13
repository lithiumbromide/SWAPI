---
title: "Component::GetPathName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetPathName.htm"
---

# Component::GetPathName

This method is obsolete and has been superseded by [Component2::GetPathName](sldworksAPI.chm::/Component2/Component2__GetPathName.htm).

Description

This method gets the full path name of this component.

Syntax (OLE Automation)

retval = Component.GetPathName ( )

| Return: | (BSTR)retval | Full path name for this component, including the file name |
| --- | --- | --- |

Syntax (COM)

status = Component->GetPathName ( &retval )

| Output: | (BSTR)retval | Full path name for this component, including the file name |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if Successful |

Remarks

It is possible that the underlying document for this component is not loaded into memory. This can happen if the component is lightweight or suppressed. When this happens, [Component::GetModelDoc](Component__GetModelDoc.htm) returns NULL, and this method returns the as-saved file and path name for the component. Component::GetPathName does not apply search criteria or look in the current working directory for the component file reference if the component is lightweight or suppressed.
