---
title: "GetSupplementalFaces Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetSupplementalFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetSupplementalFaces.html"
---

# GetSupplementalFaces Method (IMate2)

Gets the faces in this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSupplementalFaces( _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.GetSupplementalFaces(WhichOne)
```

### C#

```csharp
System.object GetSupplementalFaces(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ GetSupplementalFaces(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Number of components in this mate

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in this mate

## VBA Syntax

See [Mate2::GetSupplementalFaces](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetSupplementalFaces.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::IGetSupplementalFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IGetSupplementalFaces.html)
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.html)
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
