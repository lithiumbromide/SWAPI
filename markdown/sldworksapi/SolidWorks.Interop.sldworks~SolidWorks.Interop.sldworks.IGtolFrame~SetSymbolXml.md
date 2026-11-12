---
title: "SetSymbolXml Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "SetSymbolXml"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml.html"
---

# SetSymbolXml Method (IGtolFrame)

Sets the XML string for this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSymbolXml( _
   ByVal Xmlstring As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim Xmlstring As System.String
Dim value As System.Boolean

value = instance.SetSymbolXml(Xmlstring)
```

### C#

```csharp
System.bool SetSymbolXml(
   System.string Xmlstring
)
```

### C++/CLI

```cpp
System.bool SetSymbolXml(
   System.String^ Xmlstring
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xmlstring`: XML string

### Return Value

True if XML string successfully set, false if not

## VBA Syntax

See [GtolFrame::SetSymbolXml](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~SetSymbolXml.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

This method is valid only for Gtols created in or converted to the SOLIDWORKS 2022 format.

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

## See Also

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.html)
[ISldWorks::GetGtolFrameXMLSchema Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.html)
[IGtolFrame::GetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
