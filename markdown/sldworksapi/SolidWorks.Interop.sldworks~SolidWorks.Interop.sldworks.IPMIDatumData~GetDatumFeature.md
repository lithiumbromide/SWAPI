---
title: "GetDatumFeature Method (IPMIDatumData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumData"
member: "GetDatumFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumFeature.html"
---

# GetDatumFeature Method (IPMIDatumData)

Gets the PMI datum feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumData
Dim value As System.Object

value = instance.GetDatumFeature()
```

### C#

```csharp
System.object GetDatumFeature()
```

### C++/CLI

```cpp
System.Object^ GetDatumFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IPMIDatumFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)

## VBA Syntax

See [PMIDatumData::GetDatumFeature](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumData~GetDatumFeature.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This method is valid only if [IPMIDatumData::GetDatumType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumType.html) returns [swPMIDatumType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumType_e.html).swPMIDatumType_DatumFeature.

## See Also

[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html)
[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
