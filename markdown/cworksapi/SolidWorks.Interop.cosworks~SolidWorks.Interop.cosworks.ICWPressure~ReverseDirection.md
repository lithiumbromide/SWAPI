---
title: "ReverseDirection Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "ReverseDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~ReverseDirection.html"
---

# ReverseDirection Property (ICWPressure)

Obsolete. Superseded by [ICWPressure::ReverseDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~ReverseDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.int ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse direction, 0 to not

## VBA Syntax

See [CWPressure::ReverseDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~ReverseDirection.html).

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::Value Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Value.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
