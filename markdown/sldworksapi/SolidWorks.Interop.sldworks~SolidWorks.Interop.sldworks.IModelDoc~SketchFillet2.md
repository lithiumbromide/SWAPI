---
title: "SketchFillet2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchFillet2.html"
---

# SketchFillet2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchFillet2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchFillet2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchFillet2( _
   ByVal Rad As System.Double, _
   ByVal ConstrainedCorners As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Rad As System.Double
Dim ConstrainedCorners As System.Short
Dim value As System.Boolean

value = instance.SketchFillet2(Rad, ConstrainedCorners)
```

### C#

```csharp
System.bool SketchFillet2(
   System.double Rad,
   System.short ConstrainedCorners
)
```

### C++/CLI

```cpp
System.bool SketchFillet2(
   System.double Rad,
   System.short ConstrainedCorners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Rad`:
- `ConstrainedCorners`:

## VBA Syntax

See [ModelDoc::SketchFillet2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchFillet2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
