---
title: "IFeatureReferenceCurve Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IFeatureReferenceCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IFeatureReferenceCurve.html"
---

# IFeatureReferenceCurve Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IFeatureReferenceCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByVal BaseCurves As System.IntPtr, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As ReferenceCurve
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NumOfCurves As System.Integer
Dim BaseCurves As System.IntPtr
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As ReferenceCurve

value = instance.IFeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

### C#

```csharp
ReferenceCurve IFeatureReferenceCurve(
   System.int NumOfCurves,
   System.IntPtr BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
ReferenceCurve^ IFeatureReferenceCurve(
   System.int NumOfCurves,
   System.IntPtr BaseCurves,
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

See [ModelDoc::IFeatureReferenceCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IFeatureReferenceCurve.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
