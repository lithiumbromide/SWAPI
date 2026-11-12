---
title: "AddVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "AddVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~AddVector.html"
---

# AddVector Method (IMathPoint)

Translates a math point by a math vector to create a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVector( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim VectorObjIn As System.Object
Dim value As System.Object

value = instance.AddVector(VectorObjIn)
```

### C#

```csharp
System.object AddVector(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.Object^ AddVector(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) by which to translate this math point

### Return Value

Newly created translated [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::AddVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~AddVector.html).

## Examples

[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::IAddVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IAddVector.html)
[IMathPoint::SubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.html)
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
