---
title: "Scale Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Scale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Scale.html"
---

# Scale Property (ISketchHatch)

Obsolete. Superseded by [ISketchHatch::Scale2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~Scale2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

See [SketchHatch::Scale](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Scale.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
