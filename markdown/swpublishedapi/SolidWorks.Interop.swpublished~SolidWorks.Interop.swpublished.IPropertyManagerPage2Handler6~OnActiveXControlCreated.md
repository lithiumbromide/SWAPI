---
title: "OnActiveXControlCreated Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnActiveXControlCreated"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnActiveXControlCreated.html"
---

# OnActiveXControlCreated Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnActiveXControlCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnActiveXControlCreated.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnActiveXControlCreated( _
   ByVal Id As System.Integer, _
   ByVal Status As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler6
Dim Id As System.Integer
Dim Status As System.Boolean
Dim value As System.Integer

value = instance.OnActiveXControlCreated(Id, Status)
```

### C#

```csharp
System.int OnActiveXControlCreated(
   System.int Id,
   System.bool Status
)
```

### C++/CLI

```cpp
System.int OnActiveXControlCreated(
   System.int Id,
   System.bool Status
)
```

### Parameters

- `Id`: ID of this ActiveX control
- `Status`: True if the ActiveX control creation was successful, false if not

### Return Value

Action to take if the creation of the ActiveX control failed as defined in [swHandleActiveXCreationFailure](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHandleActiveXCreationFailure_e.html) (see Remarks)

## VBA Syntax

See [PropertyManagerPage2Handler6::OnActiveXControlCreated](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnActiveXControlCreated.html).

## Remarks

When the ActiveX control is created, the program creating the PropertyManager page should receive notification from this handler. Specify one of the available enumerators for this handler's return value:

- swHandleActiveXCreationFailure_Cancel. Continue creating the PropertyManager page without the ActiveX control. This is the default.
- swHandleActiveXCreationFailure_Retry. Try to create the ActiveX control again. You can reuse the [IPropertyManagerPageActiveX::SetClass](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageActiveX~SetClass.html) method to change the control ID or the license key to perhaps use another similar control or another version of the control, and then specify swHandleActiveXCreationFailure_Retry. Avoid an endless loop situation.
- swHandleActiveXCreationFailure_Continue. Cancel creating PropertyManager page. For example, it might be that the PropertyManager page is useless without the control, so the calling add-in might want to quit and handle the situation on its own.

For example, if the control is created successfully, then SOLIDWORKS passes true for Status to the add-in and the return value is ignored. If the control fails to be created, SOLIDWORKS passes false for Status to the add-in and the return value is swHandleActiveXCreationFailure_Continue.

Do not call [IPropertyManagerPageActiveX::GetControl](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageActiveX~GetControl.html) to get the interface object for this ActiveX control.

You cannot get a reference to the ActiveX control inside this event handler because the page is not displayed when this notification is sent. You can only get the reference to the control after the PropertyManager page is displayed.

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
