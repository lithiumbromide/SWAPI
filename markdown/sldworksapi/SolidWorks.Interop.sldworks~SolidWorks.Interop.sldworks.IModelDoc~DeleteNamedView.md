---
title: "DeleteNamedView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "DeleteNamedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DeleteNamedView.html"
---

# DeleteNamedView Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::DeleteNamedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeleteNamedView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteNamedView( _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.DeleteNamedView(ViewName)
```

### C#

```csharp
System.bool DeleteNamedView(
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool DeleteNamedView(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`:

## VBA Syntax

See [ModelDoc::DeleteNamedView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~DeleteNamedView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
