---
title: "IsSwept Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsSwept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsSwept.html"
---

# IsSwept Method (ISurface)

Gets whether the surface is swept.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSwept() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsSwept()
```

### C#

```csharp
System.bool IsSwept()
```

### C++/CLI

```cpp
System.bool IsSwept();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is a swept surface, false if not

## VBA Syntax

See [Surface::IsSwept](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsSwept.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.html)
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
