---
title: "EnumBodies Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "EnumBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies.html"
---

# EnumBodies Method (IComponent2)

Obsolete. Superseded by [IComponent2::EnumBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~EnumBodies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies( _
   ByVal BodyType As System.Integer _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As EnumBodies2

value = instance.EnumBodies(BodyType)
```

### C#

```csharp
EnumBodies2 EnumBodies(
   System.int BodyType
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumBodies(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`:

## VBA Syntax

See [Component2::EnumBodies](ms-its:sldworksapivb6.chm::/sldworks~Component2~EnumBodies.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
