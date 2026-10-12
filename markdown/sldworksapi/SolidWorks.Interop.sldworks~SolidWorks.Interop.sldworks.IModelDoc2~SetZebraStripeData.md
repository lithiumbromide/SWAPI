---
title: "SetZebraStripeData Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetZebraStripeData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetZebraStripeData.html"
---

# SetZebraStripeData Method (IModelDoc2)

Sets the zebra-line data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetZebraStripeData( _
   ByVal Size As System.Double, _
   ByVal Ratio As System.Double, _
   ByVal Color1 As System.Integer, _
   ByVal Color2 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Size As System.Double
Dim Ratio As System.Double
Dim Color1 As System.Integer
Dim Color2 As System.Integer

instance.SetZebraStripeData(Size, Ratio, Color1, Color2)
```

### C#

```csharp
void SetZebraStripeData(
   System.double Size,
   System.double Ratio,
   System.int Color1,
   System.int Color2
)
```

### C++/CLI

```cpp
void SetZebraStripeData(
   System.double Size,
   System.double Ratio,
   System.int Color1,
   System.int Color2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Number of stripes
- `Ratio`: Width of the stripes
- `Color1`: First color in zebra stripe design
- `Color2`: Second color in zebra stripe design

## VBA Syntax

See [ModelDoc2::SetZebraStripeData](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetZebraStripeData.html).

## Remarks

The Size parameter is inversely related; a large size value generates lots of small stripes.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetZebraStripeData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetZebraStripeData.html)
[IModelView::DisplayZebraStripes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
