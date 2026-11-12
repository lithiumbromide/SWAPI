---
title: "IsTempAxis Method (IRefAxis)"
project: "SOLIDWORKS API Help"
interface: "IRefAxis"
member: "IsTempAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IsTempAxis.html"
---

# IsTempAxis Method (IRefAxis)

Gets whether the reference axis is a temporary axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTempAxis() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxis
Dim value As System.Boolean

value = instance.IsTempAxis()
```

### C#

```csharp
System.bool IsTempAxis()
```

### C++/CLI

```cpp
System.bool IsTempAxis();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the reference axis is a temporary axis, false if not

## VBA Syntax

See [RefAxis::IsTempAxis](ms-its:sldworksapivb6.chm::/sldworks~RefAxis~IsTempAxis.html).

## Examples

[Get Temporary Axis and Its Reference Face (C#)](Get_Temporary_Axis_and_Its_Reference_Face_Example_CSharp.htm)
[Get Temporary Axis and Its Reference Face (VB.NET)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VBNET.htm)
[Get Temporary Axis and Its Reference Face (VBA)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VB.htm)

## See Also

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.html)
[IRefAxis::GetTempAxisReferenceFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetTempAxisReferenceFace.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
