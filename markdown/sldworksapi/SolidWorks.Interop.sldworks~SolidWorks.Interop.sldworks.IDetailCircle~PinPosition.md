---
title: "PinPosition Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "PinPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~PinPosition.html"
---

# PinPosition Property (IDetailCircle)

Sets the pin position for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Property PinPosition As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

instance.PinPosition = value

value = instance.PinPosition
```

### C#

```csharp
System.bool PinPosition {get; set;}
```

### C++/CLI

```cpp
property System.bool PinPosition {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to prevent the detail view from moving if the parent view changes size, false to not

## VBA Syntax

See [DetailCircle::PinPosition](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~PinPosition.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
