---
title: "IGetTessNorms Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessNorms.html"
---

# IGetTessNorms Method (IComponent2)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessNorms() As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Single

value = instance.IGetTessNorms()
```

### C#

```csharp
System.float IGetTessNorms()
```

### C++/CLI

```cpp
System.float IGetTessNorms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of floats (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

The format of retval is:

- float x, y, z - first point's unit normal
- float x, y, z - second point's unit normal
- float x, y, z - third point's unit normal

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessNorms.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision number 10.0
