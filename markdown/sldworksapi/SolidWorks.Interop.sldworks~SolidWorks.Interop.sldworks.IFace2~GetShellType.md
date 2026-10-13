---
title: "GetShellType Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetShellType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetShellType.html"
---

# GetShellType Method (IFace2)

Gets the shell type for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShellType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetShellType()
```

### C#

```csharp
System.int GetShellType()
```

### C++/CLI

```cpp
System.int GetShellType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Shell type:

- 0 = Open shell. For example, a face that belongs to a sheet (surface) body or reference surface.
- 1 = Internal shell. For example, a face that belongs to a cavity. Face helps define an internal volume.
- 2 = External shell. For example, a typical face on a solid body (helps "hold in" the body mass). This includes all external faces (faces belonging to bosses, pockets, holes, and so on).

## VBA Syntax

See [Face2::GetShellType](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetShellType.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
