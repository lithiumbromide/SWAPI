---
title: "Direction Property (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Direction.html"
---

# Direction Property (IBalloonStack)

Gets or sets the direction of this balloon stack.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim value As System.Integer

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.int Direction {get; set;}
```

### C++/CLI

```cpp
property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Balloon stacking direction as defined in [swStackedBalloonDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStackedBalloonDirection_e.html)

## VBA Syntax

See [BalloonStack::Direction](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~Direction.html).

## Remarks

f you specify an invalid valid for Direction, SOLIDWORKS does not change the balloon stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
