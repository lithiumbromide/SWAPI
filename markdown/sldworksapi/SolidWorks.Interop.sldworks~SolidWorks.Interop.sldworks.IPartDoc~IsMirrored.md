---
title: "IsMirrored Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IsMirrored"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsMirrored.html"
---

# IsMirrored Method (IPartDoc)

Gets whether this part is mirrored.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsMirrored() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Boolean

value = instance.IsMirrored()
```

### C#

```csharp
System.bool IsMirrored()
```

### C++/CLI

```cpp
System.bool IsMirrored();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the part is mirrored, false if not

## VBA Syntax

See [PartDoc::IsMirrored](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IsMirrored.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IComponent2::IsMirrored Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsMirrored.html)
[IAssemblyDoc::MirrorComponents3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents3.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
