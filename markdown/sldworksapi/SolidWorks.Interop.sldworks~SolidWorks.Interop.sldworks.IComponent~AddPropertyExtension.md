---
title: "AddPropertyExtension Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IComponent)

Obsolete. Superseded by [IComponent2::AddPropertyExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~AddPropertyExtension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`:

## VBA Syntax

See [Component::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Component~AddPropertyExtension.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
