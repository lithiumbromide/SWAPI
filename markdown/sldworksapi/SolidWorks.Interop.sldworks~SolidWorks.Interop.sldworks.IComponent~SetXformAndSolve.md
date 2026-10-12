---
title: "SetXformAndSolve Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "SetXformAndSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetXformAndSolve.html"
---

# SetXformAndSolve Method (IComponent)

Obsolete. Superseded by [IComponent2::SetTransformAndSolve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetTransformAndSolve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetXformAndSolve( _
   ByVal XformIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim XformIn As System.Object
Dim value As System.Boolean

value = instance.SetXformAndSolve(XformIn)
```

### C#

```csharp
System.bool SetXformAndSolve(
   System.object XformIn
)
```

### C++/CLI

```cpp
System.bool SetXformAndSolve(
   System.Object^ XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Component::SetXformAndSolve](ms-its:sldworksapivb6.chm::/sldworks~Component~SetXformAndSolve.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
