---
title: "Callout Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "Callout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html"
---

# Callout Property (IPropertyManagerPageSelectionbox)

Gets or sets a multi-row, editable callout for this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Callout As Callout
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As Callout

instance.Callout = value

value = instance.Callout
```

### C#

```csharp
Callout Callout {get; set;}
```

### C++/CLI

```cpp
property Callout^ Callout {
   Callout^ get();
   void set (    Callout^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) for this selection box

## VBA Syntax

See [PropertyManagerPageSelectionbox::Callout](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~Callout.html).

## Remarks

This property returns NULL if callouts are not enabled for this selection box. Use [IPropertyManagerPageSelectionbox::SetCalloutLabel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.html) to enable the default callouts.

To create callouts for selection boxes:

1. Use [ISelectionManager::CreateCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateCallout2.html) to create the basic callout information.
2. Use the [ICallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) interface to modify the look and of the callout.
3. Use ISelectionBox::Callout to set the callout information for the selection box.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
