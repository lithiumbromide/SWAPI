---
title: "MaterialUserName Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "MaterialUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~MaterialUserName.html"
---

# MaterialUserName Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::MaterialUserName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~MaterialUserName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.String

instance.MaterialUserName = value

value = instance.MaterialUserName
```

### C#

```csharp
System.string MaterialUserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialUserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::MaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~MaterialUserName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
