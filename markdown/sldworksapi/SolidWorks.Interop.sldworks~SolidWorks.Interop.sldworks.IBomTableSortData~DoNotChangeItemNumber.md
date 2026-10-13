---
title: "DoNotChangeItemNumber Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "DoNotChangeItemNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~DoNotChangeItemNumber.html"
---

# DoNotChangeItemNumber Property (IBomTableSortData)

Gets and sets whether to change BOM item numbers after sorting.

## Syntax

### Visual Basic (Declaration)

```vb
Property DoNotChangeItemNumber As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim value As System.Boolean

instance.DoNotChangeItemNumber = value

value = instance.DoNotChangeItemNumber
```

### C#

```csharp
System.bool DoNotChangeItemNumber {get; set;}
```

### C++/CLI

```cpp
property System.bool DoNotChangeItemNumber {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to preserve BOM item numbers, false to re-number them

## VBA Syntax

See [BomTableSortData::DoNotChangeItemNumber](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~DoNotChangeItemNumber.html).

## Examples

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) examples.

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
