---
title: "OpaqueColor Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "OpaqueColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~OpaqueColor.html"
---

# OpaqueColor Property (ICallout)

Gets or sets the opaque (background) color for the labels for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property OpaqueColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Integer

instance.OpaqueColor = value

value = instance.OpaqueColor
```

### C#

```csharp
System.int OpaqueColor {get; set;}
```

### C++/CLI

```cpp
property System.int OpaqueColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[System color](ms-its:swconst.chm::/SO_Colors.htm)

## VBA Syntax

See [Callout::OpaqueColor](ms-its:sldworksapivb6.chm::/sldworks~Callout~OpaqueColor.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## Remarks

You must use a system color; you cannot use any other RGB values. To see system colors, click **Tools >** **Options >** **Colors** in the SOLIDWORKS Design user interface.

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::TextColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
