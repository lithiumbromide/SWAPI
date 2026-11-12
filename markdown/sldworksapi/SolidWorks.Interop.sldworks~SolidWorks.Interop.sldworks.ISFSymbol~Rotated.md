---
title: "Rotated Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "Rotated"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Rotated.html"
---

# Rotated Property (ISFSymbol)

Obsolete. Superseded by [ISFSymbol::Orientation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~Orientation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Rotated As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Boolean

instance.Rotated = value

value = instance.Rotated
```

### C#

```csharp
System.bool Rotated {get; set;}
```

### C++/CLI

```cpp
property System.bool Rotated {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SFSymbol::Rotated](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~Rotated.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
