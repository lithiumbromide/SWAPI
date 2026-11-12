---
title: "AllowFlip Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "AllowFlip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~AllowFlip.html"
---

# AllowFlip Property (IDragArrowManipulator)

Gets or sets whether the unidirectional handle can change direction when dragged past length = 0.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowFlip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Boolean

instance.AllowFlip = value

value = instance.AllowFlip
```

### C#

```csharp
System.bool AllowFlip {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowFlip {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to allow the unidirectional handle to change direction when dragged past length = 0, false to not (see **Remarks**)

## VBA Syntax

See [DragArrowManipulator::AllowFlip](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~AllowFlip.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## Remarks

This property is valid only if [IDragArrowManipulator::ShowOppositeDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator~ShowOppositeDirection.html) is false.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
