---
title: "ConvertToMultiJog Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "ConvertToMultiJog"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ConvertToMultiJog.html"
---

# ConvertToMultiJog Method (IAnnotation)

Converts a note with a leader to a note with a multi-jog leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToMultiJog( _
   ByVal LeaderNumber As System.Integer, _
   ByVal NumberOfPoints As System.Integer, _
   ByVal PointsData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim LeaderNumber As System.Integer
Dim NumberOfPoints As System.Integer
Dim PointsData As System.Object
Dim value As System.Boolean

value = instance.ConvertToMultiJog(LeaderNumber, NumberOfPoints, PointsData)
```

### C#

```csharp
System.bool ConvertToMultiJog(
   System.int LeaderNumber,
   System.int NumberOfPoints,
   System.object PointsData
)
```

### C++/CLI

```cpp
System.bool ConvertToMultiJog(
   System.int LeaderNumber,
   System.int NumberOfPoints,
   System.Object^ PointsData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LeaderNumber`: Number of the leader to convert in the 0-based list of leaders
- `NumberOfPoints`: Number of jog points
- `PointsData`: Array of doubles, whose size is 3*NumberOfPoints, that specify the points where to locate the jogs; the points are in sheet space

### Return Value

True if the leader is converted to a multi-jog leader, false if not

## VBA Syntax

See [Annotation::ConvertToMultiJog](ms-its:sldworksapivb6.chm::/sldworks~Annotation~ConvertToMultiJog.html).

## Examples

```vb
Visual Basic for Applications (VBA)

' Convert the first leader of the note to a two-point multi-jog leader
...
Dim vPointData as Variant
Dim nPoints (0 to 6) as Double
nPoints(0) = 0.189013
nPoints(1) = 0.248742
nPoints(2) = -1.75647E-15
nPoints(3) = 0.252176
nPoints(4) = 0.186859
nPoints(5) = -1.32434E-15
...
vPointData = nPoints
boolstatus = Annotation.ConvertToMultiJog(0, 2, (vPointData))
...
```

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
