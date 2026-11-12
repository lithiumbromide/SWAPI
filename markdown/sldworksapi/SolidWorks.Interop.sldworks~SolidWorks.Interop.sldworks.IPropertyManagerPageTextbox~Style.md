---
title: "Style Property (IPropertyManagerPageTextbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTextbox"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox~Style.html"
---

# Style Property (IPropertyManagerPageTextbox)

Gets or sets various style-related properties for this text box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageTextbox
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

Styles as defined by [swPropMgrPageTextBoxStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageTextBoxStyle_e.html)

## VBA Syntax

See [PropertyManagerPageTextbox::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTextbox~Style.html).

## See Also

[IPropertyManagerPageTextbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox.html)
[IPropertyManagerPageTextbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
