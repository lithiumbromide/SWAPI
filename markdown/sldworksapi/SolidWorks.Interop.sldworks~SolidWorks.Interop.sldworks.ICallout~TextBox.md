---
title: "TextBox Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "TextBox"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextBox.html"
---

# TextBox Property (ICallout)

Gets or sets whether the callout text is enclosed within a box.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextBox As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Boolean

instance.TextBox = value

value = instance.TextBox
```

### C#

```csharp
System.bool TextBox {get; set;}
```

### C++/CLI

```cpp
property System.bool TextBox {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True encloses the callout text in a box, false does not

## VBA Syntax

See [Callout::TextBox](ms-its:sldworksapivb6.chm::/sldworks~Callout~TextBox.html).

## Examples

[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## Remarks

You can only set this property before the callout is shown or while the callout is hidden.

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
