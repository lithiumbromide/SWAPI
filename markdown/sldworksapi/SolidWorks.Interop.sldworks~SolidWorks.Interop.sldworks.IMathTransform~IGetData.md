---
title: "IGetData Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "IGetData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData.html"
---

# IGetData Method (IMathTransform)

Obsolete. See [IMathTransform::IGetData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~IGetData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetData( _
   ByRef XAxisObjOut As MathVector, _
   ByRef YAxisObjOut As MathVector, _
   ByRef ZAxisObjOut As MathVector, _
   ByRef TransformObjOut As MathVector, _
   ByRef ScaleOut As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim XAxisObjOut As MathVector
Dim YAxisObjOut As MathVector
Dim ZAxisObjOut As MathVector
Dim TransformObjOut As MathVector
Dim ScaleOut As System.Double

instance.IGetData(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

### C#

```csharp
void IGetData(
   out MathVector XAxisObjOut,
   out MathVector YAxisObjOut,
   out MathVector ZAxisObjOut,
   out MathVector TransformObjOut,
   out System.double ScaleOut
)
```

### C++/CLI

```cpp
void IGetData(
   [Out] MathVector^ XAxisObjOut,
   [Out] MathVector^ YAxisObjOut,
   [Out] MathVector^ ZAxisObjOut,
   [Out] MathVector^ TransformObjOut,
   [Out] System.double ScaleOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAxisObjOut`:
- `YAxisObjOut`:
- `ZAxisObjOut`:
- `TransformObjOut`:
- `ScaleOut`:

## VBA Syntax

See [MathTransform::IGetData](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~IGetData.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
