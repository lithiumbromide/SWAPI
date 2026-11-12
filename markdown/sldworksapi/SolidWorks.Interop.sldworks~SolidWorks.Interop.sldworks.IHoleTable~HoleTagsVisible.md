---
title: "HoleTagsVisible Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "HoleTagsVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.html"
---

# HoleTagsVisible Property (IHoleTable)

Gets whether the hole tags are visible for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleTagsVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.HoleTagsVisible = value

value = instance.HoleTagsVisible
```

### C#

```csharp
System.bool HoleTagsVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool HoleTagsVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if hole tags are visible, false if not

## VBA Syntax

See [HoleTable::HoleTagsVisible](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~HoleTagsVisible.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::CombineTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.html)
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html)
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.html)
[IHoleTable::EnableUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate.html)

## Availability

SOLIDWORKS 2004 SP1, Revision 12.1
