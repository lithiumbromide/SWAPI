---
title: "SketchMirror Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchMirror"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchMirror.html"
---

# SketchMirror Method (IModelDoc2)

Creates new entities that are mirror images of the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchMirror()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.SketchMirror()
```

### C#

```csharp
void SketchMirror()
```

### C++/CLI

```cpp
void SketchMirror();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SketchMirror](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchMirror.html).

## Remarks

If the entity to mirror is:

- a sketch segment, then use a selection mark of 1
- a centerline, then use a selection mark of 2

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
