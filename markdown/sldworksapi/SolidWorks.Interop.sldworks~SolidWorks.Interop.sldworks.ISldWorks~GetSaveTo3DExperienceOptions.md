---
title: "GetSaveTo3DExperienceOptions Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetSaveTo3DExperienceOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSaveTo3DExperienceOptions.html"
---

# GetSaveTo3DExperienceOptions Method (ISldWorks)

Initializes save options for a [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSaveTo3DExperienceOptions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetSaveTo3DExperienceOptions()
```

### C#

```csharp
System.object GetSaveTo3DExperienceOptions()
```

### C++/CLI

```cpp
System.Object^ GetSaveTo3DExperienceOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISaveTo3DExperienceOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.html)

## VBA Syntax

See [SldWorks::GetSaveTo3DExperienceOptions](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetSaveTo3DExperienceOptions.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
