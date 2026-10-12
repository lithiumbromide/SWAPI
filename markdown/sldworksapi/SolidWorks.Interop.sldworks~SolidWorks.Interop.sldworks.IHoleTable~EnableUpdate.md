---
title: "EnableUpdate Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "EnableUpdate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate.html"
---

# EnableUpdate Property (IHoleTable)

Gets or sets whether to update hole table and graphics after [changing hole tags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~HoleTag.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableUpdate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.EnableUpdate = value

value = instance.EnableUpdate
```

### C#

```csharp
System.bool EnableUpdate {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True updates the hole table and model view, false does not

## VBA Syntax

See [HoleTable::EnableUpdate](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~EnableUpdate.html).

## Examples

[Change Tags in Hole Table (VB.NET)](Change_Tags_in_Hole_Table_Example_VBNET.htm)
[Change Tags in Hole Table (VBA)](Change_Tags_in_Hole_Table_Example_VB.htm)

## Remarks

If you plan on changing many hole tags, then consider setting this property to false to avoid a possible degradation in performance. After changing all of the hole tags, set this property to true to update the hole table and model view.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.html)
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.html)
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
