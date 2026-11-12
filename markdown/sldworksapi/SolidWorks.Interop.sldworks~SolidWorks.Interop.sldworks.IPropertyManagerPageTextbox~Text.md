---
title: "Text Property (IPropertyManagerPageTextbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTextbox"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox~Text.html"
---

# Text Property (IPropertyManagerPageTextbox)

Gets and sets the text that appears in the text box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageTextbox
Dim value As System.String

instance.Text = value

value = instance.Text
```

### C#

```csharp
System.string Text {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for the box

## VBA Syntax

See [PropertyManagerPageTextbox::Text](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTextbox~Text.html).

## See Also

[IPropertyManagerPageTextbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox.html)
[IPropertyManagerPageTextbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
