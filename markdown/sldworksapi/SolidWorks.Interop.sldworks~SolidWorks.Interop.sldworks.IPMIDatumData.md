---
title: "IPMIDatumData Interface"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html"
---

# IPMIDatumData Interface

Allows access to the Product and Manufacturing Information (PMI) for a datum annotation in a STEP 242 model.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPMIDatumData
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumData
```

### C#

```csharp
public interface IPMIDatumData
```

### C++/CLI

```cpp
public interface class IPMIDatumData
```

## VBA Syntax

See [PMIDatumData](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumData.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This interface is valid only if [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.html) returns [swPMIType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPMIType_e.html).swPMIType_Datum.

## Accessors

[IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html)

## Access Diagram

[PMIDatumData](SWObjectModel.pdf#PMIDatumData)

## See Also

[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html)
[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
