---
title: "InsertCurveFile Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCurveFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.html"
---

# InsertCurveFile Method (IModelDoc2)

Creates a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCurveFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertCurveFile(FileName)
```

### C#

```csharp
System.bool InsertCurveFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertCurveFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name containing the point data

### Return Value

True if the curve is created successfully, false if not

## VBA Syntax

See [ModelDoc2::InsertCurveFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCurveFile.html).

## Remarks

The curve goes through the points in the specified file.The points in the specified input file can have the X, Y, Z values separated by commas, spaces, or tabs. There should be one point per line.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertCurveFileBegin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.html)
[IModelDoc2::InsertCurveFileEnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.html)
[IModelDoc2::InsertCurveFilePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
