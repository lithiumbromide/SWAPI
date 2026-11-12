---
title: "GetDatumTarget Method (IPMIDatumData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumData"
member: "GetDatumTarget"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumTarget.html"
---

# GetDatumTarget Method (IPMIDatumData)

Gets the PMI datum target.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTarget() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumData
Dim value As System.Object

value = instance.GetDatumTarget()
```

### C#

```csharp
System.object GetDatumTarget()
```

### C++/CLI

```cpp
System.Object^ GetDatumTarget();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IPMIDatumTarget](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.html)

## VBA Syntax

See [PMIDatumData::GetDatumTarget](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumData~GetDatumTarget.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This method is valid only if [IPMIDatumData::GetDatumType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumType.html) returns [swPMIDatumType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumType_e.html).swPMIDatumType_DatumTarget.

## See Also

[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html)
[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
