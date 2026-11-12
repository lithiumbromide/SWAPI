---
title: "IGetCurveParams Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "IGetCurveParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html"
---

# IGetCurveParams Method (ICoEdge)

Gets the curve parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurveParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Double

value = instance.IGetCurveParams()
```

### C#

```csharp
System.double IGetCurveParams()
```

### C++/CLI

```cpp
System.double IGetCurveParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Edge Data By Name (C++)](Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm)

## Remarks

The return value format is an array of 10 doubles:

- retval[0] X startpoint
- retval[1] Y startpoint
- retval[2] Z startpoint
- retval[3] X endpoint
- retval[4] Y endpoint
- retval[5] Z endpoint
- retval[6] startParam
- retval[7] endParam
- retval[8] sense (Not used)
- retval[9] curve type (Not used)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams.html)
