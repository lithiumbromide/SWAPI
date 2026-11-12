---
title: "Transform Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Transform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform.html"
---

# Transform Property (IComponent2)

Obsolete. Superseded by [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Transform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As MathTransform

instance.Transform = value

value = instance.Transform
```

### C#

```csharp
MathTransform Transform {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ Transform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component2::Transform](ms-its:sldworksapivb6.chm::/sldworks~Component2~Transform.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
