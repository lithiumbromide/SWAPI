---
title: "GetThread Method (ISwDMDimXpertCylinderFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCylinderFeature"
member: "GetThread"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetThread.html"
---

# GetThread Method (ISwDMDimXpertCylinderFeature)

Gets thread information for this DimXpert cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThread( _
   ByRef IsThreaded As System.Boolean, _
   ByRef ThreadDesignation As System.String, _
   ByRef ThreadDepth As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCylinderFeature
Dim IsThreaded As System.Boolean
Dim ThreadDesignation As System.String
Dim ThreadDepth As System.Double
Dim value As System.Boolean

value = instance.GetThread(IsThreaded, ThreadDesignation, ThreadDepth)
```

### C#

```csharp
System.bool GetThread(
   out System.bool IsThreaded,
   out System.string ThreadDesignation,
   out System.double ThreadDepth
)
```

### C++/CLI

```cpp
System.bool GetThread(
   [Out] System.bool IsThreaded,
   [Out] System.String^ ThreadDesignation,
   [Out] System.double ThreadDepth
)
```

### Parameters

- `IsThreaded`: True if the cylinder is threaded; false otherwise
- `ThreadDesignation`: Description of the thread
- `ThreadDepth`: Depth of the thread for a threaded cylindrical hole

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCylinderFeature::GetThread](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCylinderFeature~GetThread.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.html)
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
