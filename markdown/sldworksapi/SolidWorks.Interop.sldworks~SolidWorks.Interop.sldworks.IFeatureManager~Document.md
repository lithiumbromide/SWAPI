---
title: "Document Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "Document"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~Document.html"
---

# Document Property (IFeatureManager)

Gets the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
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

[Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) to get

## VBA Syntax

See [FeatureManager::Document](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~Document.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IModelDocExtension::Document Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Document.html)
[IModelViewManager::Document Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~Document.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
