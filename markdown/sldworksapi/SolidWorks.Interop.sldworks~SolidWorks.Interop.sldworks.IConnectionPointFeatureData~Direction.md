---
title: "Direction Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~Direction.html"
---

# Direction Property (IConnectionPointFeatureData)

Gets the x, y, z coordinates of the direction vector of this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Object

value = instance.Direction
```

### C#

```csharp
System.object Direction {get;}
```

### C++/CLI

```cpp
property System.Object^ Direction {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles of the coordinates of the direction vector of this connection point

## VBA Syntax

See [ConnectionPointFeatureData::Direction](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~Direction.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
