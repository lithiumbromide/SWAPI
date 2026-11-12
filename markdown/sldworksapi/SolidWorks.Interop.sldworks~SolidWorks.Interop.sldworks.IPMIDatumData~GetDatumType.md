---
title: "GetDatumType Method (IPMIDatumData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumData"
member: "GetDatumType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumType.html"
---

# GetDatumType Method (IPMIDatumData)

Gets the PMI datum type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumData
Dim value As System.Integer

value = instance.GetDatumType()
```

### C#

```csharp
System.int GetDatumType()
```

### C++/CLI

```cpp
System.int GetDatumType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

PMI datum type as defined in [swPMIDatumType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumType_e.html)

## VBA Syntax

See [PMIDatumData::GetDatumType](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumData~GetDatumType.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html)
[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.html)
[IPMIDatumData::GetDatumFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumFeature.html)
[IPMIDatumData::GetDatumTarget Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumTarget.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
