---
title: "ISubtract Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "ISubtract"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtract.html"
---

# ISubtract Method (IMathPoint)

Gets a math vector that describes the difference between the math point magnitude from the calling math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISubtract( _
   ByVal PointObjIn As MathPoint _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim PointObjIn As MathPoint
Dim value As MathVector

value = instance.ISubtract(PointObjIn)
```

### C#

```csharp
MathVector ISubtract(
   MathPoint PointObjIn
)
```

### C++/CLI

```cpp
MathVector^ ISubtract(
   MathPoint^ PointObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointObjIn`: [Math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) by which to subtract this math point

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::ISubtract](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~ISubtract.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Subtract.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
