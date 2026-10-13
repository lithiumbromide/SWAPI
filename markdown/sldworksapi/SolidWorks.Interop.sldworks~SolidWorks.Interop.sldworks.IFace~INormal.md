---
title: "INormal Property (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "INormal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~INormal.html"
---

# INormal Property (IFace)

Obsolete. Superseded by [IFace2::INormal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~INormal.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property INormal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim value As System.Double

instance.INormal = value

value = instance.INormal
```

### C#

```csharp
System.double INormal {get; set;}
```

### C++/CLI

```cpp
property System.double INormal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Face::INormal](ms-its:sldworksapivb6.chm::/sldworks~Face~INormal.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
