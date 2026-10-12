---
title: "IPMIDimensionData Interface"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html"
---

# IPMIDimensionData Interface

Allows access to the Product and Manufacturing Information (PMI) for a dimension annotation in a STEP 242 model.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPMIDimensionData
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionData
```

### C#

```csharp
public interface IPMIDimensionData
```

### C++/CLI

```cpp
public interface class IPMIDimensionData
```

## VBA Syntax

See [PMIDimensionData](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionData.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This interface is valid only if [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.html) returns [swPMIType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPMIType_e.html).swPMIType_Dimension.

## Accessors

IAnnotation::GetPMIData

## Access Diagram

[PMIDimensionData](SWObjectModel.pdf#PMIDimensionData)

## See Also

[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html)
[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
