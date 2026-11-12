---
title: "ShowRuler Property (IDragArrowManipulator)"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: "ShowRuler"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~ShowRuler.html"
---

# ShowRuler Property (IDragArrowManipulator)

Gets or sets whether to display a ruler when the handle moves.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowRuler As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
Dim value As System.Boolean

instance.ShowRuler = value

value = instance.ShowRuler
```

### C#

```csharp
System.bool ShowRuler {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowRuler {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display a ruler when the handle moves, false to not

## VBA Syntax

See [DragArrowManipulator::ShowRuler](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator~ShowRuler.html).

## Examples

See [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html) examples.

## See Also

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
