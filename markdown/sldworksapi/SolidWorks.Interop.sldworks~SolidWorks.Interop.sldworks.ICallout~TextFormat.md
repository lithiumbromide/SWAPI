---
title: "TextFormat Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "TextFormat"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextFormat.html"
---

# TextFormat Property (ICallout)

Gets or sets the text format for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextFormat As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As TextFormat

instance.TextFormat = value

value = instance.TextFormat
```

### C#

```csharp
TextFormat TextFormat {get; set;}
```

### C++/CLI

```cpp
property TextFormat^ TextFormat {
   TextFormat^ get();
   void set (    TextFormat^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [Callout::TextFormat](ms-its:sldworksapivb6.chm::/sldworks~Callout~TextFormat.html).

## Examples

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
