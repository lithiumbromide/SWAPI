---
title: "Length Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.html"
---

# Length Property (IDragArrowManipulator)

Gets or sets the length of the handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Double

instance.Length = value

value = instance.Length
```

### C#

```csharp
System.double Length {get; set;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of handle

## VBA Syntax

See [DragArrowManipulator::Length](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~Length.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

If you change the length of the handle using this property, then use [IDragArrowMainpulator::Update](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~Update.html) to display the modified handle in the graphics area.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[IDragArrowManipulator::LengthOppositeDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
