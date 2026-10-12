---
title: "ICreatePoint Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "ICreatePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreatePoint.html"
---

# ICreatePoint Method (IMathUtility)

Creates a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePoint( _
   ByRef ArrayDataIn As System.Double _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim ArrayDataIn As System.Double
Dim value As MathPoint

value = instance.ICreatePoint(ArrayDataIn)
```

### C#

```csharp
MathPoint ICreatePoint(
   ref System.double ArrayDataIn
)
```

### C++/CLI

```cpp
MathPoint^ ICreatePoint(
   System.double% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArrayDataIn`: Array of doubles representing the coordinates (x,y,z) of the point

### Return Value

Newly created [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object or NULL if the operation fails

## VBA Syntax

See [MathUtility::ICreatePoint](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~ICreatePoint.html).

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::CreatePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreatePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
