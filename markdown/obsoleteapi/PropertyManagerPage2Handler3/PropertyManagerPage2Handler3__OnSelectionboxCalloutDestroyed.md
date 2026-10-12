---
title: "PropertyManagerPage2Handler3::OnSelectionboxCalloutDestroyed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSelectionboxCalloutDestroyed.htm"
---

# PropertyManagerPage2Handler3::OnSelectionboxCalloutDestroyed

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnSelectionboxCalloutDestroyed](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxCalloutDestroyed.htm).

Description

This method does some processing while the callout for this selection box is being destroyed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnSelectionboxCalloutDestroyed ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnSelectionboxCalloutDestroyed ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called if callouts have been enabled for the selection box as indicated by the Id argument. See PropertyManagerPageSelectionbox::SetCalloutLabel to enable callouts. This method is essentially a pre-notification.
