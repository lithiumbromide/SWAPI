---
title: "Component::IsDisplayDataOutOfDate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IsDisplayDataOutOfDate.htm"
---

# Component::IsDisplayDataOutOfDate

This method is obsolete and has been superseded by [Component2::IsDisplayDataOutOfDate](sldworksAPI.chm::/Component2/Component2__IsDisplayDataOutOfDate.htm).

Description

This method provides the status of the display data for this component.

Syntax (OLE Automation)

retval = Component.IsDisplayDataOutOfDate ( )

| Return: | (long) retval | Rebuild state of the components as defined in swOutOfDateStatus_e |
| --- | --- | --- |

Syntax (COM)

status = Component->IsDisplayDataOutOfDate ( &retval )

| Output: | (long) retval | Rebuild state of the components as defined in swOutOfDateStatus_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
