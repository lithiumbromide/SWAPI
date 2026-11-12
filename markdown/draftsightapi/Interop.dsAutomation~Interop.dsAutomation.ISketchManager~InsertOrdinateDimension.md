---
title: "InsertOrdinateDimension Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertOrdinateDimension"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertOrdinateDimension.html"
---

# InsertOrdinateDimension Method (ISketchManager)

Inserts an ordinate Dimension.

## Syntax

### Visual Basic

```vb
Function InsertOrdinateDimension( _
   ByVal DatumPositionDblArray As System.Object, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String, _
   ByVal Measure As dsOrdinateDimensionMeasure_e _
) As OrdinateDimension
```

### C#

```csharp
OrdinateDimension InsertOrdinateDimension(
   System.object DatumPositionDblArray,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride,
   dsOrdinateDimensionMeasure_e Measure
)
```

### JScript

```
function InsertOrdinateDimension(
   DatumPositionDblArray : System.Object,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String,
   Measure : dsOrdinateDimensionMeasure_e
) : OrdinateDimension;
```

### Managed Extensions for C++

```
OrdinateDimension* InsertOrdinateDimension(
   System.Object* DatumPositionDblArray,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride,
   dsOrdinateDimensionMeasure_e Measure
)
```

### C++/CLI

```cpp
OrdinateDimension^ InsertOrdinateDimension(
   System.Object^ DatumPositionDblArray,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride,
   dsOrdinateDimensionMeasure_e Measure
)
```

### Parameters

- `DatumPositionDblArray`: Array of three doubles indicating the point where to place the datum
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the ordinate Dimension
- `DimensionTextOverride`: Text with which to override the default ordinate Dimension text
- `Measure`: Type of measurement as defined in [dsOrdinateDimensionMeasure_e](Interop.dsAutomation~Interop.dsAutomation.dsOrdinateDimensionMeasure_e.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.2
