---
title: "BorderLineWeight Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "BorderLineWeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeight.html"
---

# BorderLineWeight Property (ITableAnnotation)

Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property BorderLineWeight As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

instance.BorderLineWeight = value

value = instance.BorderLineWeight
```

### C#

```csharp
System.int BorderLineWeight {get; set;}
```

### C++/CLI

```cpp
property System.int BorderLineWeight {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weight of border lines for this table as defined by [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [TableAnnotation::BorderLineWeight](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~BorderLineWeight.html).

## Examples

[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::ITableAnnotation::GridLineWeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeight.html)
[ITableAnnotation::BorderLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom.html)
[ITableAnnotation::GridLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeightCustom.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
