---
title: "IParameter Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IParameter.html"
---

# IParameter Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IParameter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IParameter( _
   ByVal StringIn As System.String _
) As Dimension
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim StringIn As System.String
Dim value As Dimension

value = instance.IParameter(StringIn)
```

### C#

```csharp
Dimension IParameter(
   System.string StringIn
)
```

### C++/CLI

```cpp
Dimension^ IParameter(
   System.String^ StringIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringIn`:

## VBA Syntax

See [ModelDoc::IParameter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IParameter.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
