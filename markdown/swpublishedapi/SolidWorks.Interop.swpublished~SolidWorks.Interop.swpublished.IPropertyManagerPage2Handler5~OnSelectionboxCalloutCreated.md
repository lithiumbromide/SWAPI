---
title: "OnSelectionboxCalloutCreated Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnSelectionboxCalloutCreated"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnSelectionboxCalloutCreated.html"
---

# OnSelectionboxCalloutCreated Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnSelectionboxCalloutCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnSelectionboxCalloutCreated.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxCalloutCreated( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
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

See [PropertyManagerPage2Handler5::OnSelectionboxCalloutCreated](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnSelectionboxCalloutCreated.html).

## Remarks

This method is only called if callouts have been enabled for the selection box as indicated by the Id argument. Use [IPropertyManagerPageSelectionbox::SetCalloutLabel](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.html) to enable callouts.

You can collect information using this method. For example, you can get the selection type from the last selection. Next, use the [IPropertyManagerPageSelectionbox::Callout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html) property to get the [ICallout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) object. Then, use the various ICallout properties to control the callout text and display characteristics based on that selection information.

This method is a pre-notification.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
