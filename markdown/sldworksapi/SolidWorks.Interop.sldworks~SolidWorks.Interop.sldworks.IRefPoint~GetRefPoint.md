---
title: "GetRefPoint Method (IRefPoint)"
project: "SOLIDWORKS API Help"
interface: "IRefPoint"
member: "GetRefPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint~GetRefPoint.html"
---

# GetRefPoint Method (IRefPoint)

Gets the parameters for this reference point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRefPoint() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPoint
Dim value As MathPoint

value = instance.GetRefPoint()
```

### C#

```csharp
MathPoint GetRefPoint()
```

### C++/CLI

```cpp
MathPoint^ GetRefPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Parameters for this reference point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [RefPoint::GetRefPoint](ms-its:sldworksapivb6.chm::/sldworks~RefPoint~GetRefPoint.html).

## Examples

[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)
[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)

## See Also

[IRefPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)
[IRefPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
