---
title: "OnWindowFromHandleControlCreated Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnWindowFromHandleControlCreated"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnWindowFromHandleControlCreated.html"
---

# OnWindowFromHandleControlCreated Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnWindowFromHandleControlCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnWindowFromHandleControlCreated.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnWindowFromHandleControlCreated( _
   ByVal Id As System.Integer, _
   ByVal Status As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim Status As System.Boolean
Dim value As System.Integer

value = instance.OnWindowFromHandleControlCreated(Id, Status)
```

### C#

```csharp
System.int OnWindowFromHandleControlCreated(
   System.int Id,
   System.bool Status
)
```

### C++/CLI

```cpp
System.int OnWindowFromHandleControlCreated(
   System.int Id,
   System.bool Status
)
```

### Parameters

- `Id`: ID of this .NET control
- `Status`: True if the .NET control is successfully created; false if not

### Return Value

If Status = true, return nothing

If Status = false, return an action as defined in [swHandleWindowFromHandleCreationFailure_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHandleWindowFromHandleCreationFailure_e.html)

(see **Remarks**)

## VBA Syntax

See [PropertyManagerPage2Handler8::OnWindowFromHandleControlCreated](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnWindowFromHandleControlCreated.html).

## Remarks

If the .NET control is not successfully created (Status = false), the program creating the PropertyManager page should receive notification from this handler. Return one of the following options in [swHandleWindowFromHandleCreationFailure_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHandleWindowFromHandleCreationFailure_e.html):

- swHandleWindowFromHandleCreationFailure_Cancel. Continue creating the PropertyManager page without the .NET control. This is the default.
- swHandleWindowFromHandleCreationFailure_Retry. Try to create the .NET control again. You can call the [IPropertyManagerPageWindowFromHandle::SetWindowHandle](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandle.html) method to change the .NET control handle to perhaps use another similar control or another version of the control, and then return swHandleWindowFromHandleCreationFailure_Retry. Avoid an endless loop situation.
- swHandleWindowFromHandleCreationFailure_Continue. Cancel creating PropertyManager page. For example, it might be that the PropertyManager page is useless without the control, so the calling add-in might want to quit and handle the situation on its own.

For example if the control is created successfully, then SOLIDWORKS passes Status = true to the add-in, and nothing is returned. If the control fails to be created, SOLIDWORKS passes Status = false to the add-in, and the handler returns swHandleWindowFromHandleCreationFailure_Continue.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
