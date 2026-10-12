---
title: "Save2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Save2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Save2.html"
---

# Save2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Save2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Save2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Save2( _
   ByVal Silent As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Silent As System.Boolean
Dim value As System.Integer

value = instance.Save2(Silent)
```

### C#

```csharp
System.int Save2(
   System.bool Silent
)
```

### C++/CLI

```cpp
System.int Save2(
   System.bool Silent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Silent`:

## VBA Syntax

See [ModelDoc::Save2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Save2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
