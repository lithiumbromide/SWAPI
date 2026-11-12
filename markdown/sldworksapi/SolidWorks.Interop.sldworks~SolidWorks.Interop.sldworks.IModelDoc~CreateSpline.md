---
title: "CreateSpline Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateSpline.html"
---

# CreateSpline Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateSpline.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpline( _
   ByVal PointData As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PointData As System.Object
Dim value As System.Object

value = instance.CreateSpline(PointData)
```

### C#

```csharp
System.object CreateSpline(
   System.object PointData
)
```

### C++/CLI

```cpp
System.Object^ CreateSpline(
   System.Object^ PointData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointData`:

## VBA Syntax

See [ModelDoc::CreateSpline](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateSpline.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
