---
title: "IGetTessTriStripNorms Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessTriStripNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripNorms.html"
---

# IGetTessTriStripNorms Method (IComponent2)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStripNorms() As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Single

value = instance.IGetTessTriStripNorms()
```

### C#

```csharp
System.float IGetTessTriStripNorms()
```

### C++/CLI

```cpp
System.float IGetTessTriStripNorms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of floats containing the tri-strip normals

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripNorms.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
