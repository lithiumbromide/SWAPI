---
title: "PropertyManagerPage2Handler::OnGroupExpand"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnGroupExpand.htm"
---

# PropertyManagerPage2Handler::OnGroupExpand

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnGroupExpand](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnGroupExpand.htm).

Description

This method is called when the end-user clicks a group expansion arrow in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnGroupExpand ( Id, Expanded )

| Input: | (long) Id | Expansion arrow ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Expanded | TRUE if it is expanded, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler->OnGroupExpand ( Id, Expanded )

| Input: | (long) Id | Expansion arrow ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Expanded | TRUE if it is expanded, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
