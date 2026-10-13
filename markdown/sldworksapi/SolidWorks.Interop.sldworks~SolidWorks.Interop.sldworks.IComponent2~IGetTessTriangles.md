---
title: "IGetTessTriangles Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriangles.html"
---

# IGetTessTriangles Method (IComponent2)

Gets the triangles that make up the shaded picture tessellation for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriangles(NoConversion)
```

### C#

```csharp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: True prohibits conversion to user units from system units, false does not

### Return Value

- in-process, unmanaged C++: Pointer to array of floats (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

These triangles are intended for graphics display purposes and do not represent a
tessellation that could be used, for example, by a machining application. If you
need the type of accuracy associated with a machining product, we recommend that
you traverse the body faces and extract the topology and geometry data to create
your own faceting.

The format of the returned data is:

- float x, y, z - first point in meters
- float x, y, z - second point in meters
- float x, y, z - third point in meters

for the set of triangles for the component.

The total size of the data is **[** 9 x sizeof(`float)` x `(number of triangles)` **]**.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriangles.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
