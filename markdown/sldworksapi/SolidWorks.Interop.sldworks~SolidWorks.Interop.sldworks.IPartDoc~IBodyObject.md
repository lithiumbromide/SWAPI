---
title: "IBodyObject Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IBodyObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IBodyObject.html"
---

# IBodyObject Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html) and [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IBodyObject() As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As Body

value = instance.IBodyObject()
```

### C#

```csharp
Body IBodyObject()
```

### C++/CLI

```cpp
Body^ IBodyObject();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [PartDoc::IBodyObject](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IBodyObject.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
