---
title: "FindAttribute Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "FindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~FindAttribute.html"
---

# FindAttribute Method (IComponent)

Obsolete. Superseded by [IComponent2::FindAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FindAttribute.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FindAttribute( _
   ByVal AttributeDef As System.Object, _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim AttributeDef As System.Object
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.FindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
System.object FindAttribute(
   System.object AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ FindAttribute(
   System.Object^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`:
- `WhichOne`:

## VBA Syntax

See [Component::FindAttribute](ms-its:sldworksapivb6.chm::/sldworks~Component~FindAttribute.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
