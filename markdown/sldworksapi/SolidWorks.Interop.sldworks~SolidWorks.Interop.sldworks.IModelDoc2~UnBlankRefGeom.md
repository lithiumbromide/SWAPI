---
title: "UnBlankRefGeom Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "UnBlankRefGeom"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnBlankRefGeom.html"
---

# UnBlankRefGeom Method (IModelDoc2)

Shows the selected, hidden reference geometry in the graphics window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UnBlankRefGeom()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.UnBlankRefGeom()
```

### C#

```csharp
void UnBlankRefGeom()
```

### C++/CLI

```cpp
void UnBlankRefGeom();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::UnBlankRefGeom](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~UnBlankRefGeom.html).

## Remarks

If you select a reference plane and call this method, then the plane will be visible in the graphics area. This method has the same effect as selecting an item and choosing Show on the shortcut menu.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::BlankRefGeom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BlankRefGeom.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
