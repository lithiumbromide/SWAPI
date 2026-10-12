---
title: "GetSketchSegments Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "GetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetSketchSegments.html"
---

# GetSketchSegments Method (IStructuralMemberFeatureData)

Gets the sketch segments that define the path of the specified structural member body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments( _
   ByVal PBodyIn As Body2 _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim PBodyIn As Body2
Dim value As System.Object

value = instance.GetSketchSegments(PBodyIn)
```

### C#

```csharp
System.object GetSketchSegments(
   Body2 PBodyIn
)
```

### C++/CLI

```cpp
System.Object^ GetSketchSegments(
   Body2^ PBodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PBodyIn`: [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) whose path sketch segments to get

### Return Value

Array of [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)s

## VBA Syntax

See [StructuralMemberFeatureData::GetSketchSegments](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~GetSketchSegments.html).

## Examples

[Get Structural Member Body Sketch Segments (VBA)](Get_Structural_Member_Body_Sketch_Segments_Example_VB.htm)
[Get Structural Member Body Sketch Segments (VB.NET)](Get_Structural_Member_Body_Sketch_Segments_Example_VBNET.htm)
[Get Structural Member Body Sketch Segments (C#)](Get_Structural_Member_Body_Sketch_Segments_Example_CSharp.htm)

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
