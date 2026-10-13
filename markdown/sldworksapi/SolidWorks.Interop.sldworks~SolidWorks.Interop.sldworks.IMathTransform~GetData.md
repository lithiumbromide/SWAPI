---
title: "GetData Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "GetData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData.html"
---

# GetData Method (IMathTransform)

Obsolete. See [IMathTransform::GetData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~GetData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetData( _
   ByRef XAxisObjOut As System.Object, _
   ByRef YAxisObjOut As System.Object, _
   ByRef ZAxisObjOut As System.Object, _
   ByRef TransformObjOut As System.Object, _
   ByRef ScaleOut As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim XAxisObjOut As System.Object
Dim YAxisObjOut As System.Object
Dim ZAxisObjOut As System.Object
Dim TransformObjOut As System.Object
Dim ScaleOut As System.Double

instance.GetData(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

### C#

```csharp
void GetData(
   out System.object XAxisObjOut,
   out System.object YAxisObjOut,
   out System.object ZAxisObjOut,
   out System.object TransformObjOut,
   out System.double ScaleOut
)
```

### C++/CLI

```cpp
void GetData(
   [Out] System.Object^ XAxisObjOut,
   [Out] System.Object^ YAxisObjOut,
   [Out] System.Object^ ZAxisObjOut,
   [Out] System.Object^ TransformObjOut,
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

See [MathTransform::GetData](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~GetData.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
