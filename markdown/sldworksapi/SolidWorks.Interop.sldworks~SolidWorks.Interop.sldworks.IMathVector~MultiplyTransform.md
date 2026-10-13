---
title: "MultiplyTransform Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "MultiplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~MultiplyTransform.html"
---

# MultiplyTransform Method (IMathVector)

Multiplies this math vector by the specified math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiplyTransform( _
   ByVal TransformObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim TransformObjIn As System.Object
Dim value As System.Object

value = instance.MultiplyTransform(TransformObjIn)
```

### C#

```csharp
System.object MultiplyTransform(
   System.object TransformObjIn
)
```

### C++/CLI

```cpp
System.Object^ MultiplyTransform(
   System.Object^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) by which to multiply the math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::MultiplyTransform](ms-its:sldworksapivb6.chm::/sldworks~MathVector~MultiplyTransform.html).

## Examples

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IMultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IMultiplyTransform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
