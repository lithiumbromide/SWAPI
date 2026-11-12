---
title: "ICreateFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView.html"
---

# ICreateFeatureMgrView Method (IModelDoc2)

Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::ICreateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateFeatureMgrView.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
