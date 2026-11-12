---
title: "GetPlusAndMinusTolerance Method (ISwDMDimXpertDimensionTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDimensionTolerance"
member: "GetPlusAndMinusTolerance"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetPlusAndMinusTolerance.html"
---

# GetPlusAndMinusTolerance Method (ISwDMDimXpertDimensionTolerance)

Gets the plus and minus tolerance values for this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlusAndMinusTolerance( _
   ByRef Plus As System.Double, _
   ByRef Minus As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDimensionTolerance
Dim Plus As System.Double
Dim Minus As System.Double
Dim value As System.Boolean

value = instance.GetPlusAndMinusTolerance(Plus, Minus)
```

### C#

```csharp
System.bool GetPlusAndMinusTolerance(
   out System.double Plus,
   out System.double Minus
)
```

### C++/CLI

```cpp
System.bool GetPlusAndMinusTolerance(
   [Out] System.double Plus,
   [Out] System.double Minus
)
```

### Parameters

- `Plus`: Plus tolerance value
- `Minus`: Minus tolerance value

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertDimensionTolerance::GetPlusAndMinusTolerance](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDimensionTolerance~GetPlusAndMinusTolerance.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html)
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
