---
title: "CreateCenterLine Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLine.html"
---

# CreateCenterLine Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateCenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateCenterLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCenterLine( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Object
Dim P2 As System.Object
Dim value As System.Boolean

value = instance.CreateCenterLine(P1, P2)
```

### C#

```csharp
System.bool CreateCenterLine(
   System.object P1,
   System.object P2
)
```

### C++/CLI

```cpp
System.bool CreateCenterLine(
   System.Object^ P1,
   System.Object^ P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`: Array of 3 doubles (x1, y1, z1) in meters that describe the first point of the line
- `P2`: Array of 3 doubles (x2, y2, z2) in meters that describe the second point of the line

### Return Value

True if success, false if not

## VBA Syntax

See [ModelDoc2::CreateCenterLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateCenterLine.html).

## Remarks

Use [IModelDoc2::CreateCenterLineVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCenterLineVB.html) for Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays.

You can also create centerline construction geometry using [IModelDoc2::CreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLine2.html) and [ISketchSegment::ConstructionGeometry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~ConstructionGeometry.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ICreateCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCenterLine.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
