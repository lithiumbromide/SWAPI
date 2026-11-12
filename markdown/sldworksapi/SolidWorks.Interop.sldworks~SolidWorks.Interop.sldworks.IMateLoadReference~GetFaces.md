---
title: "GetFaces Method (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces.html"
---

# GetFaces Method (IMateLoadReference)

Gets the supplemental faces of the mate associated with the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaces( _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.GetFaces(WhichOne)
```

### C#

```csharp
System.object GetFaces(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ GetFaces(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: - 0 = Component1

  1 = Component2

### Return Value

Array of supplemental [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [MateLoadReference::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~GetFaces.html).

## Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)
[IMateLoadReference::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFacesCount.html)
[IMateLoadReference::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~IGetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
