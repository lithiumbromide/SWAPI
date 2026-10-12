---
title: "IGetRefAxisParams Method (IRefAxis)"
project: "SOLIDWORKS API Help"
interface: "IRefAxis"
member: "IGetRefAxisParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IGetRefAxisParams.html"
---

# IGetRefAxisParams Method (IRefAxis)

Gets information for a reference axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRefAxisParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxis
Dim value As System.Double

value = instance.IGetRefAxisParams()
```

### C#

```csharp
System.double IGetRefAxisParams()
```

### C++/CLI

```cpp
System.double IGetRefAxisParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see [Remarks](#Remarks))

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Info on Plane-Axis (C++)](Get_Info_on_Plane_Axis_Example_CPlusPlus_COM.htm)

## Remarks

The return value is the following array of doubles:

[ StartPt[3], EndPt[3] ]

where:

- StartPt[3] = array of three values describing the x,y,z start point of the reference axis.
- EndPt[3] = array of three values describing the x,y,z end point of the reference axis.

## See Also

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.html)
[IRefAxis::GetRefAxisParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetRefAxisParams.html)
