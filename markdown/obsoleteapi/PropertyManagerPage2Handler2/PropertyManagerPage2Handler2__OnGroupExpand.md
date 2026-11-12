---
title: "PropertyManagerPage2Handler2::OnGroupExpand"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnGroupExpand.htm"
---

# PropertyManagerPage2Handler2::OnGroupExpand

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnGroupExpand](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnGroupExpand.htm).

Description

This method is called when the user clicks an arrow to open a group box on the PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnGroupExpand ( Id, Expanded )

| Input: | (long) Id | ID of the arrow that open a group box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Expanded | TRUE if the group box is opened, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnGroupExpand ( Id, Expanded )

| Input: | (long) Id | ID of the arrow that opens a group box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Expanded | TRUE if the group box is opened, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
