---
title: "Subtract Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "Subtract"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Subtract.html"
---

# Subtract Method (IMathPoint)

Gets a math vector that describes the difference between the math point magnitude from the calling math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function Subtract( _
   ByVal PointObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim PointObjIn As System.Object
Dim value As System.Object

value = instance.Subtract(PointObjIn)
```

### C#

```csharp
System.object Subtract(
   System.object PointObjIn
)
```

### C++/CLI

```cpp
System.Object^ Subtract(
   System.Object^ PointObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointObjIn`: [Math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) by which to subtract this math point

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::Subtract](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~Subtract.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtract.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
