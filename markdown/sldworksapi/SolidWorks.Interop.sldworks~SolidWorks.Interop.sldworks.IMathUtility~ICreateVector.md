---
title: "ICreateVector Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "ICreateVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateVector.html"
---

# ICreateVector Method (IMathUtility)

Creates a math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateVector( _
   ByRef ArrayDataIn As System.Double _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim ArrayDataIn As System.Double
Dim value As MathVector

value = instance.ICreateVector(ArrayDataIn)
```

### C#

```csharp
MathVector ICreateVector(
   ref System.double ArrayDataIn
)
```

### C++/CLI

```cpp
MathVector^ ICreateVector(
   System.double% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of doubles representing the x,y,z components of the vector

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::CreateVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
