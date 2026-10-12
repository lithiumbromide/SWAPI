---
title: "ISetXform Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ISetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetXform.html"
---

# ISetXform Method (IComponent2)

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
Dim instance As IComponent2
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

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
