---
title: "TextDisplay Property (IBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "IBlockInstance"
member: "TextDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~TextDisplay.html"
---

# TextDisplay Property (IBlockInstance)

Obsolete. Superseded by [ISketchBlockInstance::TextDisplay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~TextDisplay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property TextDisplay As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockInstance
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

## VBA Syntax

See [BlockInstance::TextDisplay](ms-its:sldworksapivb6.chm::/sldworks~BlockInstance~TextDisplay.html).

## See Also

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.html)
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.html)
