---
title: "EdgeLengthTolerance Property (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "EdgeLengthTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~EdgeLengthTolerance.html"
---

# EdgeLengthTolerance Property (IHealEdgesFeatureData)

Gets or sets the maximum length of the edges to merge.

## Syntax

### Visual Basic (Declaration)

```vb
Property EdgeLengthTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim value As System.Double

instance.EdgeLengthTolerance = value

value = instance.EdgeLengthTolerance
```

### C#

```csharp
System.double EdgeLengthTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double EdgeLengthTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum length of the edges to merge

## VBA Syntax

See [HealEdgesFeatureData::EdgeLengthTolerance](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~EdgeLengthTolerance.html).

## Examples

[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 13.0
