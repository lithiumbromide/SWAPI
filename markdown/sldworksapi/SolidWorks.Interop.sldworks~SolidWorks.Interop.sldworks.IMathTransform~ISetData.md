---
title: "ISetData Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "ISetData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.html"
---

# ISetData Method (IMathTransform)

Sets the math vectors and data that describe the transformation matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetData( _
   ByVal XAxisObjIn As MathVector, _
   ByVal YAxisObjIn As MathVector, _
   ByVal ZAxisObjIn As MathVector, _
   ByVal TransformObjIn As MathVector, _
   ByVal ScaleValIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim XAxisObjIn As MathVector
Dim YAxisObjIn As MathVector
Dim ZAxisObjIn As MathVector
Dim TransformObjIn As MathVector
Dim ScaleValIn As System.Double

instance.ISetData(XAxisObjIn, YAxisObjIn, ZAxisObjIn, TransformObjIn, ScaleValIn)
```

### C#

```csharp
void ISetData(
   MathVector XAxisObjIn,
   MathVector YAxisObjIn,
   MathVector ZAxisObjIn,
   MathVector TransformObjIn,
   System.double ScaleValIn
)
```

### C++/CLI

```cpp
void ISetData(
   MathVector^ XAxisObjIn,
   MathVector^ YAxisObjIn,
   MathVector^ ZAxisObjIn,
   MathVector^ TransformObjIn,
   System.double ScaleValIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAxisObjIn`: X rotation [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object of the transform
- `YAxisObjIn`: Y rotation [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object of the transform
- `ZAxisObjIn`: Z rotation [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object of the transform
- `TransformObjIn`: Translation [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object of the transform
- `ScaleValIn`: Scale component of the transform

## VBA Syntax

See [MathTransform::ISetData](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~ISetData.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::SetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.html)
[IMathTransform::GetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.html)
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
