---
title: "SelectedEdgeProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectedEdgeProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectedEdgeProperties.html"
---

# SelectedEdgeProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectedEdgeProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectedEdgeProperties( _
   ByVal EdgeName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim EdgeName As System.String
Dim value As System.Boolean

value = instance.SelectedEdgeProperties(EdgeName)
```

### C#

```csharp
System.bool SelectedEdgeProperties(
   System.string EdgeName
)
```

### C++/CLI

```cpp
System.bool SelectedEdgeProperties(
   System.String^ EdgeName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeName`:

## VBA Syntax

See [ModelDoc::SelectedEdgeProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectedEdgeProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
