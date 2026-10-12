---
title: "OnSelectionboxCalloutCreated Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnSelectionboxCalloutCreated"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnSelectionboxCalloutCreated.html"
---

# OnSelectionboxCalloutCreated Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnSelectionboxCalloutCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxCalloutCreated.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxCalloutCreated( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7
Dim Id As System.Integer

instance.OnSelectionboxCalloutCreated(Id)
```

### C#

```csharp
void OnSelectionboxCalloutCreated(
   System.int Id
)
```

### C++/CLI

```cpp
void OnSelectionboxCalloutCreated(
   System.int Id
)
```

### Parameters

- `Id`: ID of this selection box

## VBA Syntax

See [PropertyManagerPage2Handler7::OnSelectionboxCalloutCreated](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnSelectionboxCalloutCreated.html).

## Remarks

This method is only called if callouts have been enabled for the selection box as indicated by the Id argument. Use [IPropertyManagerPageSelectionbox::SetCalloutLabel](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.html) to enable callouts.

You can collect information using this method. For example, you can get the selection type from the last selection. Next, use the [IPropertyManagerPageSelectionbox::Callout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html) property to get the [ICallout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) object. Then, use the various ICallout properties to control the callout text and display characteristics based on that selection information.

This method is a pre-notification.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)
[IPropertyManagerPage2Handler7::OnSelectionboxCalloutDestroyed Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnSelectionboxCalloutDestroyed.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
