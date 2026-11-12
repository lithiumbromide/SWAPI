---
title: "GridLineWeightCustom Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GridLineWeightCustom"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeightCustom.html"
---

# GridLineWeightCustom Property (ITableAnnotation)

Gets or sets the line weight of the inner lines to the specified custom weight for this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property GridLineWeightCustom As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Double

instance.GridLineWeightCustom = value

value = instance.GridLineWeightCustom
```

### C#

```csharp
System.double GridLineWeightCustom {get; set;}
```

### C++/CLI

```cpp
property System.double GridLineWeightCustom {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Custom weight for inner lines in millimeters

## VBA Syntax

See [TableAnnotation::GridLineWeightCustom](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GridLineWeightCustom.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GridLineWeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeight.html)
[ITableAnnotation::BorderLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom.html)
[ITableAnnotation::BorderLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
