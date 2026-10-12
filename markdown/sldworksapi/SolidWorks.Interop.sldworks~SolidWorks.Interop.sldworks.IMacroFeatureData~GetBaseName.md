---
title: "GetBaseName Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetBaseName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetBaseName.html"
---

# GetBaseName Method (IMacroFeatureData)

Gets the name of the base feature for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBaseName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.String

value = instance.GetBaseName()
```

### C#

```csharp
System.string GetBaseName()
```

### C++/CLI

```cpp
System.String^ GetBaseName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the base feature

## VBA Syntax

See [MacroFeatureData::GetBaseName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetBaseName.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
