---
title: "RouteType Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "RouteType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~RouteType.html"
---

# RouteType Property (IConnectionPointFeatureData)

Gets and sets the route type of this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RouteType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Integer

instance.RouteType = value

value = instance.RouteType
```

### C#

```csharp
System.int RouteType {get; set;}
```

### C++/CLI

```cpp
property System.int RouteType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Route type as defined in [swModelRouteType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModelRouteType_e.html)

## VBA Syntax

See [ConnectionPointFeatureData::RouteType](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~RouteType.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
