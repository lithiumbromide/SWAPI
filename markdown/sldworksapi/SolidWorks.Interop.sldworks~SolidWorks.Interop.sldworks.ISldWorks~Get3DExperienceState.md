---
title: "Get3DExperienceState Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "Get3DExperienceState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Get3DExperienceState.html"
---

# Get3DExperienceState Method (ISldWorks)

Gets the current state of [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DExperienceState() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.Get3DExperienceState()
```

### C#

```csharp
System.int Get3DExperienceState()
```

### C++/CLI

```cpp
System.int Get3DExperienceState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

State of SOLIDWORKS Design connected to the 3DEXPERIENCE platform as defined by [sw3DExperienceState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceState_e.html)

## VBA Syntax

See [SldWorks::Get3DExperienceState](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~Get3DExperienceState.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 SP02, Revision Number 30.2
