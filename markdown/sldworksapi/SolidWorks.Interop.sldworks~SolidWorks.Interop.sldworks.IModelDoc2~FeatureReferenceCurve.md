---
title: "FeatureReferenceCurve Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureReferenceCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.html"
---

# FeatureReferenceCurve Method (IModelDoc2)

Creates a reference curve feature from an array of curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByVal BaseCurves As System.Object, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NumOfCurves As System.Integer
Dim BaseCurves As System.Object
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.FeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

### C#

```csharp
System.object FeatureReferenceCurve(
   System.int NumOfCurves,
   System.object BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ FeatureReferenceCurve(
   System.int NumOfCurves,
   System.Object^ BaseCurves,
   System.bool Merge,
   System.String^ FromFileName,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfCurves`: Number of curves from which to create the object
- `BaseCurves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `Merge`: True creates a single reference curve feature, false creates a reference curve feature for each curve in the array
- `FromFileName`: Not used
- `ErrorCode`: Error code as defined in [swFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

### Return Value

[Reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html)

## VBA Syntax

See [ModelDoc2::FeatureReferenceCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureReferenceCurve.html).

## Examples

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IFeatureReferenceCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
