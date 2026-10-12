---
title: "IMultiSelectByRay Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IMultiSelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IMultiSelectByRay.html"
---

# IMultiSelectByRay Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IMultiSelectByRay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IMultiSelectByRay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IMultiSelectByRay( _
   ByRef PointIn As System.Double, _
   ByRef VectorIn As System.Double, _
   ByVal RadiusIn As System.Double, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PointIn As System.Double
Dim VectorIn As System.Double
Dim RadiusIn As System.Double
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim value As System.Boolean

value = instance.IMultiSelectByRay(PointIn, VectorIn, RadiusIn, TypeWanted, Append)
```

### C#

```csharp
System.bool IMultiSelectByRay(
   ref System.double PointIn,
   ref System.double VectorIn,
   System.double RadiusIn,
   System.int TypeWanted,
   System.bool Append
)
```

### C++/CLI

```cpp
System.bool IMultiSelectByRay(
   System.double% PointIn,
   System.double% VectorIn,
   System.double RadiusIn,
   System.int TypeWanted,
   System.bool Append
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointIn`:
- `VectorIn`:
- `RadiusIn`:
- `TypeWanted`:
- `Append`:

## VBA Syntax

See [ModelDoc::IMultiSelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IMultiSelectByRay.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
