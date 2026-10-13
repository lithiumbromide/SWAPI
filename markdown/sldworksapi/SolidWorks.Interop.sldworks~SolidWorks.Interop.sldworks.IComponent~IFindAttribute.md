---
title: "IFindAttribute Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IFindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IFindAttribute.html"
---

# IFindAttribute Method (IComponent)

Obsolete. Superseded by [IComponent2::IFindAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IFindAttribute.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute

value = instance.IFindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
Attribute IFindAttribute(
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
Attribute^ IFindAttribute(
   AttributeDef^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`:
- `WhichOne`:

## VBA Syntax

See [Component::IFindAttribute](ms-its:sldworksapivb6.chm::/sldworks~Component~IFindAttribute.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
