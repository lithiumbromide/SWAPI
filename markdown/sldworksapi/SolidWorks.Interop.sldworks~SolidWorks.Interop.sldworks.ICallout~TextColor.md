---
title: "TextColor Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "TextColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor.html"
---

# TextColor Property (ICallout)

Gets or sets the color of the text in the specified row in this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextColor( _
   ByVal RowID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Integer

instance.TextColor(RowID) = value

value = instance.TextColor(RowID)
```

### C#

```csharp
System.int TextColor(
   System.int RowID
) {get; set;}
```

### C++/CLI

```cpp
property System.int TextColor {
   System.int get(System.int RowID);
   void set (System.int RowID, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row in callout

### Property Value

[System color](ms-its:swconst.chm::/SO_Colors.htm)

## VBA Syntax

See [Callout::TextColor](ms-its:sldworksapivb6.chm::/sldworks~Callout~TextColor.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## Remarks

You must use a system color; you cannot use any other RGB values. To see system colors, click Tools > Options > Colors in the SOLIDWORKS Design user interface.

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::OpaqueColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~OpaqueColor.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
