---
title: "Grinding Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "Grinding"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Grinding.html"
---

# Grinding Property (ISFSymbol)

Obsolete. Superseded by [ISFSymbol::GetSymbolSurfaceTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Grinding As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Boolean

instance.Grinding = value

value = instance.Grinding
```

### C#

```csharp
System.bool Grinding {get; set;}
```

### C++/CLI

```cpp
property System.bool Grinding {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SFSymbol::Grinding](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~Grinding.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
