---
title: "ICreateFeatureMgrView3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateFeatureMgrView3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateFeatureMgrView3.html"
---

# ICreateFeatureMgrView3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.ICreateFeatureMgrView3(Bitmap, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView ICreateFeatureMgrView3(
   ref System.int Bitmap,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ ICreateFeatureMgrView3(
   System.int% Bitmap,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`:
- `ToolTip`:
- `WhichPane`:

## VBA Syntax

See [ModelDoc::ICreateFeatureMgrView3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateFeatureMgrView3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
