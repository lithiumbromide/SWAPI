---
title: "SetXform Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "SetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetXform.html"
---

# SetXform Method (IComponent)

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
Dim instance As IComponent
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

See [Component::SetXform](ms-its:sldworksapivb6.chm::/sldworks~Component~SetXform.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
