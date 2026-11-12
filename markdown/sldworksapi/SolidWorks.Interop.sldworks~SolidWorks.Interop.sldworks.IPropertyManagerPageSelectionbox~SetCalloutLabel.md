---
title: "SetCalloutLabel Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "SetCalloutLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.html"
---

# SetCalloutLabel Method (IPropertyManagerPageSelectionbox)

Sets the default callout label for selections made in this selection box on the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCalloutLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Label As System.String
Dim value As System.Boolean

value = instance.SetCalloutLabel(Label)
```

### C#

```csharp
System.bool SetCalloutLabel(
   System.string Label
)
```

### C++/CLI

```cpp
System.bool SetCalloutLabel(
   System.String^ Label
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Label`: Default callout label

### Return Value

True if the callout label was set, false if not

## VBA Syntax

See [PropertyManagerPageSelectionbox::SetCalloutLabel](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~SetCalloutLabel.html).

## Remarks

This property can be used at any time, whether or not the callout is displayed. The label must not be an empty string. By default, the selection box is created without callouts for selections. This method overrides that behavior.

For more control, you can implement the [IPropertyManagerPage2Handler5::OnSelectionboxCalloutCreated](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnSelectionboxCalloutCreated.html) property, which allows you to collect information such as the selection type from the last selection. Next, use the [IPropertyManagerPageSelectionbox::Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html) property to get the [ICallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) object. Then, use that object's various properties to control the callout text and display characteristics based on that selection information.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
