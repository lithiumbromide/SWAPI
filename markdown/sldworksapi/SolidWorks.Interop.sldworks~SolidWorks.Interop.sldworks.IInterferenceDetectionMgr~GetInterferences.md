---
title: "GetInterferences Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetInterferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.html"
---

# GetInterferences Method (IInterferenceDetectionMgr)

Calculates and gets the interferences.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterferences() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Object

value = instance.GetInterferences()
```

### C#

```csharp
System.object GetInterferences()
```

### C++/CLI

```cpp
System.Object^ GetInterferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [interferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference.html)

## VBA Syntax

See [InterferenceDetectionMgr::GetInterferences](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetInterferences.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount.html)
[IInterferenceDetectionMgr::IGetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
