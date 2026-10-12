---
title: "GetLeaderPoints Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetLeaderPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.html"
---

# GetLeaderPoints Method (ISketchBlockInstance)

Gets the coordinate information for the leader on this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Object

value = instance.GetLeaderPoints()
```

### C#

```csharp
System.object GetLeaderPoints()
```

### C++/CLI

```cpp
System.Object^ GetLeaderPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing leader point information (see **Remarks**)

## VBA Syntax

See [SketchBlockInstance::GetLeaderPoints](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetLeaderPoints.html).

## Remarks

For the COM interface, you must specify an array size of 9. Depending on the number of points in the leader, this array might only be partially filled upon return from the API. For the OLE Automation interface, the returned SafeArray is sized appropriately for the number of points returned.

You must determine the number of points in the leader to use the data returned by this method. The number of points is a function of the number of segments in the leader. The leader line can have one or two segments depending on whether it is straight or bent. Use [ISketchBlockInstnace::GetLeaderStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.html) to determine the number of points in the leader.

| If SketchBlockInstance::GetLeaderStyle returns... | Then the number of points equals... |
| --- | --- |
| swNO_LEADER | 0 |
| swSTRAIGHT | 2 |
| swBENT | 3 |

The format of the return array is:

- retval[0] = X-coordinate of first leader point
- retval[1] = Y-coordinate of first leader point
- retval[2] = Z-coordinate of first leader point
- retval[3] = X-coordinate of second leader point
- retval[4] = Y-coordinate of second leader point
- retval[5] = Z-coordinate of second leader point
- retval[6] = X-coordinate of third leader point
- retval[7] = Y-coordinate of third leader point
- retval[8] = Z-coordinate of third leader point

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::IGetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.html)
[ISketchBlockInstance::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
