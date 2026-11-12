---
title: "SetTargetPoint Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "SetTargetPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.html"
---

# SetTargetPoint Method (ICallout)

Sets the target point for the specified row in this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTargetPoint( _
   ByVal RowID As System.Integer, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double

instance.SetTargetPoint(RowID, XPos, YPos, ZPos)
```

### C#

```csharp
void SetTargetPoint(
   System.int RowID,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

### C++/CLI

```cpp
void SetTargetPoint(
   System.int RowID,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row in callout
- `XPos`: x coordinate for this target point
- `YPos`: y coordinate for this target point
- `ZPos`: z coordinate for this target poi

## VBA Syntax

See [Callout::SetTargetPoint](ms-its:sldworksapivb6.chm::/sldworks~Callout~SetTargetPoint.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::GetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint.html)
[ICallout::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
