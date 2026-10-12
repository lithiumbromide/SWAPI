---
title: "UOrder Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "UOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UOrder.html"
---

# UOrder Property (IBSurfParamData)

Gets the order of the surface in the U direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Integer

value = instance.UOrder
```

### C#

```csharp
System.int UOrder {get;}
```

### C++/CLI

```cpp
property System.int UOrder {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Order in the U direction

## VBA Syntax

See [BSurfParamData::Uorder](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~Uorder.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::UKnots Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UKnots.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
