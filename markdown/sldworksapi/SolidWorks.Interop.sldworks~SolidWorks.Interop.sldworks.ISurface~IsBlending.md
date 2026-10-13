---
title: "IsBlending Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsBlending"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsBlending.html"
---

# IsBlending Method (ISurface)

Gets whether the surface is a blending surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBlending() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsBlending()
```

### C#

```csharp
System.bool IsBlending()
```

### C++/CLI

```cpp
System.bool IsBlending();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is a blending surface, false if not

## VBA Syntax

See [Surface::IsBlending](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsBlending.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[IBody2::CreateBlendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBlendSurface.html)
[IBody2::ICreateBlendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBlendSurface.html)
