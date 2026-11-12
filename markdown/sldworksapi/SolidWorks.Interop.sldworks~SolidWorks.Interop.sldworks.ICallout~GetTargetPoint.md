---
title: "GetTargetPoint Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "GetTargetPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint.html"
---

# GetTargetPoint Method (ICallout)

Gets the target point for the specified row in this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetTargetPoint( _
   ByVal RowID As System.Integer, _
   ByRef XPos As System.Double, _
   ByRef YPos As System.Double, _
   ByRef ZPos As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double

instance.GetTargetPoint(RowID, XPos, YPos, ZPos)
```

### C#

```csharp
void GetTargetPoint(
   System.int RowID,
   out System.double XPos,
   out System.double YPos,
   out System.double ZPos
)
```

### C++/CLI

```cpp
void GetTargetPoint(
   System.int RowID,
   [Out] System.double XPos,
   [Out] System.double YPos,
   [Out] System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row in callout
- `XPos`: x coordinate of target point
- `YPos`: y coordinate of target point
- `ZPos`: z coordinate of target point

## VBA Syntax

See [Callout::GetTargetPoint](ms-its:sldworksapivb6.chm::/sldworks~Callout~GetTargetPoint.html).

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::SetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.html)
[ICallout::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
