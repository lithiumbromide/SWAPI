---
title: "TextDisplay Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "TextDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~TextDisplay.html"
---

# TextDisplay Property (ISketchBlockInstance)

Gets or sets whether to display text for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextDisplay As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Integer

instance.TextDisplay = value

value = instance.TextDisplay
```

### C#

```csharp
System.int TextDisplay {get; set;}
```

### C++/CLI

```cpp
property System.int TextDisplay {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display state as defined in [swBlockInstanceTextDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockInstanceTextDisplay_e.html)

## VBA Syntax

See [SketchBlockInstance::TextDisplay](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~TextDisplay.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
