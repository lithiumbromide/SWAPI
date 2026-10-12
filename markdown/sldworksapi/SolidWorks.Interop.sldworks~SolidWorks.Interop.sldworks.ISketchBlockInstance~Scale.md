---
title: "Scale Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "Scale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale.html"
---

# Scale Property (ISketchBlockInstance)

Obsolete. Superseded by [ISketchBlockInstance::Scale2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~Scale2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Double

instance.Scale = value

value = instance.Scale
```

### C#

```csharp
System.double Scale {get; set;}
```

### C++/CLI

```cpp
property System.double Scale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SketchBlockInstance::Scale](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~Scale.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
