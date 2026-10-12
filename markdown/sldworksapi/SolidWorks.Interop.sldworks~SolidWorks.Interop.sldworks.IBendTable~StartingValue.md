---
title: "StartingValue Property (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "StartingValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~StartingValue.html"
---

# StartingValue Property (IBendTable)

Gets and sets the starting datum tag for this bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
Dim value As System.String

instance.StartingValue = value

value = instance.StartingValue
```

### C#

```csharp
System.string StartingValue {get; set;}
```

### C++/CLI

```cpp
property System.String^ StartingValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Starting datum tag (see **Remarks**)

## VBA Syntax

See [BendTable::StartingValue](ms-its:sldworksapivb6.chm::/sldworks~BendTable~StartingValue.html).

## Examples

[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)

## Remarks

This property returns:

- Letter from A to Z, if [IBendTable::TagStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTable~TagStyle.html) is set to [swBendTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html).swBendTable_AlphaNumericTags.
- Positive integer, if [IBendTable::TagStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTable~TagStyle.html) is set to [swBendTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html).swBendTable_NumericTags.

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
