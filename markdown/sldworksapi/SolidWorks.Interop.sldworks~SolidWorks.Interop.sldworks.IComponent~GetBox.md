---
title: "GetBox Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "GetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~GetBox.html"
---

# GetBox Method (IComponent)

Obsolete. Superseded by [IComponent2::GetBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBox.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBox( _
   ByVal IncludeRefPlanes As System.Boolean, _
   ByVal IncludeSketches As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim IncludeRefPlanes As System.Boolean
Dim IncludeSketches As System.Boolean
Dim value As System.Object

value = instance.GetBox(IncludeRefPlanes, IncludeSketches)
```

### C#

```csharp
System.object GetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

### C++/CLI

```cpp
System.Object^ GetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludeRefPlanes`:
- `IncludeSketches`:

## VBA Syntax

See [Component::GetBox](ms-its:sldworksapivb6.chm::/sldworks~Component~GetBox.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
