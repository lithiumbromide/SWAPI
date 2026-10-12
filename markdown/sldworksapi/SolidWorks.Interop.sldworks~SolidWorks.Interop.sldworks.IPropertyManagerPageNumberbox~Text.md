---
title: "Text Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Text.html"
---

# Text Property (IPropertyManagerPageNumberbox)

Gets the text that appears in the number box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim value As System.String

value = instance.Text
```

### C#

```csharp
System.string Text {get;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text in number box

## VBA Syntax

See [PropertyManagerPageNumberbox::Text](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~Text.html).

## Remarks

If a user changes the value in an number box by typing in a new value, the [IPropertyManagerPage2Handler5::OnTextboxChanged](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnTextboxChanged.html) is called with the current text string and the ID of the number box. You can then use IPropertyManagerPageNumberbox::Text to show the text elsewhere, such as in a callout.

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
