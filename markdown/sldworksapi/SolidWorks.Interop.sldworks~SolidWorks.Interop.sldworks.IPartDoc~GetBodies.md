---
title: "GetBodies Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies.html"
---

# GetBodies Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies( _
   ByVal BodyType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim value As System.Object

value = instance.GetBodies(BodyType)
```

### C#

```csharp
System.object GetBodies(
   System.int BodyType
)
```

### C++/CLI

```cpp
System.Object^ GetBodies(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`:

## VBA Syntax

See [PartDoc::GetBodies](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetBodies.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
