---
title: "IGetLeaderPoints Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "IGetLeaderPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.html"
---

# IGetLeaderPoints Method (ISketchBlockInstance)

Gets the coordinate information for the leader on this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderPoints() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Double

value = instance.IGetLeaderPoints()
```

### C#

```csharp
System.double IGetLeaderPoints()
```

### C++/CLI

```cpp
System.double IGetLeaderPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array containing leader point information (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[ISketchBlockInstance::GetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.html)
[ISketchBlockInstance::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
