---
title: "ModelDocExtension::IsVirtualComponent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__IsVirtualComponent.htm"
---

# ModelDocExtension::IsVirtualComponent

This method is obsolete and has been superseded by [ModelDocExtension::IsVirtualComponent2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__IsVirtualComponent2.htm).

Description

This method gets the path of the parent assembly of a model if the model is a virtual component.

Syntax (OLE Automation)

*ParentPath = ModelDocExtension.IsVirtualComponent ()

| Output: | (BSTR ) *ParentPath | Fully qualified path of the parent assembly of a model if the model is a virtual component; otherwise, an empty string is returned |
| --- | --- | --- |

Syntax (COM)

status = ModelDocExtension->IsVirtualComponent ( &ParentPath)

| Output: | (BSTR ) *ParentPath | Fully qualified path of the parent assembly of a model if the model is a virtual component; otherwise, an empty string is returned |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only works, and should only be called, if the model document is opened in its own window.
