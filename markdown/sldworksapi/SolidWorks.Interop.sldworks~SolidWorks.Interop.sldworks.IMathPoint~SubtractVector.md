---
title: "SubtractVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "SubtractVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.html"
---

# SubtractVector Method (IMathPoint)

Gets a math point that describes the difference between a math vector's magnitude from the calling math point

## Syntax

### Visual Basic (Declaration)

```vb
Function SubtractVector( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim VectorObjIn As System.Object
Dim value As System.Object

value = instance.SubtractVector(VectorObjIn)
```

### C#

```csharp
System.object SubtractVector(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.Object^ SubtractVector(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) by which to subtract this math point

### Return Value

Newly created [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::SubtractVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~SubtractVector.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
