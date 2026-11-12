---
title: "Update Method (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "Update"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Update.html"
---

# Update Method (IDragArrowManipulator)

Displays a handle after having modified the length of the handle.

## Syntax

### Visual Basic (Declaration)

```vb
Function Update() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Boolean

value = instance.Update()
```

### C#

```csharp
System.bool Update()
```

### C++/CLI

```cpp
System.bool Update();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the length of the handle was updated, false if not

## VBA Syntax

See [DragArrowManipulator::Update](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~Update.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

To change the length of a handle, use [IDragArrowManipulator::Length](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~Length.html) or [IDragArrowManipulator::LengthOppositeDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.html), then use this method to see display the modified handle in the graphics area.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.html)
[IDragArrowManipulator::LengthOppositeDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
