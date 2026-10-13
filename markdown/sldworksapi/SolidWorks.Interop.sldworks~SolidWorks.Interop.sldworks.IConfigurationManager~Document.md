---
title: "Document Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "Document"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~Document.html"
---

# Document Property (IConfigurationManager)

Gets the related model document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
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

Document to get

## VBA Syntax

See [ConfigurationManager::Document](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~Document.html).

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
