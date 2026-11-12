---
title: "GetThread Method (IDimXpertCylinderFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCylinderFeature"
member: "GetThread"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature~GetThread.html"
---

# GetThread Method (IDimXpertCylinderFeature)

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
Dim instance As IDimXpertCylinderFeature
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
- `ThreadDepth`: Depth of the thread for a threaded hole

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCylinderFeature::GetThread](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCylinderFeature~GetThread.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertCylinderFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature.html)
[IDimXpertCylinderFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
