---
title: "ISetXform Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "ISetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~ISetXform.html"
---

# ISetXform Method (IComponent)

Obsolete. Superseded by [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetXform( _
   ByRef XformIn As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim XformIn As System.Double
Dim value As System.Boolean

value = instance.ISetXform(XformIn)
```

### C#

```csharp
System.bool ISetXform(
   ref System.double XformIn
)
```

### C++/CLI

```cpp
System.bool ISetXform(
   System.double% XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Component::ISetXform](ms-its:sldworksapivb6.chm::/sldworks~Component~ISetXform.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
