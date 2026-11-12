---
title: "OnClose Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnClose"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnClose.html"
---

# OnClose Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnClose.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnClose( _
   ByVal Reason As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
Dim Reason As System.Integer

instance.OnClose(Reason)
```

### C#

```csharp
void OnClose(
   System.int Reason
)
```

### C++/CLI

```cpp
void OnClose(
   System.int Reason
)
```

### Parameters

- `Reason`: Reason this method is called as defined in [swPropertyManagerPageCloseReasons_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageCloseReasons_e.html)

## VBA Syntax

See [PropertyManagerPage2Handler5::OnClose](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnClose.html).

## Remarks

This handler method is called when the PropertyManager page is about to close.

SOLIDWORKS controls when add-ins can do work. An add-in is unable to do any real work within the PropertyManager2Handler5::OnClose handler because the PropertyManager page and command are closing. So, typically the [IPropertyPage2Handler5::AfterClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~AfterClose.html) handler is called after IPropertyManager2Handler5::OnClose to allow an add-in to do work. However:

| If PropertyManager page is... | And you implemented the handler in... | Then you... |
| --- | --- | --- |
| Not pinned | C++ | Can prevent the PropertyManager page from closing by setting the HRESULT return value to S_false. |
|  | Visual Basic | Should use the Err.Raise method with a value of 1 to prevent the PropertyManager page from closing. In VB.NET, use 0 with Err.Raise. |
|  | NOTE: When control returns to SOLIDWORKS: The IPropertyManager page remains displayed on the screen. The IPropertyManagerPage2Handler5::AfterClose handler is not called. |  |
| Pinned | C++ or Visual Basic | Set HRESULT to S_false to close the PropertyManager page (i.e., ignore the fact that the page is pinned). This allows your add-in to call the IPropertyManagerPage2Handler5::AfterClose handler and do its work. To avoid aggravating your user, who expected the PropertyManager page to remain pinned, you should re-display and re-pin the PropertyManager page after the add-in finishes its work. |

NOTE: In a previous version of this method, [IPropertyManagerPage2Handler3::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler3~OnClose.html), if the user clicked the Cancel button and the PropertyManager page had a pushpin, then this method returned swPropertyManagerPageClose_Closed. This version of this method returns swPropertyManagerPageClose_Cancel in this scenario.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
