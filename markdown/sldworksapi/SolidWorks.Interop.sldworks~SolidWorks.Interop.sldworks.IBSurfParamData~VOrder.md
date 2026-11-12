---
title: "VOrder Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "VOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VOrder.html"
---

# VOrder Property (IBSurfParamData)

Gets the order of the surface in the V direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Integer

value = instance.VOrder
```

### C#

```csharp
System.int VOrder {get;}
```

### C++/CLI

```cpp
property System.int VOrder {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Order in the V direction

## VBA Syntax

See [BSurfParamData::VOrder](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~VOrder.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::UOrder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UOrder.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
