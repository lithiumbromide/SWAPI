---
title: "OnSelectionboxCalloutDestroyed Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnSelectionboxCalloutDestroyed"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnSelectionboxCalloutDestroyed.html"
---

# OnSelectionboxCalloutDestroyed Method (IPropertyManagerPage2Handler9)

Performs some processing after the callout for this selection box is destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxCalloutDestroyed( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer

instance.OnSelectionboxCalloutDestroyed(Id)
```

### C#

```csharp
void OnSelectionboxCalloutDestroyed(
   System.int Id
)
```

### C++/CLI

```cpp
void OnSelectionboxCalloutDestroyed(
   System.int Id
)
```

### Parameters

- `Id`: ID of this selection box

## VBA Syntax

See [PropertyManagerPage2Handler9::OnSelectionboxCalloutDestroyed](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnSelectionboxCalloutDestroyed.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

This method is:

- only called if callouts have been enabled for the selection box as indicated by the Id argument. Use [IPropertyManagerPageSelectionbox::SetCalloutLabel](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.html) to enable callouts.
- a post-notification. The callout pointed to by [IPropertyManagerPageSelectionbox::Callout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html) no longer exists, so do not make any calls to [ICallout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) methods.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)
[IProeprtyManagerPage2Handler9::OnSelectionboxCalloutCreated Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnSelectionboxCalloutCreated.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
