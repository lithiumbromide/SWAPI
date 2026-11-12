---
title: "IGetBox Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IGetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IGetBox.html"
---

# IGetBox Method (IComponent)

Obsolete. Superseded by [IComponent2::IGetBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetBox.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBox( _
   ByVal IncludeRefPlanes As System.Boolean, _
   ByVal IncludeSketches As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim IncludeRefPlanes As System.Boolean
Dim IncludeSketches As System.Boolean
Dim value As System.Double

value = instance.IGetBox(IncludeRefPlanes, IncludeSketches)
```

### C#

```csharp
System.double IGetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

### C++/CLI

```cpp
System.double IGetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludeRefPlanes`:
- `IncludeSketches`:

## VBA Syntax

See [Component::IGetBox](ms-its:sldworksapivb6.chm::/sldworks~Component~IGetBox.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
