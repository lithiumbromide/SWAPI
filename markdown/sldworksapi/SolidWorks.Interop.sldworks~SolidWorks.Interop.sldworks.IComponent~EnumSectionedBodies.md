---
title: "EnumSectionedBodies Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "EnumSectionedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~EnumSectionedBodies.html"
---

# EnumSectionedBodies Method (IComponent)

Obsolete. Superseded by [IComponent2::EnumSectionedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~EnumSectionedBodies.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim ViewIn As ModelView
Dim value As EnumBodies

value = instance.EnumSectionedBodies(ViewIn)
```

### C#

```csharp
EnumBodies EnumSectionedBodies(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
EnumBodies^ EnumSectionedBodies(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`:

## VBA Syntax

See [Component::EnumSectionedBodies](ms-its:sldworksapivb6.chm::/sldworks~Component~EnumSectionedBodies.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
