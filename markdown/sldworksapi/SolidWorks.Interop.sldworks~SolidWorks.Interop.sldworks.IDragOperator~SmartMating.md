---
title: "SmartMating Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "SmartMating"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SmartMating.html"
---

# SmartMating Property (IDragOperator)

Gets or sets SmartMates.

## Syntax

### Visual Basic (Declaration)

```vb
Property SmartMating As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.SmartMating = value

value = instance.SmartMating
```

### C#

```csharp
System.bool SmartMating {get; set;}
```

### C++/CLI

```cpp
property System.bool SmartMating {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RUE enables SmartMates, false disables it

## VBA Syntax

See [DragOperator::SmartMating](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~SmartMating.html).

## Remarks

SmartMates is an assembly mating relation that SOLIDWORKS creates automatically.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
