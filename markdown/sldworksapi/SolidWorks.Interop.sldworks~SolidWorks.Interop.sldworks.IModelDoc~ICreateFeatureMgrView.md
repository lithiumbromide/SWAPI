---
title: "ICreateFeatureMgrView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateFeatureMgrView.html"
---

# ICreateFeatureMgrView Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateFeatureMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim value As FeatMgrView

value = instance.ICreateFeatureMgrView(Bitmap)
```

### C#

```csharp
FeatMgrView ICreateFeatureMgrView(
   ref System.int Bitmap
)
```

### C++/CLI

```cpp
FeatMgrView^ ICreateFeatureMgrView(
   System.int% Bitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`:

## VBA Syntax

See [ModelDoc::ICreateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateFeatureMgrView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
