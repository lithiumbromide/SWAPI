---
title: "Type Property (ITableAnchor)"
project: "SOLIDWORKS API Help"
interface: "ITableAnchor"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor~Type.html"
---

# Type Property (ITableAnchor)

Gets the type of table anchor.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnchor
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of table anchor as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

## VBA Syntax

See [TableAnchor::Type](ms-its:sldworksapivb6.chm::/sldworks~TableAnchor~Type.html).

## Examples

[Get Table Anchor (VBA)](Get_Table_Anchor_Example_VB.htm)
[Get Table Anchor (VB.NET)](Get_Table_Anchor_Example_VBNET.htm)
[Get Table Anchor (C#)](Get_Table_Anchor_Example_CSharp.htm)

## See Also

[ITableAnchor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html)
[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
