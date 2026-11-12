---
title: "GetTessNorms Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetTessNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessNorms.html"
---

# GetTessNorms Method (IComponent2)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessNorms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetTessNorms()
```

### C#

```csharp
System.object GetTessNorms()
```

### C++/CLI

```cpp
System.Object^ GetTessNorms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object of type SafeArray of floats (see **Remarks**)

## VBA Syntax

See [Component2::GetTessNorms](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetTessNorms.html).

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
[IComponent2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessNorms.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
