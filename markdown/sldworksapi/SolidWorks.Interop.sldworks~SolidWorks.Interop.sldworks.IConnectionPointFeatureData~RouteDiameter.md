---
title: "RouteDiameter Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "RouteDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~RouteDiameter.html"
---

# RouteDiameter Property (IConnectionPointFeatureData)

Gets and sets the route diameter at this connection point.

## Syntax

### Visual Basic (Declaration)

```vb
Property RouteDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Double

instance.RouteDiameter = value

value = instance.RouteDiameter
```

### C#

```csharp
System.double RouteDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double RouteDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Route diameter at this connection point

## VBA Syntax

See [ConnectionPointFeatureData::RouteDiameter](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~RouteDiameter.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
