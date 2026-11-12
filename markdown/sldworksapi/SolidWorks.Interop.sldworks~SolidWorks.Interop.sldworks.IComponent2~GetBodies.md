---
title: "GetBodies Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies.html"
---

# GetBodies Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBodies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies( _
   ByVal BodyType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As System.Object

value = instance.GetBodies(BodyType)
```

### C#

```csharp
System.object GetBodies(
   System.int BodyType
)
```

### C++/CLI

```cpp
System.Object^ GetBodies(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`:

## VBA Syntax

See [Component2::GetBodies](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetBodies.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability
