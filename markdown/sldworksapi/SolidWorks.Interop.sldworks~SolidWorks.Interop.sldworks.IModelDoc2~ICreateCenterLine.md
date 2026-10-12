---
title: "ICreateCenterLine Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCenterLine.html"
---

# ICreateCenterLine Method (IModelDoc2)

Creates a center line from P1 to P2.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateCenterLine( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double

instance.ICreateCenterLine(P1, P2)
```

### C#

```csharp
void ICreateCenterLine(
   ref System.double P1,
   ref System.double P2
)
```

### C++/CLI

```cpp
void ICreateCenterLine(
   System.double% P1,
   System.double% P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`: Array of 3 doubles (x1, y1, z1) in meters that describe the first point of the line
- `P2`: Array of 3 doubles (x2, y2, z2) in meters that describe the second point of the line

### Return Value

True if success, false if not

## VBA Syntax

See [ModelDoc2::ICreateCenterLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateCenterLine.html).

## Remarks

Use [IModelDoc2::CreateCenterLineVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCenterLineVB.html) for Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays.

You can also create centerline construction geometry using [IModelDoc2::ICreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateLine2.html) and [ISketchSegment::ConstructionGeometry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~ConstructionGeometry.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLine.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
