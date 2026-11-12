---
title: "PropertyManagerPage2Handler4::OnSelectionboxCalloutDestroyed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxCalloutDestroyed.htm"
---

# PropertyManagerPage2Handler4::OnSelectionboxCalloutDestroyed

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnSelectionboxCalloutDestroyed.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSelectionboxCalloutDestroyed.htm)

Description

This method does some processing after the callout for this selection box is destroyed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSelectionboxCalloutDestroyed ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSelectionboxCalloutDestroyed ( Id )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is:

- only called if callouts have been enabled for the selection box as indicated by the Id argument. Use PropertyManagerPageSelectionbox::SetCalloutLabel to enable callouts.
- a post-notification. The callout pointed to by PropertyManagerPageSelectionbox::Callout no longer exists, so do not make any calls to Callout methods.
