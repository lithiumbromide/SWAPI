---
title: "ComposeTransform Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "ComposeTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.html"
---

# ComposeTransform Method (IMathUtility)

Creates a new transform matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Function ComposeTransform( _
   ByVal XVec As MathVector, _
   ByVal YVec As MathVector, _
   ByVal ZVec As MathVector, _
   ByVal TransVec As MathVector, _
   ByVal Scale As System.Double _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim XVec As MathVector
Dim YVec As MathVector
Dim ZVec As MathVector
Dim TransVec As MathVector
Dim Scale As System.Double
Dim value As MathTransform

value = instance.ComposeTransform(XVec, YVec, ZVec, TransVec, Scale)
```

### C#

```csharp
MathTransform ComposeTransform(
   MathVector XVec,
   MathVector YVec,
   MathVector ZVec,
   MathVector TransVec,
   System.double Scale
)
```

### C++/CLI

```cpp
MathTransform^ ComposeTransform(
   MathVector^ XVec,
   MathVector^ YVec,
   MathVector^ ZVec,
   MathVector^ TransVec,
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XVec`: [X-axis of the transform origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)
- `YVec`: [Y-axis of the transform origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)
- `ZVec`: [Z-axis of the transform origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)
- `TransVec`: Translation of the [origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) in space
- `Scale`: Scale factor (typically 1; must be > 0)

### Return Value

New [transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [MathUtility::ComposeTransform](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~ComposeTransform.html).

## Remarks

XVec, YVec and ZVec are expected to be mutually orthogonal. These three vectors can be non-unit vectors and are unitized during the construction of the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html).

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.html)
[IMathUtility::CreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.html)
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.html)
[IMathUtility::ICreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
