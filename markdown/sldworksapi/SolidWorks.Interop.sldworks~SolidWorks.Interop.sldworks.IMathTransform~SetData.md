---
title: "SetData Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "SetData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.html"
---

# SetData Method (IMathTransform)

Sets the math vectors and data that describe the transformation matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetData( _
   ByVal XAxisObjIn As System.Object, _
   ByVal YAxisObjIn As System.Object, _
   ByVal ZAxisObjIn As System.Object, _
   ByVal TransformObjIn As System.Object, _
   ByVal ScaleValIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim XAxisObjIn As System.Object
Dim YAxisObjIn As System.Object
Dim ZAxisObjIn As System.Object
Dim TransformObjIn As System.Object
Dim ScaleValIn As System.Double

instance.SetData(XAxisObjIn, YAxisObjIn, ZAxisObjIn, TransformObjIn, ScaleValIn)
```

### C#

```csharp
void SetData(
   System.object XAxisObjIn,
   System.object YAxisObjIn,
   System.object ZAxisObjIn,
   System.object TransformObjIn,
   System.double ScaleValIn
)
```

### C++/CLI

```cpp
void SetData(
   System.Object^ XAxisObjIn,
   System.Object^ YAxisObjIn,
   System.Object^ ZAxisObjIn,
   System.Object^ TransformObjIn,
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

See [MathTransform::SetData](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~SetData.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::ISetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.html)
[IMathTransform::GetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.html)
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
