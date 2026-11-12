---
title: "Scale2 Property (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~Scale2.html"
---

# Scale2 Property (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockInstance::Scale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~Scale.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [CustomSymbol::Scale2](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~Scale2.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
