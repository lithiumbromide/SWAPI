---
title: "NumberOfCopies Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "NumberOfCopies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~NumberOfCopies.html"
---

# NumberOfCopies Property (IMoveCopyBodyFeatureData)

Gets or sets the number of copies.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfCopies As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Integer

instance.NumberOfCopies = value

value = instance.NumberOfCopies
```

### C#

```csharp
System.int NumberOfCopies {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfCopies {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of copies

## VBA Syntax

See [MoveCopyBodyFeatureData::NumberOfCopies](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~NumberOfCopies.html).

## Examples

[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

## Remarks

Call this property after calling [IMoveCopyBodyFeatureData::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.html).

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
