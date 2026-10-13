---
title: "DatumOrigin Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "DatumOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~DatumOrigin.html"
---

# DatumOrigin Property (IHoleTable)

Gets the datum origin annotation for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DatumOrigin As DatumOrigin
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As DatumOrigin

value = instance.DatumOrigin
```

### C#

```csharp
DatumOrigin DatumOrigin {get;}
```

### C++/CLI

```cpp
property DatumOrigin^ DatumOrigin {
   DatumOrigin^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IDatumOrigin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin.html) object

## VBA Syntax

See [HoleTable::DatumOrigin](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~DatumOrigin.html).

## Examples

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
