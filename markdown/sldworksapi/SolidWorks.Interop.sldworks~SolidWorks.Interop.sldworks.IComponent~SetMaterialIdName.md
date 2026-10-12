---
title: "SetMaterialIdName Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "SetMaterialIdName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetMaterialIdName.html"
---

# SetMaterialIdName Method (IComponent)

Obsolete. Superseded by [IComponent2::SetMaterialIdName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetMaterialIdName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialIdName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialIdName(Name)
```

### C#

```csharp
System.bool SetMaterialIdName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialIdName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [Component::SetMaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Component~SetMaterialIdName.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
