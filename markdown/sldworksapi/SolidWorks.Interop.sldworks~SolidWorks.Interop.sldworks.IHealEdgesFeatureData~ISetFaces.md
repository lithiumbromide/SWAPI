---
title: "ISetFaces Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~ISetFaces.html"
---

# ISetFaces Method (IHealEdgesFeatureData)

Gets the faces whose edges were healed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal Count As System.Integer, _
   ByRef EntIn As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim Count As System.Integer
Dim EntIn As Face2

instance.ISetFaces(Count, EntIn)
```

### C#

```csharp
void ISetFaces(
   System.int Count,
   ref Face2 EntIn
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int Count,
   Face2^% EntIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces whose edges were healed
- `EntIn`: - in-process, unmanaged C++: Pointer to [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) whose edges were healed

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)
[IHealEdgesFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~IGetFaces.html)
[IHealEdgesFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
