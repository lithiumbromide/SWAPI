---
title: "GetFixedFace Method (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "GetFixedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GetFixedFace.html"
---

# GetFixedFace Method (IConvertSolidFeatureData)

Gets the face that remains in place when the part is flattened in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFixedFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Object

value = instance.GetFixedFace()
```

### C#

```csharp
System.object GetFixedFace()
```

### C++/CLI

```cpp
System.Object^ GetFixedFace();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See

[ConvertSolidFeatureData::GetFixedFace](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~GetFixedFace.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

[IConvertSolidFeatureData::SetFixedFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SetFixedFace.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
