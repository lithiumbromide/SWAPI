---
title: "swBomTableSortItemGroup_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBomTableSortItemGroup_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomTableSortItemGroup_e.html"
---

# swBomTableSortItemGroup_e Enumeration

Categories for sorting bill of material table rows.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBomTableSortItemGroup_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBomTableSortItemGroup_e
```

### C#

```csharp
public enum swBomTableSortItemGroup_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBomTableSortItemGroup_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBomTableSortItemGroup_Assemblies | 1 = Group table rows containing assemblies |
| swBomTableSortItemGroup_None | DO NOT USE |
| swBomTableSortItemGroup_Other | 3 = Group table rows containing user-defined items |
| swBomTableSortItemGroup_Parts | 2 = Group table rows containing parts |

## Remarks

These enumerator options are used by[IBomTableSortData::ItemGroups](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableSortData~ItemGroups.html)to set the groupings for table sorting.

For example, when you set IBomTableSortData::ItemGroups to the following array, assemblies are grouped first, parts are grouped second, and other categories are grouped last:

1. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Assemblies
2. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Parts
3. [swBomTableSortItemGroup_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html)

  .swBomTableSortItemGroup_Other

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
