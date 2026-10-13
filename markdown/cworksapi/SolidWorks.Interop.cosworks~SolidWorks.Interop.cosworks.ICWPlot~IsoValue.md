---
title: "IsoValue Property (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "IsoValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~IsoValue.html"
---

# IsoValue Property (ICWPlot)

Gets or sets the load level of this Design Insight plot.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsoValue As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim value As System.Integer

instance.IsoValue = value

value = instance.IsoValue
```

### C#

```csharp
System.int IsoValue {get; set;}
```

### C++/CLI

```cpp
property System.int IsoValue {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 <= load level <= 100

## VBA Syntax

See [CWPlot::IsoValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~IsoValue.html).

## Examples

[Create a Design Insight Plot for a Static Study (VBA)](Create_Design_Insight_Plot_for_Static_Study_Example_VB.htm)
[Create a Design Insight Plot for a Static Study (VB.NET)](Create_Design_Insight_Plot_for_Static_Study_Example_VBNET.htm)
[Create a Design Insight Plot for a Static Study (C#)](Create_Design_Insight_Plot_for_Static_Study_Example_CSharp.htm)

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
