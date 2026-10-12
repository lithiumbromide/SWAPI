---
title: "StartingValue Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "StartingValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~StartingValue.html"
---

# StartingValue Property (IHoleTable)

Gets or sets the starting value for the datum tags of this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
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

A letter from A to Z, if the template of this hole table uses letter tags; a positive integer, if it uses number tags (see **Remarks**)

## VBA Syntax

See [HoleTable::StartingValue](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~StartingValue.html).

## Remarks

See [IView::InsertHoleTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertHoleTable2.html) for more information about hole table templates.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html)

## Availability

SOLIDWORKS 2011 SP02, Revision Number 19.2
