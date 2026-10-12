---
title: "StubLength Property (IConnectionPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConnectionPointFeatureData"
member: "StubLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData~StubLength.html"
---

# StubLength Property (IConnectionPointFeatureData)

Gets and sets the stub length that extends from the connector or fitting when inserted into routes.

## Syntax

### Visual Basic (Declaration)

```vb
Property StubLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConnectionPointFeatureData
Dim value As System.Double

instance.StubLength = value

value = instance.StubLength
```

### C#

```csharp
System.double StubLength {get; set;}
```

### C++/CLI

```cpp
property System.double StubLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of stub that extends from this connection point

## VBA Syntax

See [ConnectionPointFeatureData::StubLength](ms-its:sldworksapivb6.chm::/sldworks~ConnectionPointFeatureData~StubLength.html).

## Examples

[Get and Set Connection Point Feature Data (VBA)](Get_and_Set_Connection_Point_Feature_Data_Example_VB.htm)
[Get and Set Connection Point Feature Data (VB.NET)](Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm)
[Get and Set Connection Point Feature Data (C#)](Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm)

## See Also

[IConnectionPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData.html)
[IConnectionPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
