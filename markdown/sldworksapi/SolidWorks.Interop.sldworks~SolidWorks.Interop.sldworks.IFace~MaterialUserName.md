---
title: "MaterialUserName Property (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "MaterialUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~MaterialUserName.html"
---

# MaterialUserName Property (IFace)

Obsolete. Superseded by [IFace2::MaterialUserName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~MaterialUserName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim value As System.String

instance.MaterialUserName = value

value = instance.MaterialUserName
```

### C#

```csharp
System.string MaterialUserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialUserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Face::MaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Face~MaterialUserName.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
