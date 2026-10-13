---
title: "ShowANSIInchLetterNumberDrillSizes Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "ShowANSIInchLetterNumberDrillSizes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes.html"
---

# ShowANSIInchLetterNumberDrillSizes Property (IHoleTable)

Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowANSIInchLetterNumberDrillSizes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.ShowANSIInchLetterNumberDrillSizes = value

value = instance.ShowANSIInchLetterNumberDrillSizes
```

### C#

```csharp
System.bool ShowANSIInchLetterNumberDrillSizes {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowANSIInchLetterNumberDrillSizes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display hole sizes using ANSI inch letters and drill numbers, false to not

## VBA Syntax

See [HoleTable::ShowANSIInchLetterNumberDrillSizes](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~ShowANSIInchLetterNumberDrillSizes.html).

## Examples

[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)
[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)

## Remarks

This property:

- corresponds to the **Show ANSI inch letter and number drill sizes** option in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.
- is valid only for holes created with the Hole Wizard tool.
- specifies whether to display hole sizes as ANSI inch letters or drill numbers, for example, A or #40.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::CombineSameSize Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize.html)
[IHoleTable::CombineTags Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
