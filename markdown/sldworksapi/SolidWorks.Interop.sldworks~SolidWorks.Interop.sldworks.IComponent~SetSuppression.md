---
title: "SetSuppression Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "SetSuppression"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetSuppression.html"
---

# SetSuppression Method (IComponent)

Obsolete. Superseded by [IComponent2::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSuppression2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSuppression( _
   ByVal State As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim State As System.Integer
Dim value As System.Integer

value = instance.SetSuppression(State)
```

### C#

```csharp
System.int SetSuppression(
   System.int State
)
```

### C++/CLI

```cpp
System.int SetSuppression(
   System.int State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`:

## VBA Syntax

See [Component::SetSuppression](ms-its:sldworksapivb6.chm::/sldworks~Component~SetSuppression.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
