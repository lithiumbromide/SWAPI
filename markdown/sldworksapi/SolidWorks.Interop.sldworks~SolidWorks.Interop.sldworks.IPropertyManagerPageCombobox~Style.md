---
title: "Style Property (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~Style.html"
---

# Style Property (IPropertyManagerPageCombobox)

Gets or sets the style for the attached drop-down list for this combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
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

Combo-box style as defined in [swPropMgrPageComboBoxStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageComboBoxStyle_e.html)

## VBA Syntax

See [PropertyManagerPageCombobox::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~Style.html).

## Remarks

Style is a combination of Boolean values, each represented by a bit in this long value. The different Boolean values are represented in the swPropMgrPageComboBoxStyle_e enumeration. For example, to set the attached drop-down list of a combo box so that the items are sorted, set Style to swPropMgrPageComboBoxStyle_Sorted.

The control style must be set before the PropertyManager page is displayed except if setting Style to swPropMgrPageComboBoxStyle_EditBoxReadOnly. You can set swPropMgrPageComboBoxStyle_EditBoxReadOnly either before or after the PropertyManager page is displayed.

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
