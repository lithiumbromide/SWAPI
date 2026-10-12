---
title: "SetTransformAndSolve Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetTransformAndSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve.html"
---

# SetTransformAndSolve Method (IComponent2)

Obsolete. Superseded by [IComponent2::SetTransformAndSolve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetTransformAndSolve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTransformAndSolve( _
   ByVal XformIn As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim XformIn As MathTransform
Dim value As System.Boolean

value = instance.SetTransformAndSolve(XformIn)
```

### C#

```csharp
System.bool SetTransformAndSolve(
   MathTransform XformIn
)
```

### C++/CLI

```cpp
System.bool SetTransformAndSolve(
   MathTransform^ XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Component2::SetTransformAndSolve](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetTransformAndSolve.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
