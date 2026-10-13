---
title: "CreateFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateFeatureMgrView.html"
---

# CreateFeatureMgrView Method (IModelDoc2)

Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::CreateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateFeatureMgrView.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
