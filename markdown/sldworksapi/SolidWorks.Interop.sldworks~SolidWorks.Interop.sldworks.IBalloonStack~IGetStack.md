---
title: "IGetStack Method (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "IGetStack"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~IGetStack.html"
---

# IGetStack Method (IBalloonStack)

Gets the stacked notes in this balloon stack, excluding the master balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStack( _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim Count As System.Integer
Dim value As Note

value = instance.IGetStack(Count)
```

### C#

```csharp
Note IGetStack(
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetStack(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of balloons

### Return Value

- in-process, unmanaged C++: Pointer to an array of stacked [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) of size Count in the balloon stack

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use [IBalloonStack::Count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Count.html) to get the number of balloons in the balloon stack.

This method does not return the master balloon in the stack, only the other stacked notes. Use [IBalloonStack::Master](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Master.html) to get the master balloon of the stack.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)
[IBalloonStack::Stack Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Stack.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number
