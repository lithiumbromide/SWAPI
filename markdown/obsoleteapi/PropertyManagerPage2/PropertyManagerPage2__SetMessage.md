---
title: "PropertyManagerPage2::SetMessage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2/PropertyManagerPage2__SetMessage.htm"
---

# PropertyManagerPage2::SetMessage

This method is obsolete and has been superseded by [PropertyManagerPage2::SetMessage2](PropertyManagerPage2__SetMessage2.htm).

Description

This method sets the message in this PropertyManager page.

Syntax (OLE Automation)

retval = PropertyManagerPage2.SetMessage ( Message, Visibility )

| Input: | (BSTR) Message | Message text |
| --- | --- | --- |
| Input: | (long) Visibility | Visibility state of this message as defined by swPropertyManagerPageMessageVisibility |
| Output: | (VARIANT_BOOL) retval | TRUE if the message is set, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2->SetMessage ( Message, Visibility, &retval )

| Input: | (BSTR) Message | Message text |
| --- | --- | --- |
| Input: | (long) Visibility | Visibility state of this message as defined by swPropertyManagerPageMessageVisibility |
| Output: | (VARIANT_BOOL) retval | TRUE if the message is set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
