---
title: "Normal Property (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "Normal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~Normal.html"
---

# Normal Property (IFace)

Obsolete. Superseded by [IFace2::Normal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~Normal.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Normal As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim value As System.Object

instance.Normal = value

value = instance.Normal
```

### C#

```csharp
System.object Normal {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Normal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Face::Normal](ms-its:sldworksapivb6.chm::/sldworks~Face~Normal.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
