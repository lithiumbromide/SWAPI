---
title: "GetPMIType Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetPMIType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.html"
---

# GetPMIType Method (IAnnotation)

Gets the type of Product and Manufacturing Information (PMI) associated with this STEP 242 annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPMIType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.GetPMIType()
```

### C#

```csharp
System.int GetPMIType()
```

### C++/CLI

```cpp
System.int GetPMIType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

PMI type for this annotation as defined in [swPMIType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPMIType_e.html)

## VBA Syntax

See [Annotation::GetPMIType](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetPMIType.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This API does not yet support note annotations.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetPMIData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
