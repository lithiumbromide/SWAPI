---
title: "Document Property (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "Document"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~Document.html"
---

# Document Property (IModelViewManager)

Gets the document to which this model view belongs.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As ModelDoc2

value = instance.Document
```

### C#

```csharp
ModelDoc2 Document {get;}
```

### C++/CLI

```cpp
property ModelDoc2^ Document {
   ModelDoc2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [ModelViewManager::Document](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~Document.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
