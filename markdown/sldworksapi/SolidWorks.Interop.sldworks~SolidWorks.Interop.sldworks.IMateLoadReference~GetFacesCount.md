---
title: "GetFacesCount Method (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFacesCount.html"
---

# GetFacesCount Method (IMateLoadReference)

Gets the number of supplemental faces of the mate associated with the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesCount( _
   ByVal WhichOne As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As System.Integer

value = instance.GetFacesCount(WhichOne)
```

### C#

```csharp
System.int GetFacesCount(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.int GetFacesCount(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: - 0 = Component1
  - 1 = Component2

### Return Value

Number of supplemental faces of the mate associated with the specified component

## VBA Syntax

See [MateLoadReference::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~GetFacesCount.html).

## Examples

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

## Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

Call this method before calling [IMateLoadReference::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference~IGetFaces.html) to determine the size of the array.

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)
[IMateLoadReference::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
