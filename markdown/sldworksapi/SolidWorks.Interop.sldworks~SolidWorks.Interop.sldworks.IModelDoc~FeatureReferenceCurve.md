---
title: "FeatureReferenceCurve Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureReferenceCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureReferenceCurve.html"
---

# FeatureReferenceCurve Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureReferenceCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.html).

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
Dim instance As IModelDoc
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

- `NumOfCurves`:
- `BaseCurves`:
- `Merge`:
- `FromFileName`:
- `ErrorCode`:

## VBA Syntax

See [ModelDoc::FeatureReferenceCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureReferenceCurve.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
