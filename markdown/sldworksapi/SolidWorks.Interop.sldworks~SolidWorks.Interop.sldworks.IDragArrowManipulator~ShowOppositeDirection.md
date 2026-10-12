---
title: "ShowOppositeDirection Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "ShowOppositeDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~ShowOppositeDirection.html"
---

# ShowOppositeDirection Property (IDragArrowManipulator)

Gets or sets whether to display the bidirectional handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowOppositeDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Boolean

instance.ShowOppositeDirection = value

value = instance.ShowOppositeDirection
```

### C#

```csharp
System.bool ShowOppositeDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowOppositeDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the bidirectional handle, false to display the unidirectional handle

## VBA Syntax

See [DragArrowManipulator::ShowOppositeDirection](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~ShowOppositeDirection.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[IDragArrowManipulator::AllowFlip Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~AllowFlip.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
