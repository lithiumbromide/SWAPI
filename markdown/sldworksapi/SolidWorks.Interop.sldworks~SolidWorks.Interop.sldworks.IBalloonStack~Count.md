---
title: "Count Property (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "Count"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Count.html"
---

# Count Property (IBalloonStack)

Gets the number of stacked notes in this balloon stack, excluding the master balloon.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of balloons in this balloon stack, excluding the master balloon

## VBA Syntax

See [BalloonStack::Count](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~Count.html).

## Remarks

This property does not count the master balloon in the stack, only the other stacked notes. Us [IBalloonStack::Master](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Master.html) to get the master balloon of the stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
