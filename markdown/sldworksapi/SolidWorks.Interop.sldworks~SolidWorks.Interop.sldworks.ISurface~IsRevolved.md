---
title: "IsRevolved Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsRevolved"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsRevolved.html"
---

# IsRevolved Method (ISurface)

Gets whether the surface is a revolved surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRevolved() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsRevolved()
```

### C#

```csharp
System.bool IsRevolved()
```

### C++/CLI

```cpp
System.bool IsRevolved();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the surface is a revolved surface, false if not

## VBA Syntax

See [Surface::IsRevolved](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsRevolved.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[IFeatureManager::InsertRevolvedRefSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface.html)
