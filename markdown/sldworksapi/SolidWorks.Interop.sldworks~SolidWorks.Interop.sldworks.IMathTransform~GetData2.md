---
title: "GetData2 Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "GetData2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.html"
---

# GetData2 Method (IMathTransform)

Gets the math vectors and data that describe the transformation matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetData2( _
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

instance.GetData2(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

### C#

```csharp
void GetData2(
   out System.object XAxisObjOut,
   out System.object YAxisObjOut,
   out System.object ZAxisObjOut,
   out System.object TransformObjOut,
   out System.double ScaleOut
)
```

### C++/CLI

```cpp
void GetData2(
   [Out] System.Object^ XAxisObjOut,
   [Out] System.Object^ YAxisObjOut,
   [Out] System.Object^ ZAxisObjOut,
   [Out] System.Object^ TransformObjOut,
   [Out] System.double ScaleOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAxisObjOut`: [Rotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) about the x axis
- `YAxisObjOut`: [Rotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) about the y axis
- `ZAxisObjOut`: [Rotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) about the z axis
- `TransformObjOut`: [Transformation vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)
- `ScaleOut`: Scale

### Return Value

The previous version of this method, [IMathTransform::GetData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform~GetData.html), returned inversed x, y, z axes. This version of this method returns the actual x, y, z axes.

## VBA Syntax

See [MathTransform::GetData2](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~GetData2.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.html)
[IMathTransform::ISetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.html)
[IMathTransform::SetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
