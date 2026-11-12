---
title: "GetPathType Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "GetPathType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetPathType.html"
---

# GetPathType Method (ISweptFlangeFeatureData)

Gets the type of the [sweep path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html) in this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Integer

value = instance.GetPathType()
```

### C#

```csharp
System.int GetPathType()
```

### C++/CLI

```cpp
System.int GetPathType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sweep path type as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SweptFlangeFeatureData::GetPathType](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~GetPathType.html).

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
