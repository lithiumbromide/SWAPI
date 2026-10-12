---
title: "CreateFeatureMgrView2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateFeatureMgrView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateFeatureMgrView2.html"
---

# CreateFeatureMgrView2 Method (IModelDoc2)

Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView2( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim value As System.Object

value = instance.CreateFeatureMgrView2(Bitmap, ToolTip)
```

### C#

```csharp
System.object CreateFeatureMgrView2(
   ref System.int Bitmap,
   System.string ToolTip
)
```

### C++/CLI

```cpp
System.Object^ CreateFeatureMgrView2(
   System.int% Bitmap,
   System.String^ ToolTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`:
- `ToolTip`:

## VBA Syntax

See [ModelDoc2::CreateFeatureMgrView2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateFeatureMgrView2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
