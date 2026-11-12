---
title: "IGetReferencePoints Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IGetReferencePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.html"
---

# IGetReferencePoints Method (IDimension)

Gets the reference points for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetReferencePoints( _
   ByVal PointsCount As System.Integer _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim PointsCount As System.Integer
Dim value As MathPoint

value = instance.IGetReferencePoints(PointsCount)
```

### C#

```csharp
MathPoint IGetReferencePoints(
   System.int PointsCount
)
```

### C++/CLI

```cpp
MathPoint^ IGetReferencePoints(
   System.int PointsCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointsCount`: Number of reference points for this dimension

### Return Value

- in-process, unmanaged C++: Pointer to the [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IDimension::IGetReferencePointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetReferencePointsCount.html) before calling this method to determine the size of the array.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.html)
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
