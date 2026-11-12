---
title: "Name2 Property (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "Name2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~Name2.html"
---

# Name2 Property (IComponent)

Obsolete. Superseded by [IComponent2::Name2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Name2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Name2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim value As System.String

instance.Name2 = value

value = instance.Name2
```

### C#

```csharp
System.string Name2 {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component::Name2](ms-its:sldworksapivb6.chm::/sldworks~Component~Name2.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
