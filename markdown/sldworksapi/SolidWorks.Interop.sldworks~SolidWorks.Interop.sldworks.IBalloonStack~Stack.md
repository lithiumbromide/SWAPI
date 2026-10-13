---
title: "Stack Property (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "Stack"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Stack.html"
---

# Stack Property (IBalloonStack)

Gets the stacked notes in this balloon stack, excluding the master balloon.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Stack As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim value As System.Object

value = instance.Stack
```

### C#

```csharp
System.object Stack {get;}
```

### C++/CLI

```cpp
property System.Object^ Stack {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array notes in the balloon stack

## VBA Syntax

See [BalloonStack::Stack](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~Stack.html).

## Remarks

This method does not return the master balloon in the stack, only the other stacked notes. Use [IBalloonStack::Master](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Master.html) to get the master balloon of the stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)
[IBalloonStack::IGetStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~IGetStack.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
