---
title: "SetMaterialUserName Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "SetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetMaterialUserName.html"
---

# SetMaterialUserName Method (IComponent)

Obsolete. Superseded by [IComponent2::SetMaterialUserName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetMaterialUserName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialUserName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialUserName(Name)
```

### C#

```csharp
System.bool SetMaterialUserName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialUserName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [Component::SetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Component~SetMaterialUserName.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
