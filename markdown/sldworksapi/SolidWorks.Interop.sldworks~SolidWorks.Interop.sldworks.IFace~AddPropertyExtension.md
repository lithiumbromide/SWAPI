---
title: "AddPropertyExtension Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IFace)

Obsolete. Superseded by [IFace2::AddPropertyExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~AddPropertyExtension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`:

## VBA Syntax

See [Face::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Face~AddPropertyExtension.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
