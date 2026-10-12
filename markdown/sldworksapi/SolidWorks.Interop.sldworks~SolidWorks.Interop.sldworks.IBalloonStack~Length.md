---
title: "Length Property (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Length.html"
---

# Length Property (IBalloonStack)

Gets or sets the number of notes that can be stacked before another row is started.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim value As System.Integer

instance.Length = value

value = instance.Length
```

### C#

```csharp
System.int Length {get; set;}
```

### C++/CLI

```cpp
property System.int Length {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum number of balloons in one row of the stack; valid values are from 2 to 100

## VBA Syntax

See [BalloonStack::Length](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~Length.html).

## Remarks

Valid values are from 2 to 100. If you specify an invalid value for Length, SOLIDWORKS oes not change the balloon stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
