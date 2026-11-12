---
title: "Position Property (ITableAnchor)"
project: "SOLIDWORKS API Help"
interface: "ITableAnchor"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor~Position.html"
---

# Position Property (ITableAnchor)

Gets or sets the location of the table anchor.

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnchor
Dim value As System.Object

instance.Position = value

value = instance.Position
```

### C#

```csharp
System.object Position {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Position {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles of x and y coordinates of the table anchor

## VBA Syntax

See [TableAnchor::Position](ms-its:sldworksapivb6.chm::/sldworks~TableAnchor~Position.html).

## Examples

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

## See Also

[ITableAnchor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html)
[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
