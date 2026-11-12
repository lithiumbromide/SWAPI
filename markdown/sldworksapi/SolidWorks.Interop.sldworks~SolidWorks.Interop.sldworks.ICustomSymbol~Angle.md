---
title: "Angle Property (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~Angle.html"
---

# Angle Property (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockInstance::Angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~Angle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [CustomSymbol::Angle](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~Angle.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
