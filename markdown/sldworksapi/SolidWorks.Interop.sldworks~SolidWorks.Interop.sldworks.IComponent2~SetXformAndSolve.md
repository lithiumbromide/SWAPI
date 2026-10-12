---
title: "SetXformAndSolve Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetXformAndSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetXformAndSolve.html"
---

# SetXformAndSolve Method (IComponent2)

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
Dim instance As IComponent2
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

See [Component2::SetXformAndSolve](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetXformAndSolve.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
