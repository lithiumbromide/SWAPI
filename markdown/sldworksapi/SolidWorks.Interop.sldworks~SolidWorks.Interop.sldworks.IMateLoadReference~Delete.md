---
title: "Delete Method (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "Delete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Delete.html"
---

# Delete Method (IMateLoadReference)

Deletes this mate load reference.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim value As System.Boolean

value = instance.Delete()
```

### C#

```csharp
System.bool Delete()
```

### C++/CLI

```cpp
System.bool Delete();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the mate load reference is deleted, false if not

## VBA Syntax

See [MateLoadReference::Delete](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~Delete.html).

## Remarks

This method rebuilds the FeatureManager design tree, which can be a time-consuming operation if it is large. If using this method to delete many load references at once, use [IFeatureManager::EnableFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EnableFeatureTree.html) before and after using IAssemblyDoc::InsertLoadReference to disable and then re-enable rebuilding the FeatureManager design tree.

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
