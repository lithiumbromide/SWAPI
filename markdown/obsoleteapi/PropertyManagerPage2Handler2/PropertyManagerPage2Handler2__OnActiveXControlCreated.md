---
title: "PropertyManagerPage2Handler2::OnActiveXControlCreated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnActiveXControlCreated.htm"
---

# PropertyManagerPage2Handler2::OnActiveXControlCreated

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnActiveXControlCreated](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnActiveXControlCreated.htm).

Description

This method is called when an attempt to create an ActiveX control on the PropertyManager occurs.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler2.OnActiveXControlCreated ( Id, Status )

| Input: | (long) Id | ID of this ActiveX control |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Status | TRUE if the ActiveX control creation was successful, FALSE if not |
| Output: | (long) retval | Action to take if the creation of the ActiveX control failed as defined in swHandleActiveXCreationFailure (see Remarks ) |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnActiveXControlCreated ( Id, Status, &retval )

| Input: | (long) Id | ID of this ActiveX control |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Status | TRUE if the creation of the ActiveX control was successful, FALSE if not |
| Output: | (long) retval | Action to take if the creation of the ActiveX control failed as defined in swHandleActiveXCreationFailure (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When the ActiveX control is created, the program creating the PropertyManager page should receive notification from this handler. Specify one of the available enumerators for this handler's retval argument:

- swHandleActiveXCreationFailure_Cancel. Continue creating the DVE page without the ActiveX control. This is the default.
- swHandleActiveXCreationFailure_Retry. Try to create the ActiveX control again. You can reuse the PropertyManagerPageActiveX::SetClass method to change the control ID or the license key to perhaps use another similar control or another version of the control, and then specify swHandleActiveXCreationFailure_Retry. Avoid an endless loop situation.
- swHandleActiveXCreationFailure_Continue. Cancel creating PropertyManager page. For example, it might be that the PropertyManager page is useless without the control, so the calling add-in might want to quit and handle the situation on its own.

Do not call PropertyManagerPageActiveX::GetControl to get the interface object for this ActiveX control.

You cannot get a reference to the ActiveX control inside this event handler, because the page is not displayed when this notification is sent. You can only get the reference to the control after the PropertyManager page is displayed.
