---
title: "FontSize Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "FontSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~FontSize.html"
---

# FontSize Property (ICallout)

Gets or sets the font size for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FontSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Integer

instance.FontSize = value

value = instance.FontSize
```

### C#

```csharp
System.int FontSize {get; set;}
```

### C++/CLI

```cpp
property System.int FontSize {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Font size of the callout

## VBA Syntax

See [Callout::FontSize](ms-its:sldworksapivb6.chm::/sldworks~Callout~FontSize.html).

## Examples

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
