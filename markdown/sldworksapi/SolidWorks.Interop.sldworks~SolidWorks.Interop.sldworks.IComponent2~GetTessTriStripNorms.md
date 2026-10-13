---
title: "GetTessTriStripNorms Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetTessTriStripNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripNorms.html"
---

# GetTessTriStripNorms Method (IComponent2)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripNorms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetTessTriStripNorms()
```

### C#

```csharp
System.object GetTessTriStripNorms()
```

### C++/CLI

```cpp
System.Object^ GetTessTriStripNorms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the tri-strip normals

## VBA Syntax

See [Component2::GetTessTriStripNorms](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetTessTriStripNorms.html).

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripNorms.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
