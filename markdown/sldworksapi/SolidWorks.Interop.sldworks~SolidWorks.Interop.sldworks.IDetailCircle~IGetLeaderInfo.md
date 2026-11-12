---
title: "IGetLeaderInfo Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "IGetLeaderInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetLeaderInfo.html"
---

# IGetLeaderInfo Method (IDetailCircle)

Gets the leader information for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Double

value = instance.IGetLeaderInfo()
```

### C#

```csharp
System.double IGetLeaderInfo()
```

### C++/CLI

```cpp
System.double IGetLeaderInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [DetailCircle::IGetLeaderInfo](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~IGetLeaderInfo.html).

## Remarks

There can be 0, 1 or 2 lines in the leader line. If the GTol is not attached, there are 0 lines. Otherwise, leaders can use a straight leaderline (1 line) or a bent leaderline (2 lines). Your applications must infer the number of leader lines based on [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) and [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html).

- IsAttached() == false implies no leaderline; therefore, no leaderline points (PointCount=0).
- HasExtraLeader() == false means that this is a straight leaderline; therefore, 1 line (PointCount=2)
- HasExtraLeader() == True means that this is a bent leaderline; therefore, 2 lines (PointCount=3)

Format of return information is the following array of doubles:

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

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLeaderInfo.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
