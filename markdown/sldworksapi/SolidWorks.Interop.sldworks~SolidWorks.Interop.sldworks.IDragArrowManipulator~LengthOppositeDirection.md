---
title: "LengthOppositeDirection Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "LengthOppositeDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.html"
---

# LengthOppositeDirection Property (IDragArrowManipulator)

Gets or sets the length of the opposite handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthOppositeDirection As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Double

instance.LengthOppositeDirection = value

value = instance.LengthOppositeDirection
```

### C#

```csharp
System.double LengthOppositeDirection {get; set;}
```

### C++/CLI

```cpp
property System.double LengthOppositeDirection {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of opposite handle

## VBA Syntax

See [DragArrowManipulator::LengthOppositeDirection](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~LengthOppositeDirection.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

If you change the length of the handle using this property, then use [IDragArrowMainpulator::Update](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~Update.html) to display the modified handle in the graphics area.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
