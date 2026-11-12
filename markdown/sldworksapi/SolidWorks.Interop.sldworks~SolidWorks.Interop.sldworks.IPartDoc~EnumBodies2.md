---
title: "EnumBodies2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies2.html"
---

# EnumBodies2 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies2( _
   ByVal BodyType As System.Integer _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim value As EnumBodies2

value = instance.EnumBodies2(BodyType)
```

### C#

```csharp
EnumBodies2 EnumBodies2(
   System.int BodyType
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumBodies2(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`:

## VBA Syntax

See [PartDoc::EnumBodies2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumBodies2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
