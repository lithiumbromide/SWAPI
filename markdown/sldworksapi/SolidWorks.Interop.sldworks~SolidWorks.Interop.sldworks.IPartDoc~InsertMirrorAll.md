---
title: "InsertMirrorAll Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertMirrorAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertMirrorAll.html"
---

# InsertMirrorAll Method (IPartDoc)

Mirrors the part about a selected planar face.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMirrorAll() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Boolean

value = instance.InsertMirrorAll()
```

### C#

```csharp
System.bool InsertMirrorAll()
```

### C++/CLI

```cpp
System.bool InsertMirrorAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature is successfully created, false if not

## VBA Syntax

See [PartDoc::InsertMirrorAll](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertMirrorAll.html).

## Remarks

This method returns a True or false to indicate whether or not the mirror-all feature was created. If it is successful, the newly created feature remains selected after the method runs. You can use [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to retrieve this object.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::MirrorPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorPart.html)
[IFeatureManager::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html)
[IPartDoc::MirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
