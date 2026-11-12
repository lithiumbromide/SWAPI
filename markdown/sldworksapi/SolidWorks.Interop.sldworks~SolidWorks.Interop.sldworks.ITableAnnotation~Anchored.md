---
title: "Anchored Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Anchored"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Anchored.html"
---

# Anchored Property (ITableAnnotation)

Gets or sets whether this table is attached to its anchor.

## Syntax

### Visual Basic (Declaration)

```vb
Property Anchored As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Boolean

instance.Anchored = value

value = instance.Anchored
```

### C#

```csharp
System.bool Anchored {get; set;}
```

### C++/CLI

```cpp
property System.bool Anchored {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the table is attached to the anchor, false if not

## VBA Syntax

See [TableAnnotation::Anchored](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Anchored.html).

## Examples

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

## Remarks

If setting this property to TRUE, then the table origin is snapped to the anchor point, according to the anchor type of this table. Use:

- [ITableAnnotation::AnchorType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~AnchorType.html) to determine where the origin is on the table.
- [IAnnotation::GetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetPosition.html) to determine the position of the table.

If the drawing sheet format does not contain an anchor point for this type of table, then attempting to attach the table to the anchor point has no effect.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.html)
[ITableAnnotation::AnchorType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~AnchorType.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
