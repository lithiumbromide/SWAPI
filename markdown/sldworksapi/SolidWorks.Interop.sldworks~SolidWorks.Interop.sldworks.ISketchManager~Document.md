---
title: "Document Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "Document"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Document.html"
---

# Document Property (ISketchManager)

Gets the document for this [ISketchManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
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

See [SketchManager::Document](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~Document.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
