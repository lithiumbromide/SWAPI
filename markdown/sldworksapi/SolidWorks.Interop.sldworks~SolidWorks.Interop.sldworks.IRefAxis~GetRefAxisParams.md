---
title: "GetRefAxisParams Method (IRefAxis)"
project: "SOLIDWORKS API Help"
interface: "IRefAxis"
member: "GetRefAxisParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetRefAxisParams.html"
---

# GetRefAxisParams Method (IRefAxis)

Gets information for a reference axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRefAxisParams() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxis
Dim value As System.Object

value = instance.GetRefAxisParams()
```

### C#

```csharp
System.object GetRefAxisParams()
```

### C++/CLI

```cpp
System.Object^ GetRefAxisParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see [Remarks](#Remarks))

## VBA Syntax

See [RefAxis::GetRefAxisParams](ms-its:sldworksapivb6.chm::/sldworks~RefAxis~GetRefAxisParams.html).

## Examples

[Get Parameters for Reference Axis (VBA)](Get_Parameters_for_Reference_Axis_Example_VB.htm)

## Remarks

The return value is the following array of doubles:

[ StartPt[3], EndPt[3] ]

where:

- StartPt[3] = array of three values describing the x,y,z start point of the reference axis.
- EndPt[3] = array of three values describing the x,y,z end point of the reference axis.

## See Also

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.html)
[IRefAxis::IGetRefAxisParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IGetRefAxisParams.html)
