---
title: "ElectricalPinID Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "ElectricalPinID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~ElectricalPinID.html"
---

# ElectricalPinID Property (IConnectionPointFeatureData)

Gets and sets the electrical pin ID of this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ElectricalPinID As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.String

instance.ElectricalPinID = value

value = instance.ElectricalPinID
```

### C#

```csharp
System.string ElectricalPinID {get; set;}
```

### C++/CLI

```cpp
property System.String^ ElectricalPinID {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Electrical pin ID

## VBA Syntax

See [ConnectionPointFeatureData::ElectricalPinID](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~ElectricalPinID.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
