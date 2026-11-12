---
title: "BorderLineWeightCustom Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "BorderLineWeightCustom"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom.html"
---

# BorderLineWeightCustom Property (ITableAnnotation)

Gets or sets the line weight of the border lines to the specified custom weight for this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property BorderLineWeightCustom As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Double

instance.BorderLineWeightCustom = value

value = instance.BorderLineWeightCustom
```

### C#

```csharp
System.double BorderLineWeightCustom {get; set;}
```

### C++/CLI

```cpp
property System.double BorderLineWeightCustom {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Custom weight, in millimeters, of border lines for this table

## VBA Syntax

See [TableAnnotation::BorderLineWeightCustom](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~BorderLineWeightCustom.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
