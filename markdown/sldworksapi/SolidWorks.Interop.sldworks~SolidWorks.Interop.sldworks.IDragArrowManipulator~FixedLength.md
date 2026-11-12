---
title: "FixedLength Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "FixedLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~FixedLength.html"
---

# FixedLength Property (IDragArrowManipulator)

Gets or sets whether the origin can be changed.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Boolean

instance.FixedLength = value

value = instance.FixedLength
```

### C#

```csharp
System.bool FixedLength {get; set;}
```

### C++/CLI

```cpp
property System.bool FixedLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to permit changing the origin, false to not

## VBA Syntax

See [DragArrowManipulator::FixedLength](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~FixedLength.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

Set this property to true before calling [IDragArrowManipulator::Origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~Origin.html) to change the origin.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.html)
[IDragArrowManipulator::LengthOppositeDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
