---
title: "GOSTNotation Property (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GOSTNotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTNotation.html"
---

# GOSTNotation Property (ISFSymbol)

Gets whether the GOST Use for notation option is set.

## Syntax

### Visual Basic (Declaration)

```vb
Property GOSTNotation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Boolean

instance.GOSTNotation = value

value = instance.GOSTNotation
```

### C#

```csharp
System.bool GOSTNotation {get; set;}
```

### C++/CLI

```cpp
property System.bool GOSTNotation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the GOST Use for notation option is set, false if it is not

## VBA Syntax

See [SFSymbol::GOSTNotation](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GOSTNotation.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GOSTDefaultSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTDefaultSymbol.html)
