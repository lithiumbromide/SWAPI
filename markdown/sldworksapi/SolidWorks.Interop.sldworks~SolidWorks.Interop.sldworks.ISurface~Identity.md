---
title: "Identity Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "Identity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Identity.html"
---

# Identity Method (ISurface)

Gets the type of surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function Identity() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Integer

value = instance.Identity()
```

### C#

```csharp
System.int Identity()
```

### C++/CLI

```cpp
System.int Identity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of surface as defined in [swSurfaceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceTypes_e.html)

## VBA Syntax

See [Surface::Identity](ms-its:sldworksapivb6.chm::/sldworks~Surface~Identity.html).

## Examples

[Get Surface Type (VBA)](Get_Surface_Type_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
