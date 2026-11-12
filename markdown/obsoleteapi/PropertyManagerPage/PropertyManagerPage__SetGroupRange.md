---
title: "PropertyManagerPage::SetGroupRange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage/PropertyManagerPage__SetGroupRange.htm"
---

# PropertyManagerPage::SetGroupRange

This object and method are obsolete and have been superseded by [PropertyManagerPage2](sldworksAPI.chm::/PropertyManagerPage2/PropertyManagerPage2.htm).

Description

This method sets the group box range for this PropertyManager page.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = PropertyManagerPage->SetGroupRange ( FirstGroupId, FirstCheckId, GroupCount )

| Input: | (long) FirstGroupId | Resource ID of the first group title's static text control |
| --- | --- | --- |
| Input: | (long) FirstCheckId | Resource ID of the first check box control |
| Input: | (long) GroupCount | Number of group boxes |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
