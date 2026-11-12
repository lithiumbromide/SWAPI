---
title: "InsertCurveFileBegin Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCurveFileBegin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.html"
---

# InsertCurveFileBegin Method (IModelDoc2)

Creates a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCurveFileBegin()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertCurveFileBegin()
```

### C#

```csharp
void InsertCurveFileBegin()
```

### C++/CLI

```cpp
void InsertCurveFileBegin();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertCurveFileBegin](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCurveFileBegin.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## Remarks

This method:

- is the first method called that create a curve. This method must precede all calls to [IModelDoc2::InsertCurveFilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html).
- and [IModelDoc2::InsertCurveFileEnd](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.html) must enclose all of the calls to IModelDoc2::InsertCurveFilePoint.

See the examples.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number
