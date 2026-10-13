---
title: "ShowNamedView2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ShowNamedView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ShowNamedView2.html"
---

# ShowNamedView2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ShowNamedView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowNamedView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowNamedView2( _
   ByVal VName As System.String, _
   ByVal ViewId As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim VName As System.String
Dim ViewId As System.Integer

instance.ShowNamedView2(VName, ViewId)
```

### C#

```csharp
void ShowNamedView2(
   System.string VName,
   System.int ViewId
)
```

### C++/CLI

```cpp
void ShowNamedView2(
   System.String^ VName,
   System.int ViewId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VName`:
- `ViewId`:

## VBA Syntax

See [ModelDoc::ShowNamedView2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ShowNamedView2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
