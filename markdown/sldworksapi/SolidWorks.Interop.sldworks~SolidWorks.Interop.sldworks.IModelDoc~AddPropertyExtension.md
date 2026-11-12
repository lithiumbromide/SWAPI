---
title: "AddPropertyExtension Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddPropertyExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddPropertyExtension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`:

## VBA Syntax

See [ModelDoc::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddPropertyExtension.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
