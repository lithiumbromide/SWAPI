---
title: "CurveType Property (ICurveParamData)"
project: "SOLIDWORKS API Help"
interface: "ICurveParamData"
member: "CurveType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~CurveType.html"
---

# CurveType Property (ICurveParamData)

Gets the type of curve.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurveType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveParamData
Dim value As System.Integer

value = instance.CurveType
```

### C#

```csharp
System.int CurveType {get;}
```

### C++/CLI

```cpp
property System.int CurveType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of curve as defined in [swCurveTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCurveTypes_e.html)

## VBA Syntax

See [CurveParamData::CurveType](ms-its:sldworksapivb6.chm::/sldworks~CurveParamData~CurveType.html).

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## See Also

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.html)
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
