---
title: "IPMIGtolData Interface"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html"
---

# IPMIGtolData Interface

Allows access to the Product and Manufacturing Information (PMI) for a Gtol annotation in a STEP 242 model.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPMIGtolData
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
```

### C#

```csharp
public interface IPMIGtolData
```

### C++/CLI

```cpp
public interface class IPMIGtolData
```

## VBA Syntax

See [PMIGtolData](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This interface is valid only if [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.html) returns [swPMIType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPMIType_e.html).swPMIType_GTol.

## Accessors

IAnnotation::GetPMIData

## Access Diagram

[PMIGtolData](SWObjectModel.pdf#PMIGtolData)

## See Also

[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html)
[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html)
