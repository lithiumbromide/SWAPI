---
title: "GetZebraStripeData Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetZebraStripeData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetZebraStripeData.html"
---

# GetZebraStripeData Method (IModelDoc2)

Gets zebra line data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetZebraStripeData( _
   ByRef Size As System.Double, _
   ByRef Ratio As System.Double, _
   ByRef Color1 As System.Integer, _
   ByRef Color2 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Size As System.Double
Dim Ratio As System.Double
Dim Color1 As System.Integer
Dim Color2 As System.Integer

instance.GetZebraStripeData(Size, Ratio, Color1, Color2)
```

### C#

```csharp
void GetZebraStripeData(
   out System.double Size,
   out System.double Ratio,
   out System.int Color1,
   out System.int Color2
)
```

### C++/CLI

```cpp
void GetZebraStripeData(
   [Out] System.double Size,
   [Out] System.double Ratio,
   [Out] System.int Color1,
   [Out] System.int Color2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Number of stripes
- `Ratio`: Width of the stripes
- `Color1`: First color in zebra stripe design
- `Color2`: Second color in zebra stripe design

### Return Value

## VBA Syntax

See [ModelDoc2::GetZebraStripeData](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetZebraStripeData.html).

## Remarks

The size parameter is inversely related; a large size value generates lots of small stripes.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetZebraStripeData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetZebraStripeData.html)
[IModelView::DisplayZebraStripes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
