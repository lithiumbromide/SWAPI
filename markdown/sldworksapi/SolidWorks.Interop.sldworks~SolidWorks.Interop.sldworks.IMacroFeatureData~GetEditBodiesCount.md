---
title: "GetEditBodiesCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEditBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.html"
---

# GetEditBodiesCount Method (IMacroFeatureData)

Gets the number of bodies to be modified by this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Integer

value = instance.GetEditBodiesCount()
```

### C#

```csharp
System.int GetEditBodiesCount()
```

### C++/CLI

```cpp
System.int GetEditBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies to be modified by this macro feature

## VBA Syntax

See [MacroFeatureData::GetEditBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEditBodiesCount.html).

## Remarks

Call this method before calling [IMacroFeatureData::IGetEditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetEditBodies.html) to size the array for that method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::ISetEditBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.html)
[IMacroFeatureData::EditBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.html)
[IMacroFeatureData::EnableMultiBodyConsume Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
