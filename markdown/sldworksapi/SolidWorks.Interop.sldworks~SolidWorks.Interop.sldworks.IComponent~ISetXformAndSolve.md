---
title: "ISetXformAndSolve Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "ISetXformAndSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~ISetXformAndSolve.html"
---

# ISetXformAndSolve Method (IComponent)

Obsolete. Superseded by [IComponent2::SetTransformAndSolve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetTransformAndSolve2.html),

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetXformAndSolve( _
   ByRef XformIn As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim XformIn As System.Double
Dim value As System.Boolean

value = instance.ISetXformAndSolve(XformIn)
```

### C#

```csharp
System.bool ISetXformAndSolve(
   ref System.double XformIn
)
```

### C++/CLI

```cpp
System.bool ISetXformAndSolve(
   System.double% XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Component::ISetXformAndSolve](ms-its:sldworksapivb6.chm::/sldworks~Component~ISetXformAndSolve.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
