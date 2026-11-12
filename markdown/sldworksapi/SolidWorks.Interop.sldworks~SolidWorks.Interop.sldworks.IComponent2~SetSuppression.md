---
title: "SetSuppression Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetSuppression"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression.html"
---

# SetSuppression Method (IComponent2)

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
Dim instance As IComponent2
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

See [Component2::SetSuppression](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetSuppression.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
