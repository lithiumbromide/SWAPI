---
title: "SetXform Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetXform.html"
---

# SetXform Method (IComponent2)

Obsolete. Superseded by [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetXform( _
   ByVal XformIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim XformIn As System.Object
Dim value As System.Boolean

value = instance.SetXform(XformIn)
```

### C#

```csharp
System.bool SetXform(
   System.object XformIn
)
```

### C++/CLI

```cpp
System.bool SetXform(
   System.Object^ XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Component2::SetXform](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetXform.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
