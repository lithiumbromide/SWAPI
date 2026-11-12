---
title: "MaterialIdName Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "MaterialIdName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~MaterialIdName.html"
---

# MaterialIdName Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::MaterialIdName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~MaterialIdName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialIdName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.String

instance.MaterialIdName = value

value = instance.MaterialIdName
```

### C#

```csharp
System.string MaterialIdName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::MaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~MaterialIdName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
