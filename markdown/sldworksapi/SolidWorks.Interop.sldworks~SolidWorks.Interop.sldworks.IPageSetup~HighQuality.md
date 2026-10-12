---
title: "HighQuality Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "HighQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HighQuality.html"
---

# HighQuality Property (IPageSetup)

Gets or sets whether to print a drawing in high quality.

## Syntax

### Visual Basic (Declaration)

```vb
Property HighQuality As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Boolean

instance.HighQuality = value

value = instance.HighQuality
```

### C#

```csharp
System.bool HighQuality {get; set;}
```

### C++/CLI

```cpp
property System.bool HighQuality {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to print a drawing in high quality, false to not

## VBA Syntax

See [PageSetup::HighQuality](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~HighQuality.html).

## Examples

[Get Whether Draft Edges Scaled in Printed Drawing (C#)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VB.NET)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VBA)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm)

## Remarks

You can [scale draft edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~ScaleDraftEdges.html) in a printed drawing when this property is set to true.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
