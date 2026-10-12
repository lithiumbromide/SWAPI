---
title: "Style Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.html"
---

# Style Property (IPropertyManagerPageSelectionbox)

Gets or sets style of this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Style as defined in [swPropMgrPageSelectionboxStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageSelectionBoxStyle_e.html)

## VBA Syntax

See [PropertyManagerPageSelectionbox::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~Style.html).

## Remarks

You must set this property before the PropertyManager page is displayed.

For a selection list to automatically have a horizontal scroll bar if the text is wider than the selection box, set this property's style to swPropMgrPageSelectionBoxStyle_HScroll.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
