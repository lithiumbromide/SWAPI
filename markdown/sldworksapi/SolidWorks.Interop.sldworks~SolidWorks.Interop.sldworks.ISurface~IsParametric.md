---
title: "IsParametric Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsParametric"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsParametric.html"
---

# IsParametric Method (ISurface)

Gets whether the surface is a parametric (spline type) surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsParametric() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsParametric()
```

### C#

```csharp
System.bool IsParametric()
```

### C++/CLI

```cpp
System.bool IsParametric();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is a parametric surface, false if not

## VBA Syntax

See [Surface::IsParametric](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsParametric.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
