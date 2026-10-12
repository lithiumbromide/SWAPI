---
title: "ChangeSketchPlane Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ChangeSketchPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ChangeSketchPlane.html"
---

# ChangeSketchPlane Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ChangeSketchPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ChangeSketchPlane.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeSketchPlane() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.ChangeSketchPlane()
```

### C#

```csharp
System.bool ChangeSketchPlane()
```

### C++/CLI

```cpp
System.bool ChangeSketchPlane();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the change was successful, false otherwise

## VBA Syntax

See [ModelDoc2::ChangeSketchPlane](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ChangeSketchPlane.html).

## Examples

[Change Plane of Sketch (VBA)](Change_Sketch_of_Plane_Example.htm)

## Remarks

Every sketch is associated with a plane (for example, a reference plane or a planar face). You must preselect the sketch and the new plane or face before using this method.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
