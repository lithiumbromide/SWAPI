---
title: "GetInterferenceCount Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetInterferenceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount.html"
---

# GetInterferenceCount Method (IInterferenceDetectionMgr)

Calculates and gets the number of interferences.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterferenceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Integer

value = instance.GetInterferenceCount()
```

### C#

```csharp
System.int GetInterferenceCount()
```

### C++/CLI

```cpp
System.int GetInterferenceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of interferences

## VBA Syntax

See [InterferenceDetectionMgr::GetInterferenceCount](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetInterferenceCount.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

## Remarks

Call this method before calling [IInterferenceDetectionMgr::IGetInterferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.html) to determine the size of the array for the interferences.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
