---
title: "UpdatePosition Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "UpdatePosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~UpdatePosition.html"
---

# UpdatePosition Method (ICallout)

Obsolete. Superseded by [Callout::Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~Position.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdatePosition( _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double

instance.UpdatePosition(XPos, YPos, ZPos)
```

### C#

```csharp
void UpdatePosition(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

### C++/CLI

```cpp
void UpdatePosition(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPos`: x coordinate for callout
- `YPos`: y coordinate for callout
- `ZPos`: z coordinate for callout

## VBA Syntax

See [Callout::UpdatePosition](ms-its:sldworksapivb6.chm::/sldworks~Callout~UpdatePosition.html).

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
