---
title: "InsertMirrorFeature Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertMirrorFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertMirrorFeature.html"
---

# InsertMirrorFeature Method (IPartDoc)

Obsolete. Superseded by [IFeatureManager::InsertMirrorFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMirrorFeature( _
   ByVal GeometryPattern As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim GeometryPattern As System.Boolean
Dim value As System.Boolean

value = instance.InsertMirrorFeature(GeometryPattern)
```

### C#

```csharp
System.bool InsertMirrorFeature(
   System.bool GeometryPattern
)
```

### C++/CLI

```cpp
System.bool InsertMirrorFeature(
   System.bool GeometryPattern
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GeometryPattern`:

## VBA Syntax

See [PartDoc::InsertMirrorFeature](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertMirrorFeature.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
