---
title: "Identifier Property (IDimXpertDatum)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDatum"
member: "Identifier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDatum~Identifier.html"
---

# Identifier Property (IDimXpertDatum)

Gets the label for this DimXpert datum.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Identifier As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDatum
Dim value As System.String

value = instance.Identifier
```

### C#

```csharp
System.string Identifier {get;}
```

### C++/CLI

```cpp
property System.String^ Identifier {
   System.String^ get();
}
```

### Property Value

A label for the datum

## VBA Syntax

See [DimXpertDatum::Identifier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDatum~Identifier.html).

## Examples

[Get and Set Datum Example (C#)](Get_and_Set_Datum_Example_CSharp.htm)
[Get and Set Datum Example (VB.NET)](Get_and_Set_Datum_Example_VBNET.htm)
[Get and Set Datum Example (VBA)](Get_and_Set_Datum_Example_VB.htm)
[Get DimXpert Datum Example (VBA)](Get_DimXpert_Datum_Example_VB.htm)
[Get DimXpert Datum Example (VB.NET)](Get_DimXpert_Datum_Example_VBNET.htm)

## See Also

[IDimXpertDatum Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDatum.html)
[IDimXpertDatum Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDatum_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
