---
title: "Master Property (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "Master"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Master.html"
---

# Master Property (IBalloonStack)

Gets the master note in this balloon stack.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Master As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim value As Note

value = instance.Master
```

### C#

```csharp
Note Master {get;}
```

### C++/CLI

```cpp
property Note^ Master {
   Note^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Master [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) in this balloon stack

## VBA Syntax

See [BalloonStack::Master](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~Master.html).

## Remarks

Use [IBalloonStack::Stack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Stack.html) or [IBalloonStack::IGetStack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~IGetStack.html) to get all of the other balloons in this balloon stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
