---
title: "Origin Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "Origin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Origin.html"
---

# Origin Property (IDragArrowManipulator)

Gets or sets the origin of the handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property Origin As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As MathPoint

instance.Origin = value

value = instance.Origin
```

### C#

```csharp
MathPoint Origin {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ Origin {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object

## VBA Syntax

See [DragArrowManipulator::Origin](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~Origin.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

Before calling this property to change the origin setting, set [IDragArrowManipulator::FixedLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~FixedLength.html) to true.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
