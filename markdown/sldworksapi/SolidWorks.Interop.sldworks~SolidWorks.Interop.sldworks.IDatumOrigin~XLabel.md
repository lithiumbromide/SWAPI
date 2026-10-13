---
title: "XLabel Property (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "XLabel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~XLabel.html"
---

# XLabel Property (IDatumOrigin)

Gets or sets the label for the X axis for this datum origin.

## Syntax

### Visual Basic (Declaration)

```vb
Property XLabel As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As System.String

instance.XLabel = value

value = instance.XLabel
```

### C#

```csharp
System.string XLabel {get; set;}
```

### C++/CLI

```cpp
property System.String^ XLabel {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Label for the X axis for this datum origin

## VBA Syntax

See [DatumOrigin::XLabel](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~XLabel.html).

## Examples

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)
[IDatumOrigin::YLabel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~YLabel.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
