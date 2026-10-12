---
title: "AngularTolerance Property (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "AngularTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~AngularTolerance.html"
---

# AngularTolerance Property (IHealEdgesFeatureData)

Gets or sets the maximum angle between the edges to merge.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngularTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim value As System.Double

instance.AngularTolerance = value

value = instance.AngularTolerance
```

### C#

```csharp
System.double AngularTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double AngularTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum angle between the edges to merge

## VBA Syntax

See [HealEdgesFeatureData::AngularTolerance](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~AngularTolerance.html).

## Examples

[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
