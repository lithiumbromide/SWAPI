---
title: "IsVirtualComponent2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsVirtualComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent2.html"
---

# IsVirtualComponent2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IsVirtualComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsVirtualComponent2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.IsVirtualComponent2()
```

### C#

```csharp
System.object IsVirtualComponent2()
```

### C++/CLI

```cpp
System.Object^ IsVirtualComponent2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Fully qualified paths to parent assembly components, up to and including the first non-virtual parent assembly component, if the model is a virtual component

## VBA Syntax

See [ModelDocExtension::IsVirtualComponent2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsVirtualComponent2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)

## Availability

SOLIDWORKS 2008 SP3, Revision Number 16.3
