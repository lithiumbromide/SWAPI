---
title: "Insert3DSketch2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Insert3DSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Insert3DSketch2.html"
---

# Insert3DSketch2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::Insert3DSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~Insert3DSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Insert3DSketch2( _
   ByVal UpdateEditRebuild As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UpdateEditRebuild As System.Boolean

instance.Insert3DSketch2(UpdateEditRebuild)
```

### C#

```csharp
void Insert3DSketch2(
   System.bool UpdateEditRebuild
)
```

### C++/CLI

```cpp
void Insert3DSketch2(
   System.bool UpdateEditRebuild
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpdateEditRebuild`: True if you want to edit and rebuild the document, false if not

## VBA Syntax

See [ModelDoc2::Insert3DSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Insert3DSketch2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISketch::Is3D Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~Is3D.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
