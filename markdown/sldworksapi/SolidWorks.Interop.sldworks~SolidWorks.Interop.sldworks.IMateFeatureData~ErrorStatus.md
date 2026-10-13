---
title: "ErrorStatus Property (IMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateFeatureData"
member: "ErrorStatus"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData~ErrorStatus.html"
---

# ErrorStatus Property (IMateFeatureData)

Gets the status of adding or editing this mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ErrorStatus As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateFeatureData
Dim value As System.Integer

value = instance.ErrorStatus
```

### C#

```csharp
System.int ErrorStatus {get;}
```

### C++/CLI

```cpp
property System.int ErrorStatus {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Status of adding or editing this mate as defined in [swAddMateError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddMateError_e.html)

## VBA Syntax

See [MateFeatureData::ErrorStatus](ms-its:sldworksapivb6.chm::/sldworks~MateFeatureData~ErrorStatus.html).

## See Also

[IMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html)
[IMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
