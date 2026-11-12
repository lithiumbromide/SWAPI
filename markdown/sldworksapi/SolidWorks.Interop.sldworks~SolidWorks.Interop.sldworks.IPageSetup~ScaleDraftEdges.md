---
title: "ScaleDraftEdges Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "ScaleDraftEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleDraftEdges.html"
---

# ScaleDraftEdges Property (IPageSetup)

Gets or sets whether to scale draft edges when printing a drawing in high quality.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleDraftEdges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Boolean

instance.ScaleDraftEdges = value

value = instance.ScaleDraftEdges
```

### C#

```csharp
System.bool ScaleDraftEdges {get; set;}
```

### C++/CLI

```cpp
property System.bool ScaleDraftEdges {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to scale draft edges when printing a drawing in high quality, false to not

## VBA Syntax

See [PageSetup::ScaleDraftEdges](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~ScaleDraftEdges.html).

## Examples

[Get Whether Draft Edges Scaled in Printed Drawing (C#)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VB.NET)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VBA)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm)

## Remarks

This property is only valid when [IPageSetup::HighQuality](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~HighQuality.html) is set to true.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
