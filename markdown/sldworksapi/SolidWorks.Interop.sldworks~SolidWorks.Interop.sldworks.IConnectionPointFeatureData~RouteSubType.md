---
title: "RouteSubType Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "RouteSubType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~RouteSubType.html"
---

# RouteSubType Property (IConnectionPointFeatureData)

Gets and sets the route sub-type of this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RouteSubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Integer

instance.RouteSubType = value

value = instance.RouteSubType
```

### C#

```csharp
System.int RouteSubType {get; set;}
```

### C++/CLI

```cpp
property System.int RouteSubType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Electrical route sub-type as defined in [swElectricalSubType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swElectricalSubType_e.html)

## VBA Syntax

See [ConnectionPointFeatureData::RouteSubType](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~RouteSubType.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
