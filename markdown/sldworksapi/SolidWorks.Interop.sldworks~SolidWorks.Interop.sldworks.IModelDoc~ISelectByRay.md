---
title: "ISelectByRay Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ISelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISelectByRay.html"
---

# ISelectByRay Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ISelectByRay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ISelectByRay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISelectByRay( _
   ByRef PointIn As System.Double, _
   ByRef VectorIn As System.Double, _
   ByVal RadiusIn As System.Double, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PointIn As System.Double
Dim VectorIn As System.Double
Dim RadiusIn As System.Double
Dim TypeWanted As System.Integer
Dim value As System.Boolean

value = instance.ISelectByRay(PointIn, VectorIn, RadiusIn, TypeWanted)
```

### C#

```csharp
System.bool ISelectByRay(
   ref System.double PointIn,
   ref System.double VectorIn,
   System.double RadiusIn,
   System.int TypeWanted
)
```

### C++/CLI

```cpp
System.bool ISelectByRay(
   System.double% PointIn,
   System.double% VectorIn,
   System.double RadiusIn,
   System.int TypeWanted
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointIn`:
- `VectorIn`:
- `RadiusIn`:
- `TypeWanted`:

## VBA Syntax

See [ModelDoc::ISelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ISelectByRay.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
