---
title: "GetLeaderPointsAtIndex Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetLeaderPointsAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.html"
---

# GetLeaderPointsAtIndex Method (IAnnotation)

Gets coordinate information about a specified leader on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderPointsAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLeaderPointsAtIndex(Index)
```

### C#

```csharp
System.object GetLeaderPointsAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLeaderPointsAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader within this annotation (see **Remarks**)

### Return Value

Array of objects (see **Remarks**)

## VBA Syntax

See [Annotation::GetLeaderPointsAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetLeaderPointsAtIndex.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)

## Remarks

The index value is 0-based. Therefore, a valid index value is >= 0 < number of leaders on this annotation.

Use [IAnnotation::GetLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetLeaderCount.html) to find out how many leaders are on this annotation. If the index value is invalid in Visual Basic for Applications (VBA), SOLIDWORKS returns an empty SafeArray or S_false.

You must determine the number of points in the leader to use the data returned by this method. The number of points is a function of the number of segments in the leader. There can be one or two segments in a leader line, depending on whether or not it is a straight, bent, or underlined leader. Use [IAnnotation::GetLeaderStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetLeaderStyle.html)
to determine the number of points in the leader.

- If IAnnotation::GetLeaderStyle returns swNO_LEADER, then the number of points = 0.
- If IAnnotation::GetLeaderStyle returns swSTRAIGHT and swUNDERLINED then the number
  of points = 2.
- If IAnnotation::GetLeaderStyle returns swBENT, then the number of points = 3.

Additionally, for the COM interface, you must determine the number of points to allocate the appropriate size array for the return value. The number of points must also be passed to the method to help prevent overwrite problems if you have not allocated an array that is the correct size. If the number of points passed does not match what is found, SOLIDWORKS does not return any point information and returns S_false.

The format of the return array is:

retval[0] = X-coordinate of first leader point

retval[1] = Y-coordinate of first leader point

retval[2] = Z-coordinate of first leader point

retval[3] = X-coordinate of second leader point

retval[4] = Y-coordinate of second leader point

retval[5] = Z-coordinate of second leader point

retval[6] = X-coordinate of third leader point

retval[7] = Y-coordinate of third leader point

retval[8] = Z-coordinate of third leader point

You cannot directly set the leader coordinate information. The leader coordinates are computed based on the annotations text and attachment points. Use [IAnnotation::GetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetPosition.html) and [IAnnotation::SetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetPosition.html) to get and set the text point.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetDashedLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.html)
[IAnnotation::GetLeaderAllAround Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.html)
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.html)
[IAnnotation::GetLeaderSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::IGetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetLeaderPointsAtIndex.html)
[IAnnotation::SetLeader3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)
[IAnnotation::SetLeaderAttachmentPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex.html)

## Availability

SOLIDWORKS 99, datecode 1999207
