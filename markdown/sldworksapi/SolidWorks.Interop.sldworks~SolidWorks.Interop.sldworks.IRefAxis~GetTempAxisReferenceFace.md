---
title: "GetTempAxisReferenceFace Method (IRefAxis)"
project: "SOLIDWORKS API Help"
interface: "IRefAxis"
member: "GetTempAxisReferenceFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetTempAxisReferenceFace.html"
---

# GetTempAxisReferenceFace Method (IRefAxis)

Gets the reference face for this temporary axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTempAxisReferenceFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxis
Dim value As System.Object

value = instance.GetTempAxisReferenceFace()
```

### C#

```csharp
System.object GetTempAxisReferenceFace()
```

### C++/CLI

```cpp
System.Object^ GetTempAxisReferenceFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Reference face for this temporary axis

## VBA Syntax

See [RefAxis::GetTempAxisReferenceFace](ms-its:sldworksapivb6.chm::/sldworks~RefAxis~GetTempAxisReferenceFace.html).

## Examples

[Get Temporary Axis and Its Reference Face (C#)](Get_Temporary_Axis_and_Its_Reference_Face_Example_CSharp.htm)
[Get Temporary Axis and Its Reference Face (VB.NET)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VBNET.htm)
[Get Temporary Axis and Its Reference Face (VBA)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VB.htm)

## See Also

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.html)
[IRefAxis::IsTempAxis Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IsTempAxis.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
