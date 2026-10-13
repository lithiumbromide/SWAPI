---
title: "MaterialIdName Property (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "MaterialIdName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~MaterialIdName.html"
---

# MaterialIdName Property (IFace)

Obsolete. Superseded by [IFace2::MaterialIdName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~MaterialIdName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialIdName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim value As System.String

instance.MaterialIdName = value

value = instance.MaterialIdName
```

### C#

```csharp
System.string MaterialIdName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Face::MaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Face~MaterialIdName.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
