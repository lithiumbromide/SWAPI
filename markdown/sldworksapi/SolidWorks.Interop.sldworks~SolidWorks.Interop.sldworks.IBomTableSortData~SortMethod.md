---
title: "SortMethod Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "SortMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SortMethod.html"
---

# SortMethod Property (IBomTableSortData)

Gets and sets the method for sorting the BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property SortMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim value As System.Integer

instance.SortMethod = value

value = instance.SortMethod
```

### C#

```csharp
System.int SortMethod {get; set;}
```

### C++/CLI

```cpp
property System.int SortMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sort method as defined by [swBomTableSortMethod_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomTableSortMethod_e.html)

## VBA Syntax

See [BomTableSortData::SortMethod](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~SortMethod.html).

## Examples

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) examples.

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
