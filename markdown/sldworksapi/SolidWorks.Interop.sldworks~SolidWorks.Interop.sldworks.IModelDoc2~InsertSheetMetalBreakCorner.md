---
title: "InsertSheetMetalBreakCorner Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSheetMetalBreakCorner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBreakCorner.html"
---

# InsertSheetMetalBreakCorner Method (IModelDoc2)

Inserts a break corner into a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSheetMetalBreakCorner( _
   ByVal Type As System.Integer, _
   ByVal Distance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Type As System.Integer
Dim Distance As System.Double

instance.InsertSheetMetalBreakCorner(Type, Distance)
```

### C#

```csharp
void InsertSheetMetalBreakCorner(
   System.int Type,
   System.double Distance
)
```

### C++/CLI

```cpp
void InsertSheetMetalBreakCorner(
   System.int Type,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Corner type as defined in [swBreakCornerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)
- `Distance`: Distance to break from corner

## VBA Syntax

See [ModelDoc2::InsertSheetMetalBreakCorner](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSheetMetalBreakCorner.html).

## Examples

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
