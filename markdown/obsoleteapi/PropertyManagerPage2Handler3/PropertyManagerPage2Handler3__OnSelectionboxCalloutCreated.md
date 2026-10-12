---
title: "PropertyManagerPage2Handler3::OnSelectionboxCalloutCreated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSelectionboxCalloutCreated.htm"
---

# PropertyManagerPage2Handler3::OnSelectionboxCalloutCreated

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnSelectionboxCalloutCreated](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxCalloutCreated.htm).

Description

This method does some processing while the callout for the selection box is being created.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnSelectionboxCalloutCreated ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnSelectionboxCalloutCreated ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called if callouts have been enabled for the selection box as indicated by the Id argument. See PropertyManagerPageSelectionbox::SetCalloutLabel to enable callouts.

Using this method, you can collect information. For example, you can get the selection type from the last selection. Next, use the PropertyManagerPageSelectionbox::Callout property to get the Callout object. Then, use the various Callout properties to control the callout text and display characteristics based on that selection information.

This method is essentially a pre-notification.
