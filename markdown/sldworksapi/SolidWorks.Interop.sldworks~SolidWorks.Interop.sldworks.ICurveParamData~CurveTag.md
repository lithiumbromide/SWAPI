---
title: "CurveTag Property (ICurveParamData)"
project: "SOLIDWORKS API Help"
interface: "ICurveParamData"
member: "CurveTag"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~CurveTag.html"
---

# CurveTag Property (ICurveParamData)

Gets the ID for this curve.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurveTag As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveParamData
Dim value As System.Integer

value = instance.CurveTag
```

### C#

```csharp
System.int CurveTag {get;}
```

### C++/CLI

```cpp
property System.int CurveTag {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

ID of the curve

## VBA Syntax

See [CurveParamData::CurveTag](ms-its:sldworksapivb6.chm::/sldworks~CurveParamData~CurveTag.html).

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## See Also

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.html)
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
