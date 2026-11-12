---
title: "PropertyManagerPage2Handler::OnGroupCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnGroupCheck.htm"
---

# PropertyManagerPage2Handler::OnGroupCheck

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnGroupCheck](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnGroupCheck.htm).

Description

This method is called when the end-user clicks a group checkbox in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnGroupCheck ( Id, Checked )

| Input: | (long) Id | Checkbox ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if checkbox is selected, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler->OnGroupCheck ( Id, Checked )

| Input: | (long) Id | Checkbox ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if checkbox is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
