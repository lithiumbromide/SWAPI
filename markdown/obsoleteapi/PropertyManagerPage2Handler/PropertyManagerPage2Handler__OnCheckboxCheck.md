---
title: "PropertyManagerPage2Handler::OnCheckboxCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnCheckboxCheck.htm"
---

# PropertyManagerPage2Handler::OnCheckboxCheck

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnCheckboxCheck](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnCheckboxCheck.htm).

Description

This method is called when the end-user clicks a checkbox in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | Checkbox ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the checkbox is checked, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler->OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | Checkbox ID |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the checkbox is checked, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
