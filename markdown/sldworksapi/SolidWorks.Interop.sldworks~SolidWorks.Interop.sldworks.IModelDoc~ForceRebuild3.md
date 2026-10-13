---
title: "ForceRebuild3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ForceRebuild3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ForceRebuild3.html"
---

# ForceRebuild3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ForceRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceRebuild3( _
   ByVal TopOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim TopOnly As System.Boolean
Dim value As System.Boolean

value = instance.ForceRebuild3(TopOnly)
```

### C#

```csharp
System.bool ForceRebuild3(
   System.bool TopOnly
)
```

### C++/CLI

```cpp
System.bool ForceRebuild3(
   System.bool TopOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopOnly`:

## VBA Syntax

See [ModelDoc::ForceRebuild3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ForceRebuild3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
