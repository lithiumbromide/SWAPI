---
title: "IsActive Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IsActive"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IsActive.html"
---

# IsActive Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IsActive](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsActive.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsActive( _
   ByVal CompStr As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim CompStr As System.String
Dim value As System.Boolean

value = instance.IsActive(CompStr)
```

### C#

```csharp
System.bool IsActive(
   System.string CompStr
)
```

### C++/CLI

```cpp
System.bool IsActive(
   System.String^ CompStr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompStr`:

## VBA Syntax

See [ModelDoc::IsActive](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IsActive.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
