---
title: "CreateCenterLineVB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateCenterLineVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLineVB.html"
---

# CreateCenterLineVB Method (IModelDoc2)

Creates a center line from P1 to P2 and can be used in Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateCenterLineVB( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double

instance.CreateCenterLineVB(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
void CreateCenterLineVB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
void CreateCenterLineVB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: Location of first end point in meters
- `Y1`: Location of first end point in meters
- `Z1`: Location of first end point in meters
- `X2`: Location of second end point in meters
- `Y2`: Location of second end point in meters
- `Z2`: Location of second end point in meters

## VBA Syntax

See [ModelDoc2::CreateCenterLineVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateCenterLineVB.html).

## Remarks

You can also create centerline construction geometry using [IModelDoc2::CreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLine2.html) and [ISketchSegment::ConstructionGeometry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~ConstructionGeometry.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLine.html)
[IModelDoc2::ICreateCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCenterLine.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
