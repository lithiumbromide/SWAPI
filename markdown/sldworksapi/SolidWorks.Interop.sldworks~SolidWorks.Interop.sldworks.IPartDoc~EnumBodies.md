---
title: "EnumBodies Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies.html"
---

# EnumBodies Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies( _
   ByVal BodyType As System.Integer _
) As EnumBodies
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim value As EnumBodies

value = instance.EnumBodies(BodyType)
```

### C#

```csharp
EnumBodies EnumBodies(
   System.int BodyType
)
```

### C++/CLI

```cpp
EnumBodies^ EnumBodies(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`:

## VBA Syntax

See [PartDoc::EnumBodies](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumBodies.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
