---
title: "Component::IGetChildrenCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetChildrenCount.htm"
---

# Component::IGetChildrenCount

This method is obsolete and has been superseded by [Component2::IGetChildrenCount](sldworksAPI.chm::/Component2/Component2__IGetChildrenCount.htm).

Description

This method gets the number of direct child components for this component object.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->IGetChildrenCount ( &retval )

| Output: | (int*) retval | Number of children |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The value returned is a single-level count. This method does not count subassemblies.

To get the number of children in a Dispatch application, check the size of the VARIANT returned by Component::GetChildren.

For more information, see SafeArray Return Values.
