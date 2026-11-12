---
title: "TextVisible Property (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "TextVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~TextVisible.html"
---

# TextVisible Property (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockInstance::TextDisplay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~TextDisplay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property TextVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim value As System.Boolean

instance.TextVisible = value

value = instance.TextVisible
```

### C#

```csharp
System.bool TextVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool TextVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [CustomSymbol::TextVisible](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~TextVisible.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
