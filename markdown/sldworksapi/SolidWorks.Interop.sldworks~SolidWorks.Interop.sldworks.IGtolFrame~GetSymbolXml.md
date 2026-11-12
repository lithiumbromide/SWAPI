---
title: "GetSymbolXml Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "GetSymbolXml"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml.html"
---

# GetSymbolXml Method (IGtolFrame)

Gets the XML string for this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymbolXml() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim value As System.String

value = instance.GetSymbolXml()
```

### C#

```csharp
System.string GetSymbolXml()
```

### C++/CLI

```cpp
System.String^ GetSymbolXml();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

XML string for this Gtol frame

## VBA Syntax

See [GtolFrame::GetSymbolXml](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~GetSymbolXml.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

This method is valid only for Gtols created in or converted to the SOLIDWORKS 2022 format.

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

## See Also

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.html)
[ISldWorks::GetGtolFrameXMLSchema Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.html)
[IGtolFrame::SetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
