---
title: "PortID Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "PortID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~PortID.html"
---

# PortID Property (IConnectionPointFeatureData)

Gets and sets the port ID for this connection point feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PortID As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.String

instance.PortID = value

value = instance.PortID
```

### C#

```csharp
System.string PortID {get; set;}
```

### C++/CLI

```cpp
property System.String^ PortID {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Port ID of this feature

## VBA Syntax

See [ConnectionPointFeatureData::PortID](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~PortID.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
