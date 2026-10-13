---
title: "IGetConstraints Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "IGetConstraints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetConstraints.html"
---

# IGetConstraints Method (ISketchPath)

Gets the names of the constraints in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConstraints( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetConstraints(Count)
```

### C#

```csharp
System.string IGetConstraints(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetConstraints(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch constraints

### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch constraints

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchPath::GetConstraintsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~GetConstraintsCount.html) to get the value of count.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraints.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
