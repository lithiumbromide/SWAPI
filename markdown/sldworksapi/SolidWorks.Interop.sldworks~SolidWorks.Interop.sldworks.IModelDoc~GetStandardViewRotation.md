---
title: "GetStandardViewRotation Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetStandardViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetStandardViewRotation.html"
---

# GetStandardViewRotation Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetStandardViewRotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetStandardViewRotation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStandardViewRotation( _
   ByVal ViewId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ViewId As System.Integer
Dim value As System.Object

value = instance.GetStandardViewRotation(ViewId)
```

### C#

```csharp
System.object GetStandardViewRotation(
   System.int ViewId
)
```

### C++/CLI

```cpp
System.Object^ GetStandardViewRotation(
   System.int ViewId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewId`:

## VBA Syntax

See [ModelDoc::GetStandardViewRotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetStandardViewRotation.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
