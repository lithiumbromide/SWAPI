---
title: "Direction Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Direction.html"
---

# Direction Property (IDragArrowManipulator)

Gets or sets the direction of the handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As MathVector

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
MathVector Direction {get; set;}
```

### C++/CLI

```cpp
property MathVector^ Direction {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object

## VBA Syntax

See [DragArrowManipulator::Direction](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~Direction.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
