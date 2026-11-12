---
title: "CreateFeatureMgrView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateFeatureMgrView.html"
---

# CreateFeatureMgrView Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateFeatureManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateFeatureMgrView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim value As System.Object

value = instance.CreateFeatureMgrView(Bitmap)
```

### C#

```csharp
System.object CreateFeatureMgrView(
   ref System.int Bitmap
)
```

### C++/CLI

```cpp
System.Object^ CreateFeatureMgrView(
   System.int% Bitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`:

## VBA Syntax

See [ModelDoc::CreateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateFeatureMgrView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
