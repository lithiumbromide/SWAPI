---
title: "ICreatePsplineSurfaceDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreatePsplineSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreatePsplineSurfaceDLL.html"
---

# ICreatePsplineSurfaceDLL Method (IBody)

Obsolete. Superseded by [IBody2::ICreatePsplineSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePsplineSurfaceDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePsplineSurfaceDLL( _
   ByVal Dim As System.Integer, _
   ByVal UOrder As System.Integer, _
   ByVal VOrder As System.Integer, _
   ByVal Ncol As System.Integer, _
   ByVal Nrow As System.Integer, _
   ByRef Coeffs As System.Double, _
   ByVal Basis As System.Integer, _
   ByRef Xform As System.Double, _
   ByVal ScaleFactor As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Dim As System.Integer
Dim UOrder As System.Integer
Dim VOrder As System.Integer
Dim Ncol As System.Integer
Dim Nrow As System.Integer
Dim Coeffs As System.Double
Dim Basis As System.Integer
Dim Xform As System.Double
Dim ScaleFactor As System.Double
Dim value As Surface

value = instance.ICreatePsplineSurfaceDLL(Dim, UOrder, VOrder, Ncol, Nrow, Coeffs, Basis, Xform, ScaleFactor)
```

### C#

```csharp
Surface ICreatePsplineSurfaceDLL(
   System.int Dim,
   System.int UOrder,
   System.int VOrder,
   System.int Ncol,
   System.int Nrow,
   ref System.double Coeffs,
   System.int Basis,
   ref System.double Xform,
   System.double ScaleFactor
)
```

### C++/CLI

```cpp
Surface^ ICreatePsplineSurfaceDLL(
   System.int Dim,
   System.int UOrder,
   System.int VOrder,
   System.int Ncol,
   System.int Nrow,
   System.double% Coeffs,
   System.int Basis,
   System.double% Xform,
   System.double ScaleFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Dim`:
- `UOrder`:
- `VOrder`:
- `Ncol`:
- `Nrow`:
- `Coeffs`:
- `Basis`:
- `Xform`:
- `ScaleFactor`:

## VBA Syntax

See [Body::ICreatePsplineSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreatePsplineSurfaceDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
