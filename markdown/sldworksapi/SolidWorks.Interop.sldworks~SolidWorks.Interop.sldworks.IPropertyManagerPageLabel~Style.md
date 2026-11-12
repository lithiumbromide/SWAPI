---
title: "Style Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Style.html"
---

# Style Property (IPropertyManagerPageLabel)

Gets or sets style-related properties of this label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
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

Control style as defined in [swPropMgrPageLabelStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageLabelStyle_e.html)

## VBA Syntax

See [PropertyManagerPageLabel::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageLabel~Style.html).

## Remarks

You can only set this property before the PropertyManager is displayed.

This property value is a combination of several boolean values, each represented by a bit in this long value. The different values are represented in the [swPropMgrPageLabelStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageLabelStyle_e.html) enumeration. For example, to set a label control to have its text right-justified,
you should set the Style argument to swPropMgrPageLabelStyle_RightText. By default, the text in PropertyManagerPageLabel is left-justified.

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
