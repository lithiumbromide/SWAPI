---
title: "PropertyManagerPage2Handler4::OnSelectionboxCalloutCreated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxCalloutCreated.htm"
---

# PropertyManagerPage2Handler4::OnSelectionboxCalloutCreated

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnSelectionboxCalloutCreated](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSelectionboxCalloutCreated.htm).

Description

This method does some processing while the callout for the selection box is being created.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSelectionboxCalloutCreated ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSelectionboxCalloutCreated ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called if callouts have been enabled for the selection box as indicated by the Id argument. Use PropertyManagerPageSelectionbox::SetCalloutLabel to enable callouts.

You can collect information using this method. For example, you can get the selection type from the last selection. Next, use the PropertyManagerPageSelectionbox::Callout property to get the Callout object. Then, use the various Callout properties to control the callout text and display characteristics based on that selection information.

This method is a pre-notification.
