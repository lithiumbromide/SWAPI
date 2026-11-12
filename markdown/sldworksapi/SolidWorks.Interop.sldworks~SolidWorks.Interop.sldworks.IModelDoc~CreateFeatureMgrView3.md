---
title: "CreateFeatureMgrView3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateFeatureMgrView3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateFeatureMgrView3.html"
---

# CreateFeatureMgrView3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateFeatureMgrView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As System.Object

value = instance.CreateFeatureMgrView3(Bitmap, ToolTip, WhichPane)
```

### C#

```csharp
System.object CreateFeatureMgrView3(
   ref System.int Bitmap,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.Object^ CreateFeatureMgrView3(
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

See [ModelDoc::CreateFeatureMgrView3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateFeatureMgrView3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
