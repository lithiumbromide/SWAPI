---
title: "Location Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "Location"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~Location.html"
---

# Location Property (IConnectionPointFeatureData)

Gets the x,y,z coordinates of this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Location As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Object

value = instance.Location
```

### C#

```csharp
System.object Location {get;}
```

### C++/CLI

```cpp
property System.Object^ Location {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Coordinates of this feature

## VBA Syntax

See [ConnectionPointFeatureData::Location](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~Location.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
