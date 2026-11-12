---
title: "InsertCurveFileEnd Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCurveFileEnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.html"
---

# InsertCurveFileEnd Method (IModelDoc2)

Creates a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCurveFileEnd() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.InsertCurveFileEnd()
```

### C#

```csharp
System.bool InsertCurveFileEnd()
```

### C++/CLI

```cpp
System.bool InsertCurveFileEnd();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if curve is created successfully, false if not

## VBA Syntax

See [ModelDoc2::InsertCurveFileEnd](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCurveFileEnd.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## Remarks

This method:

- is the last method called to create a curve.
- and [IModelDoc2::InsertCurveFileBegin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.html) must enclose all of the calls to [IModelDoc2::InsertCurveFilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html).

See the examples.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
