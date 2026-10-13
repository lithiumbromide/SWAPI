---
title: "GetPMIData Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetPMIData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html"
---

# GetPMIData Method (IAnnotation)

Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPMIData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetPMIData()
```

### C#

```csharp
System.object GetPMIData()
```

### C++/CLI

```cpp
System.Object^ GetPMIData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IPMIDatumData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.html), [IPMIDimensionData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html), [IPMIGtolData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html); null or Nothing if the model is a drawing or no PMI data is associated with this annotation (see **Remarks**)

## VBA Syntax

See [Annotation::GetPMIData](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetPMIData.html).

## Examples

[Get PMI Data (VBA)](Get_PMI_Data_Example_VB.htm)
[Get PMI Data (C#)](Get_PMI_Data_Example_CSharp.htm)

## Remarks

This method is not valid for drawings.

Use [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.html) to determine the feature data object returned by this method.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
