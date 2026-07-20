---
title: "ItemGroups Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "ItemGroups"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~ItemGroups.html"
---

# ItemGroups Property (IBomTableSortData)

Gets and sets the categories into which the BOM table rows are grouped.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemGroups As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim value As System.Object

instance.ItemGroups = value

value = instance.ItemGroups
```

### C#

```csharp
System.object ItemGroups {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ItemGroups {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Array of categories as defined in

[swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

or null (see

Remarks

)

## VBA Syntax

See

[BomTableSortData::ItemGroups](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~ItemGroups.html)

.

## Examples

See the

[IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)

examples.

## Remarks

You can set this property in one of two ways:

- Specify null to indicate that the BOM table rows are not to be grouped into categories.
- Specify an array of

  [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  enumerators to indicate that the BOM table rows are to be grouped into categories (assemblies, parts, user defined).

For example, when you set this property to an array of three enumerators in the following order, assemblies are grouped first, parts are grouped next, and user-defined categories are grouped last:

1. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Assemblies
2. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Parts
3. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Other

To eliminate grouping into a category, do not include it in the array.

For example, when you set this property to the following array, no assemblies are grouped, parts are grouped first, and user-defined categories are grouped last:

1. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Parts
2. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Other

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)

[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
